def exec():
    from core.managers.network import NetworkManager

    nics = NetworkManager().get_info()

    print(
        "\n" + ("=" * 25) + "\n" +
        "|\t NETWORK  \t|" +
        "\n" + ("=" * 25)
    )

    for nic in nics:
        print(
            "\n".join([
                f"Model: {nic.model}",
                f"PCI Path: {nic.pci}",
                f"ACPI Path: {nic.acpi}",
                f"Device ID: {nic.dev_id}",
                f"Vendor ID: {nic.ven_id}\n"
            ]) + "\n"
        )
