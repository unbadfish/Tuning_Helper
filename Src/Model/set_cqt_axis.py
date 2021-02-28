# -*- encoding: utf-8 -*-
"""
@FILE    set_cqt_axis.py
@DATE    2021/02/14
@author  unbadfish @github&gitee
@usage   给纵坐标是cqt_note的图绘制更好的y轴
"""

# from icecream import ic
import librosa
# import librosa.display
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import LogLocator, FixedLocator
from matplotlib.ticker import FuncFormatter


def set_axis(ax) -> None:
    """要在draw_theme之后调用!!
    =========================
    Args:
        ax : Axes
    Returns:
        None
    """

    def _major_fomatter(x, pos):
        """Fomatter for major ticks"""
        # print('MAJOR  ' + str(x) + '  ' + str(librosa.hz_to_note(x, octave=True, cents=True)))
        if x <= 0:
            return ""
        else:
            # necessary for cents
            return librosa.hz_to_note(x, octave=True, cents=True)
            # return librosa.hz_to_note(x, octave=True, cents=False)

    def _minor_fomatter(x, pos):
        """Fomatter for minor ticks"""
        # print('MINOR  ' + str(x) + '  ' + str(librosa.hz_to_note(x, octave=True, cents=True)))
        if x <= 0:
            return ""
        vmin, vmax = ax.yaxis.get_view_interval()
        if vmax > 4 * max(1, vmin):
            return ""
        # return '*' + librosa.hz_to_note(x, octave=True, cents=True)  # debug
        return librosa.hz_to_note(x, octave=True, cents=False)
    """=Set Locator & Fomatter="""
    # log_C1 = np.log2(librosa.note_to_hz("C1"));
    # offset = 2.0 ** (log_C1 - np.floor(log_C1))
    offset = librosa.note_to_hz("C1") / 32
    ax.yaxis.set_major_locator(LogLocator(base=2.0, subs=(offset,)))
    ax.yaxis.set_minor_locator(
        # FixedLocator(librosa.cqt_frequencies(
        #     85, fmin=librosa.note_to_hz('C1')))
        LogLocator(base=2.0, subs=offset * (2.0 ** (np.arange(1, 12) / 12)))
    )
    ax.yaxis.set_major_formatter(_major_fomatter)
    ax.yaxis.set_minor_formatter(_minor_fomatter)
    return None
