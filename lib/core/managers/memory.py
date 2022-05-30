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
        try:
            import core.helper.ioreg as ioreg

            if Util.get_cpu_vendor() == "Apple":
                return

            interface = ioreg.corefoundation_to_native(
                ioreg.IORegistryEntryCreateCFProperties(
                    ioreg.IORegistryEntryFromPath(
                        ioreg.kIOMasterPortDefault,
                        b"IODeviceTree:/memory"
                    ),
                    None,
                    ioreg.kCFAllocatorDefault,
                    ioreg.kNilOptions
                )[1]
            )

            modules = []
            part_no = []
            types = []
            slots = []
            frequency = []
            manufacturer = []
            sizes = []
            length = None

            for prop in interface:
                value = interface[prop]

                if not value:
                    continue

                if type(value) == bytes:
                    if "reg" in prop.lower() and length:
                        for i in range(length):
                            try:
                                # Converts non-0 values from the 'reg' property
                                # into readable integer values representing the memory capacity.
                                sizes.append(
                                    [
                                        round(n * 0x010000 / 0x10) * 10**6
                                        for n in value.replace(b"\x00", b"")
                                    ][i]
                                )
                            except Exception:
                                part_no = types = \
                                    slots = frequency = \
                                    manufacturer = sizes = []
                                break

                    else:
                        try:
                            value = [
                                x.decode()
                                for x in value.split(b"\x00")
                                if type(x) == bytes and x.decode().strip()
                            ]
                        except Exception:
                            continue

                if "part-number" in prop:
                    length = len(value)

                    for i in range(length):
                        part_no.append(value[i])

                else:
                    if not length:
                        return

                    for i in range(length):
                        if "dimm-types" in prop.lower():
                            types.append(value[i])

                        elif "slot-names" in prop.lower():
                            bank, channel = value[i].split("/")

                            slots.append(RAMSlot(bank, channel))

                        elif "dimm-speeds" in prop.lower():
                            frequency.append(
                                int(value[i].split(" ")[0]) * 10**6
                            )

                        elif "dimm-manufacturer" in prop.lower():
                            manufacturer.append(value[i])

                ioreg.IOObjectRelease(i)

            for i in range(length):
                modules.append(
                    RAM(
                        part_no[i],
                        types[i],
                        slots[i],
                        frequency[i],
                        manufacturer[i],
                        sizes[i]
                    )
                )

            return modules
        except Exception:
            return []

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
                _type = MEMORY_TYPE[MODULE.wmi_property(
                    "SMBIOSMemoryType").value]
                frequency = MODULE.wmi_property("ConfiguredClockSpeed").value
                part_no = MODULE.wmi_property("PartNumber").value.strip()

                MODULES.append(
                    RAM(
                        part_no,
                        _type,
                        RAMSlot(bank, channel),
                        int(frequency) * 10**6,
                        manufacturer,
                        capacity * 10**6
                    )
                )

            return MODULES
        except Exception:
            return []

    def _linux(self) -> list[RAM] | None:
        raise NotImplementedError
