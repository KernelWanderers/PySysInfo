# PySysInfo Changelog

## v0.1.0 (May 28, 2022 - Current)

* Added `extract_from_pnp()` to `Util` (May 28, 2022)
    - Windows-only feature which extracts the Device-Vendor, or Product-Vendor, IDs from a PNPDeviceID, if possible.

* Added `construct_pci_path()` to `Util` (May 28, 2022)
    - Attempts to construct a valid and OpenCore-standard PCI path based on the value provided and OS.

* Added `construct_acpi_path()` to `Util` (May 28, 2022)
    - Attempts to construct a valid and OpenCore-standard ACPI path based on the value provided and OS.

* Added `split_at_convert()` to `Util` (May 28, 2022)
    - Divides a list into two at a given index, and combines both sides into their own respective strings.

* Added `feat_available()` to `Util` (May 28, 2022)
    - Checks if a feature bit returns true relative to the EAX and ECX register, and register IDX provided.

* Implemented Storage device detection for Windows, alongside  accompanying `BUS_TYPE` and `MEDIA_TYPE` enums (May 28, 2022)

* Implemented `cfgmgr32` API interops (May 28, 2022)
    - Used to obtain a device node for more verbose inspection

* Implemented Memory module detection for Windows; alongside an accompanying `MEMORY_TYPE` enum (May 28, 2022)

* Implemented input device detection for Windows (special thanks to @1Revenger1 for helping us with this!) (May 28, 2022)
    - Properly identifies parent driver / protocol type

* Implemented Network controller detection for Windows (May 28, 2022)

* Implemented GPU detection for Windows (May 28, 2022)

* Implemented Audio controller detection for Windows (May 28, 2022)
    - Also attempts to detect ALC codec, if found available

* Implemented GPU detection for macOS (May 28, 2022)

* Implemented Audio controller detection for macOS (May 28, 2022)

* Implemented RAM detection for macOS (May 28, 2022)

* Added enums for `HDA_CONTROLLER` and `HDA_CODEC` 
    - Helps with HDA controller/codec detection on macOS. (May 28, 2022)

* Added `get_cpu_vendor()` to `Util` (May 30, 2022)

* Added `get_hda_codec()` to `Util` (May 30, 2022)

* Added `get_hda_controller()` to `Util` (May 30, 2022)

* Added `is_hackintosh()` to `Util` (May 30, 2022)

* Added unit tests (May 30, 2022)

* Implemented PCI path convention conversion utilities for `Util` (Sep 3, 2022)

* Fixed broken imports on macOS (Sep 3, 2022)