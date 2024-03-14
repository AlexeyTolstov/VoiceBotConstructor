class CommandItem:
    def __init__(self, name: str,
                    phrases: list,
                    func):
        self.name = name
        self.phrases = phrases
        self.func = func