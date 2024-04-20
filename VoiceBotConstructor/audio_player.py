import pygame.mixer as mxr
from gtts import gTTS
from os import remove
from enum import Enum


class AudioPlayerStates(Enum):
    PLAY = 1
    STOP = 2
    PAUSE = 3


class AudioPlayer:
    def __init__(self, recog_func):
        mxr.init()
        self.state = AudioPlayerStates.STOP  
        self.current_file = None
        self.recog_func = recog_func

    def load(self, file_name: str):
        mxr.music.load(file_name)
        self.state = AudioPlayerStates.PLAY
        self.current_file = file_name

    def play(self):
        if self.state == AudioPlayerStates.PLAY:
            mxr.music.play()

            while mxr.music.get_busy():
                self.recog_func()
            
            mxr.music.unload()
            if self.current_file:
                remove(self.current_file)
            self.state = AudioPlayerStates.STOP

    def unpause(self):
        self.state = AudioPlayerStates.PLAY
        mxr.music.unpause()

    def pause(self):
        self.state = AudioPlayerStates.PAUSE
        mxr.music.pause()

    def set_volume(self, value: float):
        mxr.music.set_volume(value)

    def stop(self):
        mxr.music.stop()
        mxr.music.unload()

        if self.current_file:
            remove(self.current_file)

    def say(self, text: str, audio_filename: str="voice.mp3"):
        tts = gTTS(text=text, lang='ru')
        tts.save(audio_filename)
        self.load(audio_filename)
        self.play()