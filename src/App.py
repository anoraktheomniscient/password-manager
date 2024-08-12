try:
    from json import load
except:
    raise ImportError("Import of modules failed")

class App:
    def __init__(self, inputFile) -> None:
        self.inputFile = inputFile