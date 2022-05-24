from .base import BaseManager
from ..hardware.network import NetworkController
from ...util.util import Util

class NetworkManager(BaseManager[NetworkController]):
    def __init__(self):
        pass
    
    def net_info(self) -> list[NetworkController]:
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
        
        return getattr(self, "__" + kernel.get("short"))()

    # The following are marked private
    # since they're meant for
    # internal usage only.
    def __osx(self) -> list[NetworkController]:
        raise NotImplementedError

    def __win(self) -> list[NetworkController]:
        raise NotImplementedError
    
    def __linux(self) -> list[NetworkController]:
        raise NotImplementedError