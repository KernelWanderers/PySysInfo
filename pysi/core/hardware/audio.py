class AudioController:
    def __init__(
        self,
        dev_id: str,
        ven_id: str,
        model: str | None = None,
        codec: str | None = None
    ):
        self.model = model
        """ The model name of this Audio controller. """

        self.dev_id = dev_id
        """ The Device ID of this Audio controller. """

        self.ven_id = ven_id
        """ The Vendor ID of this Audio controller. """

        self.codec = codec
        """ The ALC codec of this Audio controller (if available.) """