# -*- coding: UTF-8 -*-
# 画出stft得到的分贝数图像
import numpy as np
import matplotlib.pyplot as plt
import librosa
import librosa.display

y, sr = librosa.load("music\\003796.wav", sr=None)
D = librosa.stft(y)  # STFT of y
S_db = librosa.amplitude_to_db(np.abs(D), ref=np.max)
fig, ax = plt.subplots()
img = librosa.display.specshow(S_db, sr=sr, x_axis='time', y_axis='log', ax=ax, cmap='gray_r')
fig.colorbar(img, ax=ax, format='%+2.0f dB')
ax.set(title='STFT - Time')
plt.show()
