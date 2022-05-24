class NetworkController:
    def __init__(
        self,
        model: str,
        dev_id: str,
        ven_id: str,
        pci: str,
        acpi: str
    ):
        self.model = model
        self.dev_id = dev_id
        self.ven_id = ven_id
        self.pci = pci
        self.acpi = acpi

    @property
    def model(self) -> str:
        """ The (model) name of this network controller. """
        return self.model

    @property
    def dev_id(self) -> str:
        """ Returns the Device ID of this network controller. """
        return self.dev_id

    @property
    def ven_id(self) -> str:
        """ Returns the Vendor ID of this network controller. """
        return self.ven_id

    @property
    def pci(self) -> str:
        """ Returns the raw PCI path of this network controller. """
        return self.pci

    @property
    def acpi(self) -> str:
        """ Returns the raw ACPI path of this network controller. """
        return self.acpi
