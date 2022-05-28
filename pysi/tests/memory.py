def exec():
    from core.managers.memory import RAMManager

    rams = RAMManager().get_info()

    print(
        ("=" * 25) + "\n" +
        "|\t   RAM   \t|" +
        "\n" + ("=" * 25)
    )

    for ram in rams:
        print(
            "\n".join([
                f"Part-No: {ram.part_no}",
                f"Capacity (Bytes): {ram.capacity}",
                f"Bank: {ram.slot.bank}",
                f"Channel: {ram.slot.channel}",
                f"Frequency (Hz): {ram.frequency}",
                f"Type: {ram.ram_type}",
                f"Manufacturer: {ram.manufacturer}\n"
            ]) + "\n"
        )
