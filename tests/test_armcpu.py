def test_armcpu():
    from core.managers.armcpu import ARMCPUManager

    cpus = ARMCPUManager().get_info()

    assert type(cpus) == list

    for cpu in cpus:
        assert type(cpu.cores) == int
        assert type(cpu.threads) == int
        assert type(cpu.model) == str
        assert type(cpu.vendor) == str or not cpu.vendor
        assert type(cpu.arm_t) == str or not cpu.arm_t
        assert type(cpu.codename) == str or not cpu.codename 