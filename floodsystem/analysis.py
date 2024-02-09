import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mpdates

def polyfit(dates, levels, p):
    dates = mpdates.date2num(dates)
    p_coeff = np.polyfit(dates - dates[0], levels, p)
    poly = np.poly1d(p_coeff)
    return poly