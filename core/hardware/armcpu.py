class ARMCPU:
    """ CPU instance for ARM architectures. """
    def __init__(
        self,
        cores: int,
        model: str,
        threads: int,
        vendor: str | None = None,
        arm_t: str | None = None
    ):
        self.cores = cores
        self.model = model
        self.threads = threads
        self.vendor = vendor
        self.arm_t = arm_t

    @property
    def model(self) -> str:
        """ The (model) name of this CPU. """
        return self.model

    @property
    def cores(self) -> int:
        """ Number of physical cores for this CPU. """
        return self.cores

    @property
    def threads(self) -> int:
        """ Numbers of threads for this CPU. """
        return self.threads

    @property
    def vendor(self) -> str | None:
        """ The vendor of this CPU (if available.) """
        return self.vendor

    @property
    def arm_t(self) -> str | None:
        """ The ARM arch type (v8.x, v7.x, etc.) """
        return self.arm_t
