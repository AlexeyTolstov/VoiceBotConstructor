from VoiceBotConstructor.command_item import CommandItem
from VoiceBotConstructor.audio_player import AudioPlayer

import speech_recognition as sr

import json
from os import remove, path
from inspect import signature


class Bot():
    def __init__(self, name,
                configuration_file="config.json"):
        if isinstance(name, str):
            self.names = [name]
        elif isinstance(name, (list, set, tuple)):
            self.names = name
        else:
            raise TypeError("ERROR: variable `name` must be str or list")

        self.audio_player = AudioPlayer(recog_func=self.recognize_speech)

        self._commands = []
        self.configuration_file = configuration_file
        
        if not path.isfile(configuration_file):
            self.config = {
                "user_name": None,
                "voice_bot_name": self.names,
                "todo_list": [],
                "alarms": []
            }

            with open("config.json", "w") as file:
                json.dump(self.config, file)
        
        with open("config.json", "r") as file:
            self.config = json.load(file)

    def check_command(self, phrases: list, name_cmd: str):
        def decorator(func):
            cmd_item = CommandItem(name=name_cmd,
                                   phrases=phrases,
                                   func=func)
            self._commands.append(cmd_item)
        return decorator


    def add_command(self, phrases: list, name_cmd: str, func):
        cmd_item = CommandItem(name=name_cmd,
                                phrases=phrases,
                                func=func)
        self._commands.append(cmd_item)


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
                        self.isPlaying = False
                        if len(signature(item.func).parameters):
                            item.func(text)
                        else:
                            item.func()
                        break
                else:
                    continue
                break
            break
    
    def say(self, text: str, audio_filename: str="voice.mp3"):
        print(text.capitalize())
        self.audio_player.say(text, audio_filename)