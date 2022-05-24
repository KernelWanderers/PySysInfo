class InputDevice:
    def __init__(
        self,
        model: str,
        protocol: str
    ):
        self.model = model
        self.protocol = protocol

    @property
    def model(self) -> str:
        """ The model name of this input device. """
        return self.model

    @property
    def protocol(self) -> str:
        """ 
        The underlying protocol of this input device.

        E.g:
            - HID over I2C
            - SMBus
            - HID over USB
            ...        
        """
        return self.protocol