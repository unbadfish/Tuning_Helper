# -*- coding: UTF-8 -*-
# 画出cqt图
import numpy as np
import matplotlib.pyplot as plt
import librosa
import librosa.display

y, sr = librosa.load("music\\003796.wav", sr=None)
C = librosa.cqt(y=y, sr=sr)
C_db = librosa.amplitude_to_db(np.abs(C), ref=np.max)
fig, ax = plt.subplots()
img = librosa.display.specshow(C_db, sr=sr, y_axis='cqt_note', x_axis='time', ax=ax, cmap='gray_r')
fig.colorbar(img, ax=ax, format='%+2.0f dB')
ax.set(title='CQT - Time')
plt.show()
