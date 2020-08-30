# -*- coding: UTF-8 -*-
# 传入两个音乐,第一个是完整曲子,第二个是伴奏
# 用y = y1 - y2 来完成骚操作
# sr建议就用sr=22050
# 我放弃了,效果真的不好,求大佬指点
"""
import numpy as np
import matplotlib.pyplot as plt
import librosa
import librosa.display

sr = 22050
offset = 40.0
duration = 15.0
y1 = librosa.load("music\\y1.flac", sr=sr, offset=offset, duration=duration)[0]
y2 = librosa.load("music\\y3.mp3", sr=sr, offset=offset, duration=duration)[0]
# print(np.array(y1).shape)
# print(np.array(y2).shape)
# y, sr = librosa.load("music\\election_music.wav", sr=None)
y = y1 - y2
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
"""