def exec():
    from core.managers.audio import AudioManager

    hdas = AudioManager().get_info()

    if not hdas:
        return

    print(
        "\n" + ("=" * 25) + "\n" +
        "|\t  AUDIO   \t|" +
        "\n" + ("=" * 25)
    )

    for hda in hdas:
        print(
            "\n".join([
                f"Model: {hda.model}",
                f"Device ID: {hda.dev_id}",
                f"Vendor ID: {hda.ven_id}",
                f"Codec: {hda.codec}"
            ]) + "\n"
        )
