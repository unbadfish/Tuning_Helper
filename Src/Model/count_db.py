# -*- encoding: utf-8 -*-
"""
@FILE    count_db.py
@DATE    2021/02/14
@author  unbadfish @github&gitee
@usage   完成一些分贝值有关的计算
array->array
"""

# from icecream import ic
# import librosa
# import librosa.display
import numpy as np
# import matplotlib.pyplot as plt
# import Model


def max_db(S_db: np.ndarray) -> np.ndarray:
    """"""
    # https://numpy.org/devdocs/reference/generated/numpy.amax.html#numpy.amax
    return np.amax(S_db, axis=0)  # Max along the first axis


def sum_db(S_db: np.ndarray) -> np.ndarray:
    """"""
    # https://numpy.org/devdocs/reference/generated/numpy.sum.html#numpy.sum
    return np.sum(S_db, axis=0)  # Sum along the first axis
