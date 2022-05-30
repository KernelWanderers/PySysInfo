class GPU:
    def __init__(
        self,
        model: str,
        dev_id: str,
        ven_id: str,
        pci: str | None = None,
        acpi: str | None = None,
        codename: str | None = None,
        vendor: str | None = None,
        # ==========================================
        # AGX (Apple ARM64 iGFX) specific properties
        #
        #   - Cores
        #   - Neural Engine (NE) Cores
        #   - Generation
        # ==========================================
        cores: int | None = None,
        ne_cores: int | None = None,
        generation: int | None = None
    ):
        self.model = model
        """ The (model) name of this GPU. """

        self.pci = pci
        """ The PCI path of this GPU. """

        self.acpi = acpi
        """ The ACPI path of this GPU. """

        self.dev_id = dev_id
        """ The Device ID of this GPU. """

        self.ven_id = ven_id
        """ The Vendor ID of this GPU. """

        self.codename = codename
        """ The codename of this GPU (if available.) """

        self.vendor = vendor
        """ The (readable) vendor of this GPU (if available.) """

        self.cores = (
            cores
            if type(self.vendor) == str and
            self.vendor.lower() == "apple"
            else None
        )
        """ 
        The number of cores of this GPU device (if available.) 

        This property *ONLY* applies to Apple ARM64 iGFX.

        Returns nothing if it's not Apple ARM64.
        """

        self.ne_cores = (
            ne_cores
            if type(self.vendor) == str and
            self.vendor.lower() == "apple"
            else None
        )
        """ 
        The number of Neural Engine cores of this GPU device (if available.) 

        This property *ONLY* applies to Apple ARM64 iGFX.

        Returns nothing if it's not Apple ARM64.
        """

        self.generation = (
            generation
            if type(self.vendor) == str and
            self.vendor.lower() == "apple"
            else None
        )
        """ 
        The generation of this GPU device (if available.) 

        This property *ONLY* applies to Apple ARM64 iGFX.

        Returns nothing if it's not Apple ARM64.
        """
