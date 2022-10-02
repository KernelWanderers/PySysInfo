def test_audio():
    from pysi.core.managers.audio import AudioManager
    from pysi.core.hardware.audio import AudioController

    hdas = AudioManager().get_info()

    assert type(hdas) == list

    for hda in hdas:
        assert type(hda) == AudioController
        assert type(hda.dev_id) == str
        assert type(hda.ven_id) == str
        assert type(hda.model) == str or not hda.model
        assert type(hda.codec) == str or not hda.codec
