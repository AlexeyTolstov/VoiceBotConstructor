import os
import webbrowser


class Program:
    def __init__(self, name: str, path: str, phrases: list):
        self.name = name
        self.path = path
        self.phrases = phrases
        
    def open(self):
        os.system(self.path)
    

class Website:
    def __init__(self, name: str, url: str, phrases: list):
        self.name = name
        self.url = url
        self.phrases = phrases
        
    def open(self):
        webbrowser.open_new_tab(self.url)

if __name__ == "__main__":
    Website("GitHub", "https://github.com/AlexeyTolstov", []).open()
    Program("Android Studio", '"C:/Program Files/Android/Android Studio/bin/studio64.exe"', []).open()