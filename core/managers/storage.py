from .base import BaseManager
from ..hardware.storage import StorageDevice
from ...util.util import Util

class StorageManager(BaseManager[StorageDevice]):
    def __init__(self):
        pass
    
    def net_info(self) -> list[StorageDevice]:
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
        
        return getattr(self, "__" + kernel.get("short"))()

    # The following are marked private
    # since they're meant for
    # internal usage only.
    def __osx(self) -> list[StorageDevice]:
        raise NotImplementedError

    def __win(self) -> list[StorageDevice]:
        raise NotImplementedError
    
    def __linux(self) -> list[StorageDevice]:
        raise NotImplementedError