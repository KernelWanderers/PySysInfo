class InputDevice:
    def __init__(
        self,
        model: str,
        protocol: str
    ):
        self.model = model
        """ The model name of this input device. """

        self.protocol = protocol
        """ 
        The underlying protocol of this input device.

        E.g:
            - HID over I2C
            - SMBus
            - HID over USB
            ...        
        """