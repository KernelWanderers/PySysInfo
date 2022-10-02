def test_baseboard():
    from pysi.core.managers.baseboard import BaseboardManager
    from pysi.core.hardware.baseboard import Baseboard

    mobo = BaseboardManager().baseboard_info()

    assert type(mobo) == Baseboard
    assert type(mobo.model) == str
    assert type(mobo.manufacturer) == str
