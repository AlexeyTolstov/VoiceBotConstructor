from VoiceBotConstructor.command_item import CommandItem

import speech_recognition as sr
from playsound import playsound
from gtts import gTTS
from os import remove


class Bot():
    def __init__(self, name):
        if isinstance(name, str):
            self.names = [name]
        elif isinstance(name, (list, set, tuple)):
            self.names = name
        else:
            raise TypeError("ERROR: variable `name` must be str or list")
        
        self._commands = []

    def check_command(self, phrases: list, name_cmd: str):
        def decorator(func):
            cmd_item = CommandItem(name=name_cmd,
                                   phrases=phrases,
                                   func=func)
            self._commands.append(cmd_item)
        return decorator
    
    def start(self):
        while True:
            self.recognize_speech()

    
    def recognize_speech(self):
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio, language="ru-RU").lower()
            
            if text:
                print(text)
            
            self.execute_command(text)
        except Exception as ex:
            print(ex)
    
    def execute_command(self, text):
        for name in self.names:
            if not name.lower() in text:
                continue
            for item in self._commands:
                for phrase in item.phrases:
                    if phrase.lower() in text:
                        item.func()

    def say(self, text: str):
        print(text)
        tts = gTTS(text=text, lang='ru')
        tts.save("temp_audio.mp3")
        playsound("temp_audio.mp3")
        remove("temp_audio.mp3")