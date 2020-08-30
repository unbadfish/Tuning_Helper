# -*- coding: UTF-8 -*-
# 画出stft图
import numpy as np
import matplotlib.pyplot as plt
import librosa
import librosa.display

y, sr = librosa.load("music\\003796.wav", sr=None)
f0, voiced_flag, voiced_probs = librosa.pyin(y, sr=sr, fmin=librosa.note_to_hz('C1'), fmax=librosa.note_to_hz('C8'))
D = librosa.amplitude_to_db(np.abs(librosa.stft(y)), ref=np.max)
times = librosa.times_like(D, sr=sr)
fig, ax = plt.subplots()
img = librosa.display.specshow(D, sr=sr, x_axis='time', y_axis='log', ax=ax, cmap='gray_r')
fig.colorbar(img, ax=ax, format="%+2.f dB")
ax.plot(times, f0, label='f0', color='cyan', linewidth=3)
ax.legend(loc='upper right')
ax.set(title='STFT - Time & f0')
plt.show()
