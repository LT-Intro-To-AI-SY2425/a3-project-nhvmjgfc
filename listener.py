import sounddevice as sd
import numpy as np
from scipy.io import wavfile
from pynput import keyboard
import time

recording = []
is_recording = False
sample_rate = 48000
target_callback = None


def on_press(key):
    global is_recording, recording
    if key == keyboard.Key.space and not is_recording:
        is_recording = True
        recording = []


def on_release(key):
    global is_recording
    if key == keyboard.Key.space and is_recording:
        is_recording = False
        save_recording()


def save_recording():
    if len(recording) > 0:
        recording_array = np.concatenate(recording, axis=0)
        file_name = str(time.time_ns() // 1_000_000) + ".wav"

        wavfile.write(file_name, sample_rate, recording_array)

        if target_callback:
            target_callback(file_name)


def audio_callback(indata, frames, time, status):
    if is_recording:
        recording.append(indata.copy())


listener = keyboard.Listener(on_press=on_press, on_release=on_release)
listener.start()


def start(callback):
    global target_callback
    target_callback = callback
    try:
        with sd.InputStream(callback=audio_callback, channels=1, samplerate=sample_rate):
            print("Press the spacebar to start/stop recording. Use Ctrl+C to exit.")
            while True:
                time.sleep(0.1)
    except KeyboardInterrupt:
        print("\nProgram interrupted by user. Exiting...")
    finally:
        listener.stop()
        if is_recording:
            save_recording()
        print("Program ended.")
