def exec():
    from core.managers.input import InputManager

    inputs = InputManager().get_info()

    print(
        ("=" * 25) + "\n" +
        "|\t  INPUT  \t|" +
        "\n" + ("=" * 25)
    )

    for input in inputs:
        print(
            "\n".join([
                f"Model: {input.model}",
                f"Protocol: {input.protocol}\n"
            ]) + "\n"
        )
