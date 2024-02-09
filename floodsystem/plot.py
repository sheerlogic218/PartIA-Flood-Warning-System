import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
import datetime as dt
import pandas as pd

def plot_water_levels(station, dates, levels, show = True):
    #plot the water levels for a given station
    #also show typical high and low levels
    name = station.name
    typical_range = station.typical_range
    plt.plot(dates, levels)
    plt.xlabel('date')
    plt.ylabel('water level')
    plt.title(name)
    plt.xticks(rotation=45)
    plt.axhline(typical_range[0], color='r', linestyle='--')
    plt.axhline(typical_range[1], color='r', linestyle='--')
    if show:
        plt.show()


def plot_water_levels_with_fit(station, dates, levels, p):
    """Plot water levels and polynomial of best fit."""
    print(dates[0])
    # Create polynomial of best fit
    poly = np.polyfit(dates - dates[0], levels, p)

    # Create plot
    plt.plot(dates, levels, label='water levels')
    plt.plot(dates, np.polyval(poly, dates - dates[0]), label='polyfit')
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.title('Water levels and polynomial of best fit for station: ' + station.name)
    plt.legend()
    plt.show()