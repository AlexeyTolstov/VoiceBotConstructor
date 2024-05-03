from VoiceBotConstructor.command_item import CommandItem
from VoiceBotConstructor.audio_player import AudioPlayer
from VoiceBotConstructor.listen_microphone import recognition_speech

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

        self.audio_player = AudioPlayer(vb_name=self.names,
                                        recognition_func=recognition_speech)

        self._commands = []
        self.configuration_file = configuration_file
        
        self.isSay = False
        self.s_time = None

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
    
    def recognize_phrase(self):
        text = ""
        while True:
            t_text = recognition_speech()
            
            if not t_text:
                return text
            text = t_text

    
    def execute_command(self):
        text = self.recognize_phrase()
        if text and any((name.lower() in text for name in set(self.names))):
            print(text)
            for item in set(self._commands):
                if any((phrase.lower() in text for phrase in set(item.phrases))):
                    if len(signature(item.func).parameters):
                        item.func(text)
                    else:
                        item.func()
                    
                    self.isSay = False
                    self.s_time = None
                    break
        else:
            if self.isSay:
                if (time.time() - self.s_time) > 3:
                    self.isSay = False
                    self.s_time = None
                    self.audio_player.unpause()
            
    def play_audio(self, file_name: str):
        self.audio_player.load(file_name)
        self.audio_player.play()

    def say(self, text: str, audio_filename: str="voice.mp3"):
        print(text.capitalize())
        self.isSay = self.audio_player.say(text, audio_filename)
        self.s_time = time.time()
    
    def update_config(self):
        with open(self.configuration_file, "w", encoding="utf-8") as file:
            json.dump(self.config, file)