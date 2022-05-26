class StorageDevice:
    def __init__(
        self,
        model: str,
        connector: str,
        location: str,
        drive_type: str | None = None
    ):
        self.connector = connector
        """ The connector type for this storage device. """

        self.drive_type = drive_type
        """ The type of drive (SSD/HDD/etc., if available.) """

        self.location = location
        """ The location of this storage device. """

        self.model = model
        """ The model name of this storage device. """