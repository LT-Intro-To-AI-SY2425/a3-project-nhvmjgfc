import listener
from faster_whisper import WhisperModel
import os
import chatbot

model_size = "small.en"
model = WhisperModel(model_size, device="cpu", num_workers=os.cpu_count())


def audio_callback(file_name):
    segments, info = model.transcribe(
        file_name, beam_size=5, language="en", vad_filter=True)
    os.remove(file_name)

    text = ""
    for segment in segments:
        text += segment.text

    print("What you said: " + text)

    text = text.lower().strip()[:-1]

    if text == "bye":
        print("BYEBYE!!")
        raise KeyboardInterrupt

    text = text.split()

    chatbot.query(text)


listener.start(audio_callback)
