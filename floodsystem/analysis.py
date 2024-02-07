import numpy as np
import matplotlib.pyplot as plt

def polyfit(dates, levels, p):
    """Calculate polynomial of best fit."""

    # Convert dates to numbers
    dates = plt.dates.date2num(dates)

    # Fit polynomial
    poly = np.polyfit(dates - dates[0], levels, p)

    return poly