# -*- encoding: utf-8 -*-
"""
@FILE    cqt_db_f0.py
@DATE    2021/02/13
@author  unbadfish @github&gitee
@usage   在cqt_db图上画出f0
"""

import librosa
# import librosa.display
import numpy as np
import matplotlib.pyplot as plt
import Model.draw_cqt_themes

y, sr = librosa.load("Resource\\003796.wav")

C = librosa.cqt(y=y, sr=sr)
C_db = librosa.amplitude_to_db(np.abs(C))
f0, _, _ = librosa.pyin(y, sr=sr, 
    fmin=librosa.note_to_hz('C1'), fmax=librosa.note_to_hz('C8'))

fig, ax = plt.subplots()
# Model.draw_cqt_themes.draw_dev_theme(fig, ax, sr, C_db, f0)
# Model.draw_cqt_themes.draw_print_theme(fig, ax, sr, C_db, f0)
Model.draw_cqt_themes.draw_tuning_theme(fig, ax, sr, C_db, f0)
Model.set_cqt_axis.set_axis(ax)
plt.tight_layout()
plt.show()
