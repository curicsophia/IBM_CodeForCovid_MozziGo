# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 13:09:30 2020

@author: Anjali
"""

import sounddevice as sd
from scipy.io.wavfile import write
import time
fs = 44100  # Sample rate
seconds = 8 # Duration of recording

print('Start !')
time.sleep(0.5)
myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
sd.wait()  # Wait until recording is finished
print('Stop')
write('output.wav', fs, myrecording)  # Save as WAV file 