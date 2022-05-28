def exec():
    from core.managers.x86cpu import X86CPUManager

    cpu = X86CPUManager().get_info()

    if not cpu:
        return
    else:
        cpu = cpu[0]

    print(
        ("=" * 25) + "\n" +
        "|\t   CPU   \t|" +
        "\n" + ("=" * 25) + "\n" +
        "\n".join([
            f"Model: {cpu.model}",
            f"Cores: {cpu.cores}",
            f"Threads: {cpu.threads}",
            f"Features: {cpu.features}",
            f"Vendor: {cpu.vendor}\n"
        ]) + "\n"
    )
