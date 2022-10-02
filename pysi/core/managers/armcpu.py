from pysi.core.managers.base import BaseManager
from pysi.core.hardware.armcpu import ARMCPU
from pysi.util.util import Util


class ARMCPUManager(BaseManager[ARMCPU]):
    def __init__(self):
        pass

    def get_info(self) -> list[ARMCPU] | None:
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
        try:
            import pysi.core.helper.ioreg as ioreg
            from pysi.core.hardware.armcpu import ARMCPU

            def exec_sysctl(*args):
                import subprocess

                return subprocess.check_output(["sysctl", *args]).decode().split(": ")[-1].strip()

            try:
                exec_sysctl("machdep.cpu.vendor")
                return []
            except Exception:
                pass

            IODT = ioreg.corefoundation_to_native(
                ioreg.IORegistryEntryCreateCFProperties(
                    ioreg.IORegistryEntryFromPath(
                        ioreg.kIOMasterPortDefault,
                        b"IODeviceTree:/"
                    ),
                    None,
                    ioreg.kCFAllocatorDefault,
                    ioreg.kNilOptions
                )[1]
            )

            CPU0 = ioreg.corefoundation_to_native(
                ioreg.IORegistryEntryCreateCFProperties(
                    ioreg.IORegistryEntryFromPath(
                        ioreg.kIOMasterPortDefault,
                        b"IODeviceTree:/cpus/cpu0@0"
                    ),
                    None,
                    ioreg.kCFAllocatorDefault,
                    ioreg.kNilOptions
                )[1]
            )

            codename = IODT.get("platform-name", b"").decode().upper()
            arm_t = CPU0.get("compatible", b"").decode()[-1].replace(",", " ")
            model = exec_sysctl("machdep.cpu.brand_string")
            cores = int(exec_sysctl("machdep.cpu.core_count"))
            threads = int(exec_sysctl("machdep.cpu.thread_count"))

            return [
                ARMCPU(
                    cores,
                    model,
                    threads,
                    "Apple",
                    arm_t,
                    codename
                )
            ]
        except Exception:
            return []

    def _win(self) -> list[ARMCPU] | None:
        raise NotImplementedError

    def _linux(self) -> list[ARMCPU] | None:
        raise NotImplementedError
