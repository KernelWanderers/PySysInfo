class RAMSlot:
    def __init__(
        self,
        bank: str,
        channel: str
    ):
        self.bank = bank
        """ The bank location of this memory module. """

        self.channel = channel
        """ The channel location of this memory module. """

class RAM:
    def __init__(
        self,
        part_no: str,
        ram_type: str,
        slot: RAMSlot,
        frequency: int,
        manufacturer: str,
        capacity: int,
    ):
        self.part_no = part_no
        """ The Part-Number of this memory module. """

        self.ram_type = ram_type
        """ The RAM type of this module. """

        self.slot = slot
        """ Details about this memory module's slot location. """

        self.frequency = frequency
        """ The frequency of this memory module represented in Hz. """

        self.manufacturer = manufacturer
        """ The manufacturer of this memory module. """

        self.capacity = capacity
        """ The capacity of this memory module represented in bytes. """