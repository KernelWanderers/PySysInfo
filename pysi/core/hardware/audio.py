class AudioController:
    def __init__(
        self,
        model: str,
        dev_id: str,
        ven_id: str,
        pci: str | None = None,
        codec: str | None = None
    ):
        self.model = model
        """ The model name of this Audio controller. """

        self.dev_id = dev_id
        """ The Device ID of this Audio controller. """

        self.ven_id = ven_id
        """ The Vendor ID of this Audio controller. """

        self.pci = pci
        """ The raw PCI path of this Audio controller (if available.) """

        self.codec = codec
        """ The ALC codec of this Audio controller (if available.) """

        if (
            type(self.ven_id) == str and
            "10ec" in self.ven_id.lower()
        ):
            alc_codec = "ALC" + hex(int(self.ven_id, 16))[2:]

            self.codec = alc_codec