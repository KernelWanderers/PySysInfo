def test_input():
    from core.managers.input import InputManager
    from core.hardware.input import InputDevice

    inputs = InputManager().get_info()

    assert type(inputs) == list

    for input in inputs:
        assert type(input) == InputDevice
        assert type(input.model) == str
        assert type(input.protocol) == str
