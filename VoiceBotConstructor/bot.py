from VoiceBotConstructor.command_item import CommandItem
from VoiceBotConstructor.audio_player import AudioPlayer

import speech_recognition as sr

import json
from os import remove, path
from inspect import signature
import time

class Bot():
    def __init__(self, name,
                configuration_file="config.json"):
        if isinstance(name, str):
            self.names = [name]
        elif isinstance(name, (list, set, tuple)):
            self.names = name
        else:
            raise TypeError("ERROR: variable `name` must be str or list")

        self.audio_player = AudioPlayer(recog_func=self.execute_command)

        self._commands = []
        self.configuration_file = configuration_file
        
        if not path.isfile(configuration_file):
            self.config = {
                "user_name": None,
                "voice_bot_name": self.names,
                "todo_list": [],
                "alarms": []
            }

            with open(self.configuration_file, "w", encoding="utf-8") as file:
                json.dump(self.config, file)
        
        with open(self.configuration_file, "r", encoding="utf-8") as file:
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
        print("Bot started succesfull")
        while True:
            self.execute_command()

    def recognize_speech(self):
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            recognizer.pause_threshold = 0.5
            recognizer.adjust_for_ambient_noise(source, duration=0.3)
             
            audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio, language="ru-RU").lower()
            if text:
                print(text)
                return text 
        except Exception as ex:
            print(ex)
    
    def execute_command(self):
        text = self.recognize_speech()
        if text:
            if any((name.lower() in text for name in set(self.names))):
                for item in set(self._commands):
                    if any((phrase.lower() in text for phrase in set(item.phrases))):
                        if len(signature(item.func).parameters):
                            item.func(text)
                        else:
                            item.func()
                        break
            
    
    def say(self, text: str, audio_filename: str="voice.mp3"):
        print(text.capitalize())
        self.audio_player.say(text, audio_filename)
    
    def update_config(self):
        with open(self.configuration_file, "w", encoding="utf-8") as file:
            json.dump(self.config, file)