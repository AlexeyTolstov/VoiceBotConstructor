import pygame.mixer as mxr
from gtts import gTTS
from os import remove
from os.path import exists
from enum import Enum

from re import findall
from VoiceBotConstructor.num2word import num2word


class AudioPlayerStates(Enum):
    PLAY = 1
    STOP = 2
    PAUSE = 3


class AudioPlayer:
    def __init__(self, recognition_func, vb_name: list):
        mxr.init()
        self.state = AudioPlayerStates.STOP  
        self.current_file = None
        self.recognition_func = recognition_func
        self.names = vb_name
        self.current_value = 0.5

    def load(self, file_name: str):
        mxr.music.load(file_name)
        self.state = AudioPlayerStates.PLAY
        self.current_file = file_name

    def turn_up(self):
        self.current_value += 0.1
        self.set_volume()
    
    def turn_down(self):
        self.current_value -= 0.1
        self.set_volume()

    def play(self) -> bool:
        mxr.music.play()

        while mxr.music.get_busy():
            text = self.recognition_func()
            if any((name.lower() in text for name in set(self.names))):
                self.pause()
                return True
            
        mxr.music.unload()

        if self.current_file and exists(self.current_file):
            remove(self.current_file)
        self.state = AudioPlayerStates.STOP
        return False

    def unpause(self):
        self.state = AudioPlayerStates.PLAY
        mxr.music.unpause()

    def pause(self):
        self.state = AudioPlayerStates.PAUSE
        mxr.music.pause()

    def set_volume(self):
        self.current_value = min(max(0, self.current_value), 1)
        mxr.music.set_volume(self.current_value)

    def stop(self):
        mxr.music.stop()
        mxr.music.unload()

        if self.current_file:
            remove(self.current_file)

    def say(self, text: str, audio_filename: str="voice.mp3"):
        if self.state == AudioPlayerStates.PLAY or self.state == AudioPlayerStates.PAUSE:
            self.stop()
        
        for n in set(findall(r'\d+', text)):
            text = text.replace(n, num2word(int(n)))

        tts = gTTS(text=text, lang='ru')

        if exists(audio_filename):
            remove(audio_filename)
        
        tts.save(audio_filename)
        self.load(audio_filename)
        return self.play()