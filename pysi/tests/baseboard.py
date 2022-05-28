def exec():
    from core.managers.baseboard import BaseboardManager

    mobo = BaseboardManager().baseboard_info()

    print(
        ("=" * 25) + "\n" +
        "| MOTHERBOARD/MAC MODEL |" +
        "\n" + ("=" * 25) + "\n" +
        "\n".join([
            f"Model: {mobo.model}",
            f"Manufacturer: {mobo.manufacturer}"
        ]) + "\n"
    )