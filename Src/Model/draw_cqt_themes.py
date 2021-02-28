# -*- encoding: utf-8 -*-
"""
@FILE    draw_cqt_themes.py
@DATE    2021/02/14
@author  unbadfish @github&gitee
@usage   对不同的使用场景绘制不同"主题"的cqt-f0图
"""

# from icecream import ic
# import librosa
import librosa.display
import numpy as np
import matplotlib.pyplot as plt


def draw_dev_theme(fig, ax, sr: int, C_db: np.ndarray, f0: np.ndarray) -> None:
    """在ax上绘出cqt_db, f0的数据. 供开发时使用
    Args:
        fig : Figure
        ax : Axes
        sr (int): 采样率
        C_db (np.ndarray): cqt_db数据
        f0 (np.ndarray): f0
    Returns:
        None
    """
    img = librosa.display.specshow(
        C_db, sr=sr, x_axis='s', y_axis='cqt_note', ax=ax, cmap='magma')
    times = librosa.times_like(f0, sr=sr)
    ax.plot(times, f0, label='f0', color='lime', linewidth=2)  # %
    fig.colorbar(img, ax=ax, format="%+2.f dB")

    ax.tick_params(direction='out', which='both',
                   bottom=True, top=True, left=True, right=True,
                   labelbottom=True, labeltop=True, labelleft=True, labelright=True
                   )
    # ax.grid(color='black', linestyle='--', alpha=0.2, linewidth=1)
    ax.grid(axis='x', which='major',  # | | |
            color='black', alpha=0.5, linestyle='-', linewidth=1
            )
    ax.grid(axis='y', which='major',  # - - -
            color='black', alpha=0.5, linestyle='-', linewidth=1
            )
    ax.legend(loc='upper right')
    return None


def draw_print_theme(fig, ax, sr: int, C_db: np.ndarray, f0: np.ndarray) -> None:
    """在ax上绘出cqt_db, f0的数据. 供打印&分享
    Args:
        fig : Figure
        ax : Axes
        sr (int): 采样率
        C_db (np.ndarray): cqt_db数据
        f0 (np.ndarray): f0
    Returns:
        None
    """
    img = librosa.display.specshow(
        C_db, sr=sr, x_axis='s', y_axis='cqt_note', ax=ax, cmap='gray_r')
    times = librosa.times_like(f0, sr=sr)
    ax.plot(times, f0, label='f0', color='springgreen', linewidth=2)  # %
    fig.colorbar(img, ax=ax, format="%+2.f dB")

    ax.tick_params(direction='inout', which='both',
                   bottom=True, top=True, left=True, right=True,
                   #    labelbottom=True, labeltop=True, labelleft=True, labelright=True
                   )
    # ax.grid(color='black', linestyle='--', alpha=0.2, linewidth=1)
    ax.grid(axis='x', which='major',  # | | |
            color='steelblue', alpha=0.5, linestyle=(0, (5, 5)), linewidth=1.5
            )
    ax.grid(axis='y', which='major',  # - - -
            color='steelblue', alpha=0.5, linestyle='-', linewidth=1.5
            )
    ax.legend(loc='upper right')
    return None


def draw_tuning_theme(fig, ax, sr: int, C_db: np.ndarray, f0: np.ndarray) -> None:
    """在ax上绘出cqt_db, f0的数据. 供调校时使用
    Args:
        fig : Figure
        ax : Axes
        sr (int): 采样率
        C_db (np.ndarray): cqt_db数据
        f0 (np.ndarray): f0
    Returns:
        None
    """
    img = librosa.display.specshow(
        C_db, sr=sr, x_axis='s', y_axis='cqt_note', ax=ax, cmap='gray_r')
    times = librosa.times_like(f0, sr=sr)
    ax.plot(times, f0, label='f0', color='seagreen', linewidth=2)  # %
    fig.colorbar(img, ax=ax, format="%+2.f dB")

    ax.tick_params(direction='inout', which='both',
                   bottom=True, top=True, left=True, right=True,
                   #    labelbottom=True, labeltop=True, labelleft=True, labelright=True
                   )
    # ax.grid(color='black', linestyle='--', alpha=0.2, linewidth=1)
    ax.grid(axis='x', which='major',  # | | |
            color='steelblue', alpha=0.5, linestyle=(0, (5, 5)), linewidth=1.5
            )
    ax.grid(axis='y', which='major',  # - - -
            color='steelblue', alpha=0.5, linestyle='-', linewidth=1.5
            )
    ax.legend(loc='upper right')
    return None
