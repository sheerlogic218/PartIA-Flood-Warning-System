
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime


def plot_water_levels_with_fit(station, dates, levels, p):
    """Plot water levels and polynomial of best fit."""
    # Convert dates to numbers
    dates = plt.dates.date2num(dates)

    # Fit polynomial
    poly = np.polyfit(dates - dates[0], levels, p)

    # Create plot
    plt.plot(dates, levels, label='water levels')
    plt.plot(dates, np.polyval(poly, dates - dates[0]), label='polyfit')
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.title('Water levels and polynomial of best fit for station: ' + station.name)
    plt.legend()
    plt.show()