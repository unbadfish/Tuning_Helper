# -*- coding: UTF-8 -*-
# name::an_al.py
import numpy as np


def anal_db(arr: np.ndarray, add_db: float = 80):
    width = arr.shape[1]
    height = arr.shape[0]
    out_list = []
    for y in range(width):
        db_list = []
        for x in range(height):
            db_list.append(arr[x][y] + add_db)
        out_list.append(max(db_list))
    # print(np.array(out_list).shape)
    return out_list
