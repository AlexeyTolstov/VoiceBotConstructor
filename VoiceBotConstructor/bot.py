from VoiceBotConstructor.command_item import CommandItem

import pygame
from gtts import gTTS
import speech_recognition as sr

from os import remove
from threading import Thread

class Bot():
    def __init__(self, name):
        pygame.mixer.init()

        if isinstance(name, str):
            self.names = [name]
        elif isinstance(name, (list, set, tuple)):
            self.names = name
        else:
            raise TypeError("ERROR: variable `name` must be str or list")
        
        self._commands = []

        self.isPlaying = False
        self.audio_filename = None

    def check_command(self, phrases: list, name_cmd: str):
        def decorator(func):
            cmd_item = CommandItem(name=name_cmd,
                                   phrases=phrases,
                                   func=func)
            self._commands.append(cmd_item)
        return decorator

    def start(self):
        self.recognition_thread_ = Thread(target=self.recognition_thread)
        self.sound_thread_ = Thread(target=self.sound_thread)

        self.recognition_thread_.start()
        self.sound_thread_.start()

        self.recognition_thread_.join()
        self.sound_thread_.join()

    def recognition_thread(self):
        while True:
            self.recognize_speech()
    
    def sound_thread(self):
        while True:
            if self.isPlaying:
                pygame.mixer.music.load(self.audio_filename)
                pygame.mixer.music.play()
                while pygame.mixer.music.get_busy():
                    pygame.time.Clock().tick(10)
                pygame.mixer.music.unload()
                remove(self.audio_filename)
                self.isPlaying = False
    
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
                        item.func()
                        break

    def say(self, text: str):
        self.audio_filename = "temp_audio.mp3"

        tts = gTTS(text=text, lang='ru')
        tts.save(self.audio_filename)
        self.isPlaying = True
