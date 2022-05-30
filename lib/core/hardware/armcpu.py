class ARMCPU:
    """ CPU instance for ARM architectures. """
    def __init__(
        self,
        cores: int,
        model: str,
        threads: int,
        vendor: str | None = None,
        arm_t: str | None = None,
        codename: str | None = None,
    ):
        self.cores = cores
        """ Number of physical cores for this CPU. """

        self.model = model
        """ The (model) name of this CPU. """

        self.threads = threads
        """ Number of threads for this CPU. """

        self.vendor = vendor
        """ The vendor of this CPU (if available.) """

        self.arm_t = arm_t
        """ The ARM arch type (v8.x, v7.x, etc.) """

        self.codename = codename
        """ The codename of this CPU (if available.) """