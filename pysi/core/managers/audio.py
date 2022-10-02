from pysi.core.managers.base import BaseManager
from pysi.core.hardware.audio import AudioController
from pysi.util.util import Util

class AudioManager(BaseManager[AudioController]):
    def __init__(self):
        pass
    
    def get_info(self) -> list[AudioController] | None:
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
        
        try:
            return getattr(self, "_" + kernel.get("short"))()
        except Exception:
            return []

    # The following are marked private
    # since they're meant for
    # internal usage only.
    def _osx(self, default=False) -> list[AudioController] | None:
        try:
            import pysi.core.helper.ioreg as ioreg
            import binascii

            # TODO: implementation for Apple ARM64
            #       audio controllers.
            if Util.get_cpu_vendor() == "Apple":
                return
            
            if default:
                device = {
                    "IOProviderClass": "IOPCIDevice",
                    # Bit mask matching, ensuring that the 3rd byte is one of the multimedia controller (0x04).
                    "IOPCIClassMatch": "0x04000000&0xff000000"
                }
            else:
                device = {"IOProviderClass": "IOHDACodecDevice"}

            HDAS = []

            interface = ioreg.ioiterator_to_list(
                ioreg.IOServiceGetMatchingServices(
                    ioreg.kIOMasterPortDefault,
                    device,
                    None
                )[1]
            )

            for i in interface:
                device = ioreg.corefoundation_to_native(
                    ioreg.IORegistryEntryCreateCFProperties(
                        i,
                        None,
                        ioreg.kCFAllocatorDefault,
                        ioreg.kNilOptions
                    )
                )[1]
                
                if not default:
                    # Ensure it's the AppleHDACodec device
                    if device.get("DigitalAudioCapabilities"):
                        return

                    ven_dev = hex(device.get("IOHDACodecVendorID"))
                    ven = "0x" + ven_dev[2:6]
                    dev = "0x" + ven_dev[6:]

                    if len(ven) > 6 or len(dev) > 6:
                        continue
                    
                    HDAS.append(
                        AudioController(
                            dev,
                            ven,
                            None,
                            Util.get_hda_codec(dev, ven),
                        )
                    )

                else:
                   # Reverse the byte sequence, and format it using `binascii` – remove leading 0s
                    dev = "0x" + (
                        binascii.b2a_hex(
                            bytes(reversed(device.get("device-id")))
                        ).decode()[4:]
                    )


                    # Reverse the byte sequence, and format it using `binascii` – remove leading 0s
                    ven = "0x" + (
                        binascii.b2a_hex(
                            bytes(reversed(device.get("vendor-id")))
                        ).decode()[4:]
                    )

                    if len(dev) > 6 or len(ven) > 6:
                        continue

                    HDAS.append(
                        AudioController(
                            dev,
                            ven,
                            Util.get_hda_controller(dev, ven),
                            None
                        )
                    )
                
                ioreg.IOObjectRelease(i)

            if not default:
                HDAS += self._osx(True)

            return HDAS
        except Exception:
            return []

    def _win(self) -> list[AudioController] | None:
        try:
            from wmi import WMI
            from pysi.util.util import Util

            HDAS = WMI().instances("Win32_SoundDevice")
            CONTROLLERS = []

            for HDA in HDAS:
                pnpid = HDA.wmi_property("PNPDeviceID")

                if (
                    not pnpid or
                    not getattr(pnpid, "value", False) or
                    not "HDAUDIO" in pnpid.value
                ):
                    continue
                else:
                    pnpid = pnpid.value

                name = HDA.wmi_property("ProductName").value
                ven, dev = [x[1] for x in Util.extract_from_pnp(pnpid)]
                codec = None

                if "10ec" in ven.lower():
                    name = f"Realtek ALC{dev.upper()}"
                    codec = f"ALC{dev.upper()[2:].lstrip('0')}"

                CONTROLLERS.append(
                    AudioController(
                        dev,
                        ven,
                        name,
                        codec
                    )
                )

            return CONTROLLERS
        except Exception:
            return []
    
    def _linux(self) -> list[AudioController] | None:
        raise NotImplementedError