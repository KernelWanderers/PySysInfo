from pysi.core.managers.base import BaseManager
from pysi.core.hardware.network import NetworkController
from pysi.util.util import Util

class NetworkManager(BaseManager[NetworkController]):
    def __init__(self):
        pass
    
    def get_info(self) -> list[NetworkController] | None:
        """
        Extracts information about the Network controller(s)
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
    def _osx(self, default=True) -> list[NetworkController] | None:
        try:
            import core.helper.ioreg as ioreg
            import binascii
        
            if default:
                device = {
                    "IOProviderClass": "IOPCIDevice",
                    # Bit mask matching, ensuring that the 3rd byte is one of the network controller (0x02).
                    "IOPCIClassMatch": "0x02000000&0xff000000",
                }
            else:
                device = {"IOProviderClass": "IOPlatformDevice"}

            interface = ioreg.ioiterator_to_list(
                ioreg.IOServiceGetMatchingServices(
                    ioreg.kIOMasterPortDefault,
                    device,
                    None
                )[1]
            )

            NICS = []

            for i in interface:
                device = ioreg.corefoundation_to_native(
                    ioreg.IORegistryEntryCreateCFProperties(
                        i,
                        None,
                        ioreg.kCFAllocatorDefault,
                        ioreg.kNilOptions
                    )
                )[1]

                if default:
                    dev = "0x" + (
                        binascii.b2a_hex(bytes(reversed(device.get("device-id")))).decode()[
                            4:
                        ]
                    )
                    ven = "0x" + (
                        binascii.b2a_hex(bytes(reversed(device.get("vendor-id")))).decode()[
                            4:
                        ]
                    )

                    pci_path = Util.construct_pci_path(i)
                    acpi_path = Util.construct_acpi_path(device.get("acpi-path"))

                    NICS.append(
                        NetworkController(
                            "Unknown",
                            dev,
                            ven,
                            pci_path,
                            acpi_path
                        )
                    )
                
                else:
                    if ioreg.IOObjectConformsTo(i, b'IO80211Controller'):
                        NICS.append(
                            NetworkController(
                                device.get("IOModel"),
                                "N/A",
                                device.get("IOVendor"),
                                None,
                                None
                            )
                        )

                ioreg.IOObjectRelease(i)

            if default:
                NICS += self._osx(False)
            
            return NICS
        except Exception:
            return []

    def _win(self) -> list[NetworkController] | None:
        try:
            from wmi import WMI
            from pysi.util.util import Util

            NICS = WMI().instances("Win32_NetworkAdapter")

            CONTROLLERS = []

            for NIC in NICS:
                pnpid = NIC.wmi_property("PNPDeviceID")

                if (
                    not pnpid or
                    not getattr(pnpid, "value", False) or
                    not "PCI" in pnpid.value
                ):
                    continue
                else:
                    pnpid = pnpid.value

                name = NIC.wmi_property("ProductName").value
                ven, dev = [x[1] for x in Util.extract_from_pnp(pnpid)]                
                pci_path = Util.construct_pci_path(pnpid)
                acpi_path = Util.construct_acpi_path(pnpid)

                CONTROLLERS.append(
                    NetworkController(
                        name,
                        dev,
                        ven,
                        pci_path,
                        acpi_path
                    )
                )

            return CONTROLLERS
        except Exception:
            return []
    
    def _linux(self) -> list[NetworkController] | None:
        raise NotImplementedError