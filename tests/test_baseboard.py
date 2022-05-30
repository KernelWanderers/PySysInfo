def test_baseboard():
    from core.managers.baseboard import BaseboardManager
    from core.hardware.baseboard import Baseboard

    mobo = BaseboardManager().baseboard_info()

    assert type(mobo) == Baseboard
    assert type(mobo.model) == str
    assert type(mobo.manufacturer) == str
