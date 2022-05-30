def test_storage():
    from core.managers.storage import StorageManager
    from core.hardware.storage import StorageDevice

    drives = StorageManager().get_info()

    assert type(drives) == list

    for drive in drives:
        assert type(drive) == StorageDevice
        assert type(drive.model) == str
        assert type(drive.connector) == str
        assert type(drive.location) == str
        assert type(drive.drive_type) == str or not drive.drive_type
