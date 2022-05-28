from core.managers.base import BaseManager
from core.hardware.network import NetworkController
from util.util import Util

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
    def _osx(self) -> list[NetworkController] | None:
        raise NotImplementedError

    def _win(self) -> list[NetworkController] | None:
        try:
            from wmi import WMI
            from util.util import Util

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