class X86CPU:
    """ CPU instance for x86_64/x86 architectures. """

    def __init__(
        self,
        cores: int,
        model: str,
        threads: int,
        vendor: str | None = None,
        sse: str | None = None,
        ssse3: bool | None = None,
        codename: str | None = None
    ):
        self.codename = codename
        self.model = model
        self.cores = cores
        self.threads = threads
        self.sse = sse
        self.ssse3 = ssse3
        self.vendor = vendor

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
    def sse(self) -> str | None:
        """ Highest SSE version supported (if available.) """
        return self.sse

    @property
    def ssse3(self) -> bool | None:
        """ Whether or not SSSE3 is supported (if available.) """
        return self.ssse3

    @property
    def codename(self) -> str | None:
        """ The codename of this CPU (if available.) """
        return self.codename

    @property
    def vendor(self) -> str | None:
        """ The vendor of this CPU (if available.) """
        return self.vendor
