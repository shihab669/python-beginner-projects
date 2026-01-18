# We need to install some modules for this project
# pip install sounddevice
# pip install wavio

import sounddevice as soud
import wavio as wav

freq = 44100

duration = 5

recording = soud.rec(int(freq * duration),
                     samplerate=freq, channels=2)
soud.wait()

wav.write("recording1.wav", recording, freq, sampwidth=3)