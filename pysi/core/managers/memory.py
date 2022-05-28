from core.managers.base import BaseManager
from core.hardware.memory import RAM
from core.hardware.memory import RAMSlot
from util.util import Util

class RAMManager(BaseManager[RAM]):
    def __init__(self):
        pass
    
    def get_info(self) -> list[RAM] | None:
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
        
        try:
            return getattr(self, "_" + kernel.get("short"))()
        except Exception:
            return []

    # The following are marked private
    # since they're meant for
    # internal usage only.
    def _osx(self) -> list[RAM] | None:
        raise NotImplementedError

    def _win(self) -> list[RAM] | None:
        try:
            from util.memory_type import MEMORY_TYPE
            from wmi import WMI

            RAM_MODULES = WMI().instances("Win32_PhysicalMemory")
            MODULES = []

            for MODULE in RAM_MODULES:
                bank = MODULE.wmi_property("BankLabel").value
                capacity = MODULE.wmi_property("Capacity").value
                channel = MODULE.wmi_property("DeviceLocator").value
                manufacturer = MODULE.wmi_property("Manufacturer").value
                _type = MEMORY_TYPE[MODULE.wmi_property("SMBIOSMemoryType").value]
                frequency = MODULE.wmi_property("ConfiguredClockSpeed").value
                part_no = MODULE.wmi_property("PartNumber").value.strip()

                MODULES.append(
                    RAM(
                        part_no,
                        _type,
                        RAMSlot(bank, channel),
                        int(frequency) * 10**6,
                        manufacturer,
                        capacity
                    )
                )
            
            return MODULES
        except Exception:
            return []
    
    def _linux(self) -> list[RAM] | None:
        raise NotImplementedError