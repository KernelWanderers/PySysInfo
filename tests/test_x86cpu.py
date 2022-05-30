def test_x86cpu():
    from core.managers.x86cpu import X86CPUManager
    from core.hardware.x86cpu import X86CPU

    cpus = X86CPUManager().get_info()
    cpu = cpus[0]

    assert type(cpus) == list
    assert type(cpu) == X86CPU
    assert type(cpu.model) == str
    assert type(cpu.cores) == int
    assert type(cpu.threads) == int
    assert type(cpu.features) == list
    assert type(cpu.vendor) == str or not cpu.vendor
    assert type(cpu.codename) == str or not cpu.codename