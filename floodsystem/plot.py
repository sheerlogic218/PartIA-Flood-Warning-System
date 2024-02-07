
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

