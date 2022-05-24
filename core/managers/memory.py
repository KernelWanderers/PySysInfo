from .base import BaseManager
from ..hardware.memory import RAM
from ...util.util import Util

class RAMManager(BaseManager[RAM]):
    def __init__(self):
        pass
    
    def mem_info(self) -> list[RAM]:
        """
        Extracts information about the RAM module(s)
        inside of the current system.

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
    def __osx(self) -> list[RAM]:
        raise NotImplementedError

    def __win(self) -> list[RAM]:
        raise NotImplementedError
    
    def __linux(self) -> list[RAM]:
        raise NotImplementedError