import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mpdates

def polyfit(dates, levels, p):
    dates = mpdates.date2num(dates)
    dates = np.array(dates)
    p_coeff = np.polyfit(dates - dates[-1], levels, p)
    poly = np.poly1d(p_coeff)
    return poly, dates[-1]

def current_gradient(poly,latest_date):
    return poly.deriv()(latest_date)

