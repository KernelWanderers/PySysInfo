class Util:
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

                pci_path.append(f"{domain.zfill(4)}:xx:{dev.zfill(2)}.{func.zfill(1)}")

            elif target.lower() == "opencore":
                if type(val) == str:
                    pci_path += f"PciRoot({hex(int(val))})"
                    continue

                dev = hex(int(dev, 16))
                func = hex(int(func, 16))

                pci_path += f"/Pci({dev},{func})"

        return pci_path

    def feat_available(cpu, leaf, subleaf, reg_idx, bit):
        return bool(
            (1 << bit) &
            cpu(leaf, subleaf)[reg_idx]
        )

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
