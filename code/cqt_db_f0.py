# -*- coding: UTF-8 -*-
# 在cqt图上画出f0
# -----------
# |IMPORTANT|
# -----------
import numpy as np
import matplotlib.pyplot as plt
import librosa
import librosa.display

y, sr = librosa.load("music\\003796.wav", sr=None)
f0, voiced_flag, voiced_probs = librosa.pyin(y, sr=sr, fmin=librosa.note_to_hz('C1'), fmax=librosa.note_to_hz('C8'))
times = librosa.times_like(f0, sr=sr)
C = librosa.cqt(y=y, sr=sr)
C_db = librosa.amplitude_to_db(np.abs(C), ref=np.max)
fig, ax = plt.subplots()
img = librosa.display.specshow(C_db, sr=sr, x_axis='time', y_axis='cqt_note', ax=ax, cmap='gray_r')
fig.colorbar(img, ax=ax, format="%+2.f dB")
ax.plot(times, f0, label='f0', color='cyan', linewidth=2)
ax.legend(loc='upper right')
ax.set(title='CQT - Time & f0')
plt.show()
