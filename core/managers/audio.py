from .base import BaseManager
from ..hardware.audio import AudioController
from ...util.util import Util

class AudioManager(BaseManager[AudioController]):
    def __init__(self):
        pass
    
    def net_info(self) -> list[AudioController]:
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
        
        return getattr(self, "__" + kernel.get("short"))()

    # The following are marked private
    # since they're meant for
    # internal usage only.
    def __osx(self) -> list[AudioController]:
        raise NotImplementedError

    def __win(self) -> list[AudioController]:
        raise NotImplementedError
    
    def __linux(self) -> list[AudioController]:
        raise NotImplementedError