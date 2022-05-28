def exec():
    from core.managers.gpu import GPUManager

    gpus = GPUManager().get_info()

    print(
        "\n" + ("=" * 25) + "\n" +
        "|\t   GPU   \t|" +
        "\n" + ("=" * 25)
    )

    for gpu in gpus:
        print(
            "\n".join([
                f"Model: {gpu.model}",
                f"PCI Path: {gpu.pci}",
                f"ACPI Path: {gpu.acpi}",
                f"Device ID: {gpu.dev_id}",
                f"Vendor ID: {gpu.ven_id}\n"
            ]) + "\n"
        )
