from .base import BaseManager
from ..hardware.x86cpu import X86CPU
from ..hardware.armcpu import ARMCPU
from ...util.util import Util


class CPUManager(BaseManager[X86CPU | ARMCPU]):
    def __init__(self):
        pass

    def cpu_info(self) -> list[X86CPU] | list[ARMCPU]:
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

        return getattr(self, "__" + kernel.get("short"))()

    # The following are marked private
    # since they're meant for
    # internal usage only.
    def __osx(self) -> list[X86CPU] | list[ARMCPU]:
        raise NotImplementedError

    def __win(self) -> list[X86CPU] | list[ARMCPU]:
        raise NotImplementedError

    def __linux(self) -> list[X86CPU] | list[ARMCPU]:
        raise NotImplementedError
