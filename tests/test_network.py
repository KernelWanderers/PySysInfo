def test_network():
    from core.managers.network import NetworkManager
    from core.hardware.network import NetworkController

    nics = NetworkManager().get_info()

    assert type(nics) == list

    for nic in nics:
        assert type(nic) == NetworkController
        assert type(nic.model) == str
        assert type(nic.pci) == str
        assert type(nic.acpi) == str
        assert type(nic.dev_id) == str
        assert type(nic.ven_id) == str

