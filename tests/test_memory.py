def test_memory():
    from pysi.core.managers.memory import RAMManager
    from pysi.core.hardware.memory import RAM, RAMSlot

    rams = RAMManager().get_info()

    assert type(rams) == list

    for ram in rams:
        assert type(ram) == RAM
        assert type(ram.part_no) == str
        assert type(ram.slot) == RAMSlot
        assert type(ram.capacity) == int
        assert type(ram.frequency) == int
        assert type(ram.ram_type) == str
        assert type(ram.manufacturer) == str
