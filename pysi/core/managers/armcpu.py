from core.managers.base import BaseManager
from core.hardware.armcpu import ARMCPU
from util.util import Util


class ARMCPUManager(BaseManager[ARMCPU]):
    def __init__(self):
        pass

    def cpu_info(self) -> list[ARMCPU] | None:
        """ 
        Extracts information about the CPU(s) inside 
        of the current system.
        
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
    def _osx(self) -> list[ARMCPU] | None:
        raise NotImplementedError

    def _win(self) -> list[ARMCPU] | None:
        raise NotImplementedError

    def _linux(self) -> list[ARMCPU] | None:
        raise NotImplementedError
