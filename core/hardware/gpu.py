class GPU:
    def __init__(
        self,
        model: str,
        pci: str,
        acpi: str,
        dev_id: str,
        ven_id: str,
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
        """ The raw PCI path of this GPU. """

        self.acpi = acpi
        """ The raw ACPI path of this GPU. """

        self.dev_id = dev_id
        """ The Device ID of this GPU. """

        self.ven_id = ven_id
        """ The Vendor ID of this GPU. """

        self.vendor = vendor
        """ The (readable) vendor of this GPU (if available.) """

        self.codename = (
            codename
            if type(self.vendor) == str and
            self.vendor.lower() != "apple"
            else None
        )
        """ 
        The codename of this GPU (if available.)

        Restricted to x86_64/x86 iGFXs and dGPUs, 
        can't yet handle Apple ARM64 chips.

        Returns nothing if it's Apple ARM64.
        """

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
