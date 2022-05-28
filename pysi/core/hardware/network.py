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
        """ The (model) name of this network controller. """

        self.dev_id = dev_id
        """ The Device ID of this network controller. """
        
        self.ven_id = ven_id
        """ The Vendor ID of this network controller. """
        
        self.pci = pci
        """ The PCI path of this network controller. """
        
        self.acpi = acpi
        """ The ACPI path of this network controller. """
