# -*- coding: UTF-8 -*-
# 画出每一帧的最大分贝数
import numpy as np
import matplotlib.pyplot as plt
import librosa
import librosa.display
import an_al

y, sr = librosa.load("music\\003796.wav", sr=None)
D = librosa.amplitude_to_db(np.abs(librosa.stft(y)), ref=np.max)
db_max = an_al.anal_db(D, 0)
times = librosa.times_like(D, sr=sr)
fig, ax = plt.subplots(1, 1)
ax.plot(times, db_max, label='db_max', color='r', linewidth=2)
ax.legend(loc='upper right')
ax.set_xlabel('Time (s)')
ax.set_ylabel('db_max')
ax.grid(color='black', linestyle='--', alpha=0.2, linewidth=1)
ax.set(title='db_max - Time')
plt.show()
