class StorageDevice:
    def __init__(
        self,
        model: str,
        connector: str,
        location: str,
        drive_type: str | None = None
    ):
        self.connector = connector
        self.drive_type = drive_type
        self.location = location
        self.model = model

    @property
    def model(self) -> str:
        """ The model name of this storage device. """
        return self.model

    @property
    def connector(self) -> str:
        """ The connector type for this storage device. """
        return self.connector

    @property
    def location(self) -> str:
        """ The location of this storage device. """
        return self.location

    @property
    def drive_type(self) -> str | None:
        """ The type of drive (SSD/HDD/etc., if available.) """
        return self.drive_type