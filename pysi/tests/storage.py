def exec():
    from core.managers.storage import StorageManager

    drives = StorageManager().get_info()

    print(
        "\n" + ("=" * 25) + "\n" +
        "|\t STORAGE  \t|" +
        "\n" + ("=" * 25)
    )

    for drive in drives:
        print(
            "\n".join([
                f"Model: {drive.model}",
                f"Connector: {drive.connector}",
                f"Location: {drive.location}",
                f"Drive Type: {drive.drive_type}\n"
            ]) + "\n"
        )
