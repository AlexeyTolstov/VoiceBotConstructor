from vosk import Model, KaldiRecognizer
import os
import pyaudio

model = Model("./vosk-model-small-ru-0.22")
rec = KaldiRecognizer(model, 44100)
p = pyaudio.PyAudio()

stream = p.open(
    format=pyaudio.paInt16, 
    channels=1, 
    rate=44100, 
    input=True, 
    frames_per_buffer=16000
)

stream.start_stream()


def recognition_speech():
    data = stream.read(16000)
    if len(data): 
        return eval(rec.Result())["text"] if rec.AcceptWaveform(data) else eval(rec.PartialResult())["partial"]
if __name__ == "__main__":
    while True:
        print(recognition_speech())