import string
import listener
from faster_whisper import WhisperModel
import os
import chatbot

model_size = "small.en"
model = WhisperModel(model_size, device="cpu", num_workers=os.cpu_count())


def audio_callback(file_name):
    segments, info = model.transcribe(
        file_name, beam_size=5, language="en", vad_filter=True)

    text = ""
    for segment in segments:
        text += segment.text

    text.translate(str.maketrans('', '', string.punctuation))
    text = text.lower()
    print(text)
    os.remove(file_name)

    if text == "bye":
        print("BYEBYE!!")
        exit()

    chatbot.query(text)


listener.start(audio_callback)
