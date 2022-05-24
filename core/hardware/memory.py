class RAMSlot:
    def __init__(
        self,
        bank: str,
        channel: str
    ):
        self.bank = bank
        self.channel = channel

    @property
    def bank(self) -> str:
        """ Returns the bank location of this memory module. """
        return self.bank

    @property
    def channel(self) -> str:
        """ Returns the channel location of this memory module. """
        return self.channel

class RAM:
    def __init__(
        self,
        part_no: str,
        ram_type: str,
        slot: RAMSlot,
        frequency: int,
        manufacturer: str,
        capacity: int
    ):
        self.part_no = part_no
        self.ram_type = ram_type
        self.slot = slot
        self.frequency = frequency
        self.manufacturer = manufacturer
        self.capacity = capacity

    @property
    def part_no(self) -> str:
        """ Returns the Part-Number of this memory module. """
        return self.part_no

    @property
    def ram_type(self) -> str:
        """ Returns the RAM type of this module. """
        return self.ram_type

    @property
    def slot(self) -> RAMSlot:
        """ Returns details about this memory module's slot location. """
        return self.slot

    @property
    def frequency(self) -> int:
        """ Returns the frequency of this memory module represented in Hz. """
        return self.frequency

    @property
    def manufacturer(self) -> str:
        """ Returns the manufacturer of this memory module. """
        return self.manufacturer

    @property
    def capacity(self) -> str:
        """ Returns the capacity of this memory module represented in bytes. """
        return self.capacity