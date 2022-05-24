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
        self.dev_id = dev_id
        self.ven_id = ven_id
        self.pci = pci
        self.codec = codec

    @property
    def model(self) -> str:
        """ The model name of this Audio controller. """
        return self.model

    @property
    def dev_id(self) -> str:
        """ The Device ID of this Audio controller. """
        return self.dev_id
    
    @property
    def ven_id(self) -> str:
        """ The Vendor ID of this Audio controller. """
        return self.ven_id

    @property
    def pci(self) -> str:
        """ The raw PCI path of this Audio controller (if available.) """
        return self.pci

    @property
    def codec(self) -> str:
        """ The ALC codec of this Audio controller (if available.) """
        if (
            type(self.ven_id) != str or
            "10ec" not in self.ven_id.lower()
        ):
            return

        alc_codec = hex(int(self.ven_id, 16))[2:]

        return "ALC" + alc_codec