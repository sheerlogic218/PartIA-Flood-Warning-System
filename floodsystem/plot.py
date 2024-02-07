
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
from datafetcher import fetch_measure_levels
from stationdata import build_station_list
import datetime as dt

def plot_water_levels(station, dates, levels):
    #plot the water levels for a given station
    name = station.name
    plt.plot(dates, levels)
    plt.xlabel('Date')
    plt.ylabel('Water Level (m)')
    plt.title('Water Level at ' + name)
    plt.show()
    return

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