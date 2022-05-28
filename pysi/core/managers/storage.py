from core.managers.base import BaseManager
from core.hardware.storage import StorageDevice
from util.util import Util


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

        try:
            return getattr(self, "_" + kernel.get("short"))()
        except Exception:
            return []

    # The following are marked private
    # since they're meant for
    # internal usage only.
    def _osx(self) -> list[StorageDevice] | None:
        raise NotImplementedError

    def _win(self) -> list[StorageDevice] | None:
        try:
            from wmi import WMI
            from util.storage_type import BUS_TYPE, MEDIA_TYPE
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
