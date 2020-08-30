# -*- coding: UTF-8 -*-
# 画出波形的包络线
import numpy as np
import matplotlib.pyplot as plt
import librosa
import librosa.display

y, sr = librosa.load("music\\003796.wav", sr=None)
fig, ax = plt.subplots()
librosa.display.waveplot(y, sr=sr, ax=ax)
ax.set(title='Envelope of Waveform')
plt.show()
