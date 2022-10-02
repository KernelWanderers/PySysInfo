def test_input():
    from pysi.core.managers.input import InputManager
    from pysi.core.hardware.input import InputDevice

    inputs = InputManager().get_info()

    assert type(inputs) == list

    for input in inputs:
        assert type(input) == InputDevice
        assert type(input.model) == str
        # Assertion to account for missing
        # `InputDevice#protocol` property on
        # the Windows VENV in Github Actions;
        # This should not happen on regular machines.
        assert type(input.protocol) == str or not input.protocol
