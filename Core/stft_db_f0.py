# -*- encoding: utf-8 -*-
"""
@FILE    stft_db_f0.py
@DATE    2021/02/15
@author  unbadfish @github&gitee
@usage   在stft_db图上画出f0
"""

import librosa
# import librosa.display
import numpy as np
import matplotlib.pyplot as plt
import Model.draw_stft_themes

y, sr = librosa.load("Resource\\003796.wav")

S = librosa.stft(y)
S_db = librosa.amplitude_to_db(np.abs(S))
f0, _, _ = librosa.pyin(y, sr=sr,
    fmin=librosa.note_to_hz('C1'), fmax=librosa.note_to_hz('C8'))

fig, ax = plt.subplots()
# Model.draw_stft_themes.draw_dev_theme(fig, ax, sr, C_db, f0)
# Model.draw_stft_themes.draw_print_theme(fig, ax, sr, C_db, f0)
Model.draw_stft_themes.draw_tuning_theme(fig, ax, sr, S_db, f0)

plt.tight_layout()
plt.show()
