import listener
from faster_whisper import WhisperModel
import os

model_size = "small.en"
model = WhisperModel(model_size, device="cpu")


def audio_callback(file_name):
    segments, info = model.transcribe(file_name, beam_size=5, language="en")
    text = ""
    for segment in segments:
        text += segment.text

    print("text: " + text)
    os.remove(file_name)


listener.start(audio_callback)
