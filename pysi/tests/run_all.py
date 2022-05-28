from tests import x86cpu, baseboard, gpu, input, memory, network, audio, storage

def exec():
    x86cpu.exec()
    baseboard.exec()
    gpu.exec()
    input.exec()
    memory.exec()
    network.exec()
    audio.exec()
    storage.exec()