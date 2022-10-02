from pysi.core.managers.base import BaseManager
from pysi.core.hardware.storage import StorageDevice
from pysi.util.util import Util


class StorageManager(BaseManager[StorageDevice]):
    def __init__(self):
        pass

    def get_info(self) -> list[StorageDevice]:
        """
        Extracts information about the Storage device(s)
        inside of the current system.

        Automatically takes care of providing the
        appropriate method in context of the platform.
        """
        kernel = Util.get_kernel()

        # Unsupported platform or error.
        if kernel.get("name", "").lower() == "unknown":
            return []

        # try:
        return getattr(self, "_" + kernel.get("short"))()
        # except Exception:
        #     return []

    # The following are marked private
    # since they're meant for
    # internal usage only.
    def _osx(self) -> list[StorageDevice] | None:
        try:
            import core.helper.ioreg as ioreg
            STORAGE = {
                "Solid State": "Solid State Drive (SSD)",
                "Rotational": "Hard Disk Drive (HDD)",
            }

            device = {"IOProviderClass": "IOBlockStorageDevice"}

            interface = ioreg.ioiterator_to_list(
                ioreg.IOServiceGetMatchingServices(
                    ioreg.kIOMasterPortDefault,
                    device,
                    None
                )[1]
            )

            DRIVES = []

            for i in interface:
                device = ioreg.corefoundation_to_native(
                    ioreg.IORegistryEntryCreateCFProperties(
                        i,
                        None,
                        ioreg.kCFAllocatorDefault,
                        ioreg.kNilOptions
                    )
                )[1]

                product = device.get("Device Characteristics")
                protocol = device.get("Protocol Characteristics")

                if (
                    not product or
                    not protocol
                ):
                    continue

                try:
                    name = product.get("Product Name").strip()
                    drive_t = STORAGE.get(product.get("Medium Type").strip(), "N/A")

                    cnt_type = protocol.get("Physical Interconnect").strip()
                    location = protocol.get("Physical Interconnect Location").strip()

                    if cnt_type.lower() == "pci-express":
                        drive_t = "Non-Volatile Memory Express (NVMe)"
                except Exception:
                    continue

                DRIVES.append(
                    StorageDevice(
                        name,
                        cnt_type,
                        location,
                        drive_t
                    )
                )

                ioreg.IOObjectRelease(i)

            return DRIVES
        except Exception as e:
            raise e
            return []

    def _win(self) -> list[StorageDevice] | None:
        try:
            from wmi import WMI
            from pysi.util.storage_type import BUS_TYPE, MEDIA_TYPE
            from operator import itemgetter

            STORAGE_DEV = WMI(namespace="Microsoft/Windows/Storage").instances("MSFT_PhysicalDisk")
            DEVICES = []

            for STORAGE in STORAGE_DEV:
                model = STORAGE.wmi_property("FriendlyName").value
                drive_type = MEDIA_TYPE.get(
                    STORAGE.wmi_property("MediaType").value, 
                    "Unspecified"
                )
                con_t, location = itemgetter("type", "location")(
                    BUS_TYPE.get(
                        STORAGE.wmi_property("BusType").value,
                        "Unknown"
                    )
                )

                if "nvme" in con_t.lower():
                    drive_type = "NVMe"
                    con_t = "PCI Express"

                DEVICES.append(
                    StorageDevice(
                        model,
                        con_t,
                        location, 
                        drive_type
                    )
                )

            return DEVICES
        except Exception:
            return []

    def _linux(self) -> list[StorageDevice] | None:
        raise NotImplementedError
