class X86CPU:
    """ CPU instance for x86_64/x86 architectures. """

    def __init__(
        self,
        cores: int,
        model: str,
        threads: int,
        features: list[str],
        vendor: str | None = None,
        codename: str | None = None
    ):
        self.codename = codename
        """ The codename of this CPU (if available.) """

        self.model = model
        """ The (model) name of this CPU. """
        
        self.cores = cores
        """ Number of physical cores for this CPU. """

        self.threads = threads
        """ Numbers of threads for this CPU. """

        self.features = features
        """ List of instruction sets supported. """

        self.vendor = vendor
        """ The vendor of this CPU (if available.) """