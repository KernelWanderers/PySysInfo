from .base import BaseManager
from ..hardware.input import InputDevice
from ...util.util import Util

class InputManager(BaseManager[InputDevice]):
    def __init__(self):
        pass
    
    def mem_info(self) -> list[InputDevice]:
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
        
        return getattr(self, "__" + kernel.get("short"))()

    # The following are marked private
    # since they're meant for
    # internal usage only.
    def __osx(self) -> list[InputDevice]:
        raise NotImplementedError

    def __win(self) -> list[InputDevice]:
        raise NotImplementedError
    
    def __linux(self) -> list[InputDevice]:
        raise NotImplementedError