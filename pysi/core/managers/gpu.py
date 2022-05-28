from core.managers.base import BaseManager
from core.hardware.gpu import GPU
from util.util import Util

class GPUManager(BaseManager[GPU]):
    def __init__(self):
        pass

    def get_info(self) -> list[GPU] | None:
        """
        Extracts information about the GPU(s) inside
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
    def _osx(self, default=True) -> list[GPU] | None:
        try:
            import core.helper.ioreg as ioreg
            import binascii

            if default:
                device = {
                    "IOProviderClass": "IOPCIDevice",
                    # Bit mask matching, ensuring that the 3rd byte is one of the display controller (0x03).
                    "IOPCIClassMatch": "0x03000000&0xff000000",
                }
            else:
                device = {"IONameMatched": "gpu*"}

            interface = ioreg.ioiterator_to_list(
                ioreg.IOServiceGetMatchingServices(
                    ioreg.kIOMasterPortDefault,
                    device,
                    None
                )[1]
            )

            GPUS = []

            for i in interface:
                device = ioreg.corefoundation_to_native(
                    ioreg.IORegistryEntryCreateCFProperties(
                        i, 
                        None, 
                        ioreg.kCFAllocatorDefault, 
                        ioreg.kNilOptions
                    )
                )[1]

                # I don't know why there needs to be
                # a try clause here, but it does.
                try:
                    # For Apple's AGX (ARM64 iGFX)

                    if (
                        not default and

                        # If both return true, that means
                        # we aren't dealing with a GPU device.
                        not "gpu" in device.get("IONameMatched", "").lower() and
                        not "AGX" in device.get("CFBundleIdentifierKernel", "")
                    ):
                        continue
                except Exception:
                    continue

                model = device.get("model")
                ven = "0x" + (
                    binascii.b2a_hex(
                        bytes(
                            reversed(device.get("vendor-id"))
                        )
                    ).decode()[4:]
                )

                if not model:
                    continue

                if default:
                    model = bytes(model).decode()
                    model = model[:len(model) - 1]

                    dev = "0x" + (
                        binascii.b2a_hex(
                            bytes(reversed(device.get("device-id")))
                        ).decode()[4:]
                    )

                    plane = device.get("acpi-path", "")

                    pci_path = Util.construct_pci_path(i)
                    acpi_path = Util.construct_acpi_path(plane)

                    GPUS.append(
                        GPU(
                            model,
                            dev,
                            ven,
                            pci_path,
                            acpi_path,
                        )
                    )
                
                else:
                    gpuconf = device.get("GPUConfigurationVariable", {})
                    dev = ""

                    cores = gpuconf.get("num_cores")
                    ne_cores = gpuconf.get("num_gps")
                    gen = gpuconf.get("gpu_gen")

                    GPUS.append(
                        GPU(
                            model,
                            dev,
                            ven,
                            None,
                            None,
                            None,
                            None,
                            cores,
                            ne_cores,
                            gen
                        )
                    )

            if default:
                GPUS += self._osx(False)

            return GPUS
        except Exception:
            return []

    def _win(self) -> list[GPU] | None:
        try:
            from wmi import WMI

            DEVICES = WMI().instances("Win32_VideoController")
            GPUS = []

            for DEVICE in DEVICES:
                model = DEVICE.wmi_property("Name").value
                pnpid = DEVICE.wmi_property("PNPDeviceID").value
                ven, dev = [x[1] for x in Util.extract_from_pnp(pnpid)]
                pci_path = Util.construct_pci_path(pnpid)
                acpi_path = Util.construct_acpi_path(pnpid)

                GPUS.append(
                    GPU(
                        model,
                        dev,
                        ven,
                        pci_path,
                        acpi_path,
                    )
                )
            
            return GPUS
        except Exception:
            return []


    def _linux(self) -> list[GPU] | None:
        raise NotImplementedError
