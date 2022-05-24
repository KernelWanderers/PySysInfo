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
        self.pci = pci,
        self.acpi = acpi,
        self.dev_id = dev_id
        self.ven_id = ven_id
        self.codename = codename
        self.vendor = vendor
        self.cores = cores
        self.ne_cores = ne_cores
        self.generation = generation

    @property
    def model(self) -> str:
        """ The (model) name of this GPU. """
        return self.model

    @property
    def pci(self) -> str:
        """ Returns the raw PCI path of this GPU. """
        return self.pci

    @property
    def acpi(self) -> str:
        """ Returns the raw ACPI path of this GPU. """
        return self.acpi

    @property
    def dev_id(self) -> str:
        """ Returns the Device ID of this GPU. """
        return self.dev_id

    @property
    def ven_id(self) -> str:
        """ Returns the Vendor ID of this GPU. """
        return self.ven_id

    @property
    def codename(self) -> str | None:
        """ 
        Returns the codename of this GPU (if available.)

        Restricted to x86_64/x86 iGFXs and dGPUs, 
        can't yet handle Apple ARM64 chips.

        Returns nothing if it's Apple ARM64.
        """
        if (
            type(self.vendor) == str or
            self.vendor.lower() != "apple"
        ):
            return

        return self.codename

    @property
    def vendor(self) -> str | None:
        """ Returns the (readable) vendor of this GPU (if available.) """
        return self.vendor

    @property
    def cores(self) -> int | None:
        """ 
        Returns the number of cores of this GPU device (if available.) 

        This property *ONLY* applies to Apple ARM64 iGFX.

        Returns nothing if it's not Apple ARM64.
        """
        if (
            type(self.vendor) == str and
            self.vendor.lower() != "apple"
        ):
            return

        return self.cores

    @property
    def ne_cores(self) -> int | None:
        """ 
        Returns the number of Neural Engine cores of this GPU device (if available.) 

        This property *ONLY* applies to Apple ARM64 iGFX.

        Returns nothing if it's not Apple ARM64.
        """
        if (
            type(self.vendor) == str and
            self.vendor.lower() != "apple"
        ):
            return

        return self.ne_cores

    @property
    def generation(self) -> int | None:
        """ 
        Returns the generation of this GPU device (if available.) 

        This property *ONLY* applies to Apple ARM64 iGFX.

        Returns nothing if it's not Apple ARM64.
        """
        if (
            type(self.vendor) == str and
            self.vendor.lower() != "apple"
        ):
            return

        return self.generation
