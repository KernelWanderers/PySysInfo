from core.managers.base import BaseManager
from core.hardware.audio import AudioController
from util.util import Util

class AudioManager(BaseManager[AudioController]):
    def __init__(self):
        pass
    
    def get_info(self) -> list[AudioController] | None:
        """
        Extracts information about the Audio controller(s)
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
    def _osx(self) -> list[AudioController] | None:
        raise NotImplementedError

    def _win(self) -> list[AudioController] | None:
        try:
            from wmi import WMI
            from util.util import Util

            HDAS = WMI().instances("Win32_SoundDevice")
            CONTROLLERS = []

            for HDA in HDAS:
                pnpid = HDA.wmi_property("PNPDeviceID")

                if (
                    not pnpid or
                    not getattr(pnpid, "value", False) or
                    not "HDAUDIO" in pnpid.value
                ):
                    continue
                else:
                    pnpid = pnpid.value

                name = HDA.wmi_property("ProductName").value
                ven, dev = [x[1] for x in Util.extract_from_pnp(pnpid)]
                codec = None

                if "10ec" in ven.lower():
                    name = f"Realtek ALC{dev.upper()}"
                    codec = f"ALC{dev.upper()[2:].lstrip('0')}"

                CONTROLLERS.append(
                    AudioController(
                        name,
                        dev,
                        ven,
                        codec
                    )
                )

            return CONTROLLERS
        except Exception:
            return []
    
    def _linux(self) -> list[AudioController] | None:
        raise NotImplementedError