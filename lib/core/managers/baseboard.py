from core.hardware.baseboard import Baseboard
from core.managers.base import BaseManager
from util.util import Util


class BaseboardManager(BaseManager[Baseboard]):
    """ 
    Obtains information about the current system's baseboard.

    On macOS, this would be the machine model.
    """

    def baseboard_info(self) -> Baseboard | None:
        """
        Extracts information about the baseboard inside
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
            return

    # The following are marked private
    # since they're meant for
    # internal usage only.
    def _osx(self) -> Baseboard | None:
        import core.helper.ioreg as ioreg

        BASEBOARD = ioreg.corefoundation_to_native(
            ioreg.IORegistryEntryCreateCFProperties(
                next(
                    ioreg.ioiterator_to_list(
                        ioreg.IOServiceGetMatchingServices(
                            ioreg.kIOMasterPortDefault,
                            ioreg.IOServiceMatching(
                                b"IOPlatformExpertDevice"),
                            None
                        )[1]
                    )
                ),
                None,
                ioreg.kCFAllocatorDefault,
                ioreg.kNilOptions
            )
        )[1]

        model = BASEBOARD.get("model").decode()
        manuf = BASEBOARD.get("manufacturer").decode()

        return Baseboard(
            model=model,
            manufacturer=manuf
        )

    def _win(self) -> Baseboard | None:
        import wmi

        MOBO = wmi.WMI().instances("Win32_BaseBoard")[0]

        return Baseboard(
            model=MOBO.wmi_property("Product").value,
            manufacturer=MOBO.wmi_property("Manufacturer").value
        )

    def _linux(self) -> Baseboard | None:
        path = "/sys/devices/virtual/dmi/id"

        return Baseboard(
            model=open(f"{path}/board_name", "r").read().strip(),
            manufacturer=open(f"{path}/board_vendor", "r").read().strip()
        )
