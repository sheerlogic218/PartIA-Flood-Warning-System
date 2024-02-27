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


def average_gradient(poly, days):
    return (poly(poly.domain[1]) - poly(poly.domain[0]))/days