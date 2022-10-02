class Util:
    """ General purpose utilities for the user and internal usage. """

    def get_kernel() -> dict:
        """ Obtains the kernel name of the current OS. """
        from platform import system

        kernel = system().lower()

        if kernel == "darwin":
            return {
                "kernel": kernel,
                "os": "macOS",
                "short": "osx"
            }
        elif kernel == "windows":
            return {
                "kernel": kernel,
                "os": "Windows",
                "short": "win"
            }
        elif kernel == "linux":
            return {
                "kernel": kernel,
                "os": "Linux",
                "short": "linux"
            }
        else:
            return {
                "kernel": kernel,
                "os": "Unknown"
            }

    def extract_from_pnp(pnpid: str) -> tuple[tuple[str, str], tuple[str, str]] | None:
        """
        Extracts the `Device:Vendor`, or `Product:Vendor` IDs from the given PNPDeviceID. 

        Expected formats of a PNPDeviceID:

            `PCI\\VEN_<VEN-ID>&DEV_<DEV-ID>&SUBSYS_<SUBSYS-ID>&REV_<REVISION>\\...` \n
            `PCI\\VEN_<VEN-ID>&PID_<PRODUCT-ID>&SUBSYS_<SUBSYS-ID>&REV_<REVISION>\\...`
        """
        try:
            import re
            regex = r'(?<=(VEN|DEV|PID)_)((\d|\w){4})'

            TYPE = {
                "PID": "Product ID",
                "VEN": "Vendor ID",
                "DEV": "Device ID"
            }

            found = re.findall(regex, pnpid)

            if not any('ven' in x[0].lower() for x in found): return

            return tuple(
                [
                    (TYPE[x[0]], "0x" + x[1]) for x in 
                    found
                ]
            )
        except Exception:
            return

    def construct_pci_path(with_value, kernel: str | None = None) -> str | None:
        """
        Auxiliary function to construct a PCI path from an accommodating 
        value given by the OS.

        Necessary values depending on the OS:
            - Windows: `<PNPDeviceID>` (E.g: `PCI\\VEN_<VEN-ID>&DEV_<DEV-ID>&SUBSYS_<SUBSYS-ID>&REV_<REVISION>\\...`) \n
            - macOS: `<io_iterator_t>` (For more, see: https://developer.apple.com/documentation/iokit/iokitlib_h) \n
            - Linux: `<Device-path>`   (E.g: `/sys/class/drm/card0/device/`)

        Available `kernel` parameter values:
            - `win`
            - `win32`
            - `windows`
            - `darwin`
            - `osx`
            - `macos`
            - `linux`
        """


        if not kernel:
            kernel = Util.get_kernel().get("os")

        if kernel.lower() in ["darwin", "osx", "macos"]:
            from pysi.core.helper.ioreg import kCFAllocatorDefault, kNilOptions, IORegistryEntryGetLocationInPlane, IOObjectConformsTo, IOObjectRelease, ioname_t_to_str, corefoundation_to_native, IORegistryEntryGetParentEntry, IORegistryEntryCreateCFProperty
            
            paths = []
            entry = with_value

            while entry:
                if IOObjectConformsTo(entry, b"IOPCIDevice"):
                    try:
                        bus, func = ([
                            hex(int(i, 16)) for i in
                            ioname_t_to_str(
                                IORegistryEntryGetLocationInPlane(
                                    entry, b"IOService", None
                                )[1]
                            ).split(',')
                        ] + ["0x0"])[:2]

                        paths.append(
                            f"Pci({bus},{func})"
                        )
                    except ValueError:
                        break

                elif IOObjectConformsTo(entry, b"IOACPIPlatformDevice"):
                    paths.append(
                        "PciRoot(" +
                        hex(
                            int(
                                corefoundation_to_native(
                                    IORegistryEntryCreateCFProperty(
                                        entry,
                                        "_UID",
                                        kCFAllocatorDefault,
                                        kNilOptions
                                    )
                                ) or 0
                            )
                        ) +
                        ")"
                    )
                    break

                elif IOObjectConformsTo(entry, b"IOPCIBridge"):
                    pass

                else:
                    paths = []
                    break

                parent = IORegistryEntryGetParentEntry(entry, b"IOService", None)[1]

                if entry != with_value:
                    IOObjectRelease(entry)

                entry = parent
        
            if paths:
                return "/".join(reversed(paths))

        elif kernel.lower() in ["win", "win32", "windows"]:
            try:
                import wmi
                
                pci_path = ""
                raw_path = (
                    wmi.WMI().query(
                        f"SELECT * FROM Win32_PnPEntity WHERE PNPDeviceID = '{with_value}'"
                    )[0]
                    .GetDeviceProperties(["DEVPKEY_Device_LocationPaths"])[0][0]
                    .Data
                )

                if not raw_path:
                    return

                devices = raw_path

                for device in devices:
                    # A valid PCI device shouldn't have
                    # `USB(...)` at any component position in its path.
                    if "usb" in device.lower():
                        break
                    
                    # We're just looking to build the PCI path,
                    # not the ACPI path.
                    if "acpi" in device.lower():
                        continue

                    for comp in device.split("#"):
                        if "pciroot" in comp.lower():
                            pci_path += f"PciRoot({hex(int(comp[:-1].split('(')[1], 16))})"
                            continue

                        bus, func = Util.split_at_convert(
                            comp[:-1].split("(")[1],
                            2
                        )

                        pci_path += f"/Pci({hex(int(bus, 16))},{hex(int(func, 16))})"
                
                return pci_path
            except Exception:
                return

        elif kernel.lower() in ["linux", "cringe"]:
            try:
                import os

                # We're not going to return the ACPI path in any way,
                # we just need it to determine the amount of components
                # our final PCI path should have.
                acpi = open(f"{with_value}/firmware_node/path", "r").read().strip()
                pci = open(f"{with_value}/uevent", "r").read().strip()

                if not acpi or not pci: 
                    return

                # The yielded PCI path, if any.
                pci_path = ""

                # Parent PCI description
                #
                # <domain>:<bus>:<slot>.<function>
                slot = ""

                # Whether or not there's 1 or 2 components
                # of the entire PCI path.
                #
                # Examples of this:
                # 1 - PciRoot(0x0)/Pci(0x2,0x0)
                # 2 - PciRoot(0x0)/Pci(0x1,0x0)/Pci(0x0,0x0)
                amount = len(acpi.split(".")) - 2

                # Whether or not we found what we were looking for.
                found = False

                for line in pci.split("\n"):
                    if "pci_slot_name" in line.lower():
                        slot = line.split("=")[1]
                        break

                if slot:
                    paths = os.listdir("/sys/bus/pci/devices/")

                    for path in paths:
                        nested = os.listdir(f"/sys/bus/pci/devices/{path}")

                        if found:
                            break

                        if slot in nested:
                            
                            for nest in nested:
                                if found:
                                    break

                                if (
                                    "pcie" in nest and
                                    not slot in nest
                                ):
                                    pci_path += f"PciRoot({hex(int(path.split(':')[1], 16))})"

                                    """
                                    `slotc` - Child slot
                                    `funcc` - Child function
                                    `slotp` - Parent slot
                                    `funcp` - Parent function
                                    """
                                    slotc, funcc = Util.get_valid_slot(path)

                                    pci_path += f"/Pci({slotc},{funcc})"

                                    if amount == 2:
                                        slotp, funcp = Util.get_valid_slot(slot)
                                        pci_path += f"/Pci({slotp},{funcp})"

                                    found = True
                                    break
                    
                    # In some cases, there won't
                    # be an accommodating directory in
                    # /sys/bus/pci/devices/* which will have
                    # the current slot name.
                    #
                    # So, we format the current one, and use that.
                    # This should, by default,
                    # only have a single PCI path component.
                    if not pci_path:
                        domain = hex(
                            int(
                                slot.split(":")[1],
                                16
                            )
                        )
                        slot, func = Util.get_valid_slot(slot)

                        pci_path = f"PciRoot({domain})/Pci({slot},{func})"

                    return pci_path
            except Exception:
                return

        else:
            return

    def get_valid_slot(slot: str) -> list[str] | None:
        """ Properly formats the slot values for PCI devices (mainly used for Linux) """

        try:
            return [
                hex(int(n, 16)) 
                for n in slot.split(":")[2].split(".")
            ]
        except Exception:
            return

    def construct_acpi_path(with_value: str, kernel: str | None = None) -> str:
        """
        Auxiliary function to construct an ACPI path from an accommodating 
        value given by the OS.

        Necessary values depending on the OS:
            - Windows: `<PNPDeviceID>` (E.g: `PCI\\VEN_<VEN-ID>&DEV_<DEV-ID>&SUBSYS_<SUBSYS-ID>&REV_<REVISION>\\...`) \n
            - macOS: `<IOACPIPlane>` (For more, see: https://developer.apple.com/documentation/iokit/iokitlib_h) \n
            - Linux: `<Device-path>`   (E.g: `/sys/class/drm/card0/device/`)

        Available `kernel` parameter values:
            - `win`
            - `win32`
            - `windows`
            - `darwin`
            - `osx`
            - `macos`
            - `linux`
        """

        if not kernel:
            kernel = Util.get_kernel().get("os")

        if kernel.lower() in ["darwin", "osx", "macos"]:
            try:
                return "".join(
                    [
                        ("\\" if "sb" in a.lower() else ".") + a.split("@")[0]
                        for a in with_value.split(":")[1].split("/")[1:]
                    ]
                )
            except Exception:
                return

        elif kernel.lower() in ["win", "win32", "windows"]:
            try:
                import wmi

                acpi_path = ""
                raw_path = (
                    wmi.WMI().query(
                        f"SELECT * FROM Win32_PnPEntity WHERE PNPDeviceID = '{with_value}'"
                    )[0]
                    .GetDeviceProperties(["DEVPKEY_Device_LocationPaths"])[0][0]
                    .Data
                )

                devices = raw_path

                for device in devices:
                    # A valid PCI device shouldn't have
                    # `USB(...)` at any component position in its path.
                    if "usb" in device.lower():
                        break

                    # We're only looking to construct
                    # the ACPI path.
                    if "acpi" not in device.lower():
                        continue

                    for comp in [x.split("(")[1][:-1] for x in device.split("#")]:
                        if "_SB" in comp:
                            acpi_path += "\\_SB"
                        else:
                            acpi_path += "." + comp

                return acpi_path
            except Exception:
                return

        elif kernel.lower() in ["linux", "cringe"]:
            try:
                return open(f"{with_value}/firmware_node/path", "r").read().strip()
            except Exception:
                return

    def pci_convert(
        path: str | list[str],
        current: str,
        target: str = "OpenCore"
    ) -> str | list[str] | None:
        """ 
        Converts a PCI path from one format to another.

        For the time being, the only way
        to convert from all other formats
        to the Linux format is by specifying
        that the bus id is unknown.

        Available "formats":
            - Windows: `PCIROOT(X)#PCI(XYZQ)#...`
            - macOS: `[('X'), ('XY', 'ZQ'), ...]`
            - Linux: `['XXXX:YY:ZZ.Q', ...]`
            - OpenCore: `PciRoot(0xM)/Pci(0xNN,0xRR)`

        Examples:
            - Windows: `PCIROOT(0)#PCI(0200)`
            - macOS: `[('0'), ('2', '0')]`
            - Linux: `['0000:00:02.0']`
            - OpenCore: `PciRoot(0x0)/Pci(0x2,0x0)`

        Returns: The converted value, or "UNKNOWN FORMAT"
        """

        if current.lower() == target.lower():
            return path

        import re

        values = []

        if target.lower() == "linux":
            pci_path = []
            domain = ""
        else:
            pci_path = ""

        # Examples of how `divide()` works:
        #
        # '1F03' -> ('1f', '3')
        # '0200' -> ('2', '0')
        # '0'    -> '0'
        def divide(x): return (
            hex(int(x[:2], 16))[2:],
            hex(int(x[2:], 16))[2:]
        ) if len(x) > 1 else x

        if current.lower() == "windows":
            values = [
                divide(re.search(r'(?<=\()(.+)(?=\))', val).group())
                for val in
                path.split("#")
                if re.search(r'(?<=\()(.+)(?=\))', val)
            ]

        elif current.lower() == "macos":
            values = path

        elif (
            current.lower() == "linux" and
            type(path) == list[str]
        ):
            def convert(x): return hex(int(x, 16))[2:]

            for pcidebug in path:
                domain = convert(pcidebug.split(":")[0])

                if domain not in values:
                    values.append(domain)

                dev, func = pcidebug.split(":")[2].split(",")

                values.append((
                    convert(dev),
                    convert(func)
                ))

        elif current.lower() == "opencore":
            components = path.split("/")

            for component in components:
                attributes = re.search(
                    r'(?<=\()(.+)(?=\))',
                    component
                ).group()

                if "pciroot" in component.lower():
                    values += attributes[2:]
                    continue

                dev, func = attributes.split(",")

                values.append((dev, func))

        else:
            return "UNKNOWN FORMAT"

        for val in values:
            if type(val) != str:
                dev, func = val

            if target.lower() == "windows":
                if type(val) == str:
                    pci_path += f"PCIROOT({val})"
                    continue

                pci_path += f"#PCI({dev.zfill(2)}{func.zfill(2)})"

            elif target.lower() == "macos":
                pci_path = values
                break

            elif target.lower() == "linux":
                if type(val) == str and not domain:
                    domain = val
                    continue

                pci_path.append(
                    f"{domain.zfill(4)}:xx:{dev.zfill(2)}.{func.zfill(1)}")

            elif target.lower() == "opencore":
                if type(val) == str:
                    pci_path += f"PciRoot({hex(int(val))})"
                    continue

                dev = hex(int(dev, 16))
                func = hex(int(func, 16))

                pci_path += f"/Pci({dev},{func})"

        return pci_path

    def validate_pci_format(path: str, format: str) -> bool:
        # PCIROOT(0)#PCI(0200)
        if format.lower() == "windows":
            if (
                "#" not in path or

                # Someone seems to have
                # forgotten to put the
                # '#' character in-between...
                ")p" in path.lower()
            ):
                return False

            for comp in path.split("#"):
                ind = comp.split("(")

                # If there's only a single
                # value, it means that it's
                # improper, syntax-wise.
                if len(ind) < 2:
                    return False

                ind = ind[-1].replace(")", "")

                # If there's nothing
                # inside of the PCI path
                # component: it's improper, syntax-wise.
                if not ind:
                    return False

                # Only accept 4-digit [hex] values.
                if len(ind) > 4 or len(ind) < 4:
                    return False

                for val in ind:
                    # If a value isn't according to
                    # the hex number base, it's invalid.
                    try:
                        int(val, 16)
                    except Exception:
                        return False

        elif format.lower() == "opencore":
            pass

    def get_gpu_codename(dev: str, ven: str) -> str | None:
        if "1002" in ven.lower():
            from .gpus import AMD

            GPUS = AMD
        
        elif "10de" in ven.lower():
            from .gpus import NVIDIA

            GPUS = NVIDIA

        def convert_underscore(value: str) -> str:
            return " ".join([
                x[0].upper() + x[1:].lower()
                for x in value.split("_")
            ])

        codename = None

        for GPU in GPUS:
            for id in GPU.value:
                if (
                    id[0].lstrip("0x") in ven.lower() and
                    id[1].lstrip("0x") in dev.lower()
                ):
                    codename = convert_underscore(GPU.name)
                    break

        return codename

    def get_hda_controller(dev: str, ven: str) -> str | None:
        """ Obtains the HD Audio Controller from the given Vendor and Device ID. """
        try:
            from pysi.core.helper.hda_list import HDA_CONTROLLER_LIST

            return HDA_CONTROLLER_LIST[
                f"_0x{ven[2:].upper()}_0x{dev[2:].upper()}"
            ].value
        except Exception:
            return

    def get_hda_codec(dev: str, ven: str) -> str | None:
        """ Obtains the HD Audio Codec from the given Vendor and Device ID. """
        try:
            import re
            from pysi.core.helper.hda_list import HDA_CODEC_LIST
            
            value = HDA_CODEC_LIST[f"_0x{ven[2:].upper()}_0x{dev[2:].upper()}"].value
            codec = re.search(
                r"((\d{1,2}?|\w{1,4})?\d(\w|\d)+((\/|-)(\d|\w)+)?)",
                value
            )

            if codec:
                codec = codec.group()
            else:
                codec = value

            return codec
        except Exception:
            return

    def get_cpu_vendor(kernel: str = "") -> str | None:
        """ Obtains the vendor of this CPU, if possible. """
        _kernel = Util.get_kernel().get("os")

        if (
            not kernel or
            kernel != _kernel
        ):
            kernel = _kernel

        if kernel.lower() in ["darwin", "osx", "macos"]:
            try:
                from subprocess import check_output

                if ".vendor" not in check_output(["sysctl", "machdep.cpu"]).decode():
                    return "Apple"
                
                return check_output(["sysctl", "machdep.cpu.vendor"]).decode()
            except Exception:
                return

        elif kernel.lower() in ["win", "win32", "windows"]:
            try:
                from wmi import WMI

                return WMI().instances("Win32_Processor")[0].wmi_property("Manufacturer").value
            except Exception:
                return

        elif kernel.lower() in ["linux", "cringe"]:
            try:
                import re

                return re.search(r"(?<=vendor_id\t\:\s+)(.+)(?=\n)", open("/proc/cpuinfo", "r").read().lower()).group()
            except Exception:
                return

    def split_at_convert(with_list: list, index: int) -> list:
        """ 
        Splits at the given index and combines both sides into their own respective string. 
        
        Example: `split_at_convert([1, 2, 3, 4], 2)` -> `['12', '34']`
        """

        return [
            ''.join(with_list[:index]),
            ''.join(with_list[index:])
        ]

    def feat_available(cpu, leaf, subleaf, reg_idx, bit):
        """ 
        Checks if a feature is available for this CPU (they're stored in EAX, EBX, ECX and EDX registers.) 

        Only works for x86 systems, AFAIK.
        """

        return bool(
            (1 << bit) &
            cpu(leaf, subleaf)[reg_idx]
        )

    def is_hackintosh() -> bool:
        """ Determines whether or not the current machine is a hackintosh. """

        import os
        import subprocess

        # We're targeting machines running macOS.
        if Util.get_kernel().get("os").lower() != "macos":
            return False

        kern_ver = int(os.uname().release.split(".")[0])

        if kern_ver > 19:
            kext_loaded = subprocess.run(
                ["kmutil", "showloaded", "--list-only", "--variant-suffix", "release"],
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
            )
        else:
            kext_loaded = subprocess.run(
                ["kextstat", "-l"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT
            )

        return any(
            x in kext_loaded.stdout.decode().lower() 
            for x in ("fakesmc", "virtualsmc")
        )