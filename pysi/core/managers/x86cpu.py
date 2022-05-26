from core.managers.base import BaseManager
from core.hardware.x86cpu import X86CPU
from util.util import Util


class X86CPUManager(BaseManager[X86CPU]):
    def __init__(self):
        pass

    def get_info(self) -> list[X86CPU]:
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
    def _osx(self) -> list[X86CPU] | None:
        import subprocess

        def exec_sysctl(*args) -> str | None:
            return subprocess.check_output(["sysctl", *args]).decode().split(": ")[-1].strip()

        model = exec_sysctl("machdep.cpu.brand_string")
        vendor = "Intel" if "intel" in exec_sysctl(
            "machdep.cpu.vendor").lower() else "AMD"
        features = exec_sysctl("machdep.cpu.features").split(" ")
        cores = exec_sysctl("machdep.cpu.core_count")
        threads = exec_sysctl("machdep.cpu.thread_count")

        return [X86CPU(
            cores=cores,
            threads=threads,
            features=features,
            vendor=vendor,
            model=model,
            codename=None
        )]

    def _win(self) -> list[X86CPU] | None:
        raise NotImplementedError

    def _linux(self) -> list[X86CPU] | None:
        raise NotImplementedError
