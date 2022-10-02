def test_gpu():
    from pysi.core.managers.gpu import GPUManager
    from pysi.core.hardware.gpu import GPU

    gpus = GPUManager().get_info()

    assert type(gpus) == list

    for gpu in gpus:
        assert type(gpu) == GPU
        assert type(gpu.model) == str
        assert type(gpu.dev_id) == str
        assert type(gpu.ven_id) == str
        assert type(gpu.vendor) == str or not gpu.vendor
        assert type(gpu.pci) == str or not gpu.pci
        assert type(gpu.acpi) == str or not gpu.acpi
        assert type(gpu.codename) == str or not gpu.codename
        assert type(gpu.cores) == int or not gpu.cores
        assert type(gpu.ne_cores) == int or not gpu.ne_cores
        assert type(gpu.generation) == int or not gpu.generation