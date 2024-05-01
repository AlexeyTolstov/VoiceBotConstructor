class CommandItem:
    def __init__(self, name: str,
                    phrases: list,
                    func):
        self.name = name
        self.phrases = phrases
        self.func = func
    
    def __str__(self) -> str:
        return "Name command: {} \nPhrases: {}".format(self.name, self.phrases)