from core.managers.base import BaseManager
from core.hardware.input import InputDevice
from util.util import Util
from util.input import InputUtil

class InputManager(BaseManager[InputDevice]):
    def __init__(self):
        pass
    
    def get_info(self) -> list[InputDevice] | None:
        """
        Extracts information about the Input devices
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
    def _osx(self) -> list[InputDevice] | None:
        raise NotImplementedError

    def _win(self) -> list[InputDevice] | None:
        try:
            from wmi import WMI

            wmi = WMI()

            KEYBOARDS = wmi.instances("Win32_Keyboard")
            POINTING  = wmi.instances("Win32_PointingDevice")

            def get(items):
                data = []

                for item in items:
                    description = item.wmi_property("Description").value
                    pnpid = item.wmi_property("PNPDeviceID").value
                    driver = InputUtil.get_protocol(pnpid, wmi)

                    data.append(
                        InputDevice(
                            description,
                            driver
                        )
                    )

                return data

            return [
                *get(KEYBOARDS),
                *get(POINTING)
            ]
        except Exception:
            return []
    
    def _linux(self) -> list[InputDevice] | None:
        raise NotImplementedError