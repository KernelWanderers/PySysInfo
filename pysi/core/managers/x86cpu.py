from core.managers.base import BaseManager
from core.hardware.x86cpu import X86CPU
from util.util import Util
from numpy import sort


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
        features = sort(exec_sysctl("machdep.cpu.features").split(" "))
        cores = exec_sysctl("machdep.cpu.core_count")
        threads = exec_sysctl("machdep.cpu.thread_count")

        return [X86CPU(
            cores,
            model,
            threads,
            features,
            vendor,
            None
        )]

    def _win(self) -> list[X86CPU] | None:
        try:
            import wmi
            from core.helper.cpuid_win import CPUID
            from core.helper.cpuid_feat import CPUID_INSTRUCTIONS

            CPU = wmi.WMI().instances("Win32_Processor")[0]

            cpu = CPUID()

            features = []

            for feature in CPUID_INSTRUCTIONS:
                if type(feature.value) == list:
                    for value in feature.value:
                        if Util.feat_available(cpu, *value):
                            features.append(feature.name)
                            break
                    continue

                if Util.feat_available(cpu, *feature.value):
                    name = feature.name[1:] if feature.name.startswith("_") else feature.name
                    
                    features.append(name)

            model = CPU.wmi_property("Name").value
            cores = CPU.wmi_property("NumberOfCores").value
            threads = CPU.wmi_property("NumberOfLogicalProcessors").value
            vendor = CPU.wmi_property("Manufacturer").value
            features = sort(features)

            return [X86CPU(
                cores,
                model,
                threads,
                features,
                vendor
            )]
        except Exception:
            return []

    def _linux(self) -> list[X86CPU] | None:
        raise NotImplementedError
