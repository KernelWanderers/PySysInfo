# PySysInfo Changelog

## v0.1.0

* Added `extract_from_pnp()` to `Util` 
    - Windows-only feature which extracts the Device-Vendor, or Product-Vendor, IDs from a PNPDeviceID, if possible.

* Added `construct_pci_path()` to `Util` 
    - Attempts to construct a valid and OpenCore-standard PCI path based on the value provided and OS.

* Added `construct_acpi_path()` to `Util` 
    - Attempts to construct a valid and OpenCore-standard ACPI path based on the value provided and OS.

* Added `split_at_convert()` to `Util` 
    - Divides a list into two at a given index, and combines both sides into their own respective strings.

* Added `feat_available()` to `Util` 
    - Checks if a feature bit returns true relative to the EAX and ECX register, and register IDX provided.

* Implemented Storage device detection for Windows, alongside  accompanying `BUS_TYPE` and `MEDIA_TYPE` enums

* Implemented `cfgmgr32` API interops
    - Used to obtain a device node for more verbose inspection

* Implemented Memory module detection for Windows; alongside an accompanying `MEMORY_TYPE` enum

* Implemented input device detection for Windows (special thanks to @1Revenger1 for helping us with this!)
    - Properly identifies parent driver / protocol type

* Implemented Network controller detection for Windows

* Implemented GPU detection for Windows

* Implemented Audio controller detection for Windows
    - Also attempts to detect ALC codec, if found available

* Implemented GPU detection for macOS

* Implemented Audio controller detection for macOS

* Implemented RAM detection for macOS

* Added enums for `HDA_CONTROLLER` and `HDA_CODEC` 
    - Helps with HDA controller/codec detection on macOS.

* Added `get_cpu_vendor()` to `Util`

* Added `get_hda_codec()` to `Util`

* Added `get_hda_controller()` to `Util`

* Added `is_hackintosh()` to `Util`

* Added unit tests for each core module