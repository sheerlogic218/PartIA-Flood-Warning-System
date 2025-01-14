import matplotlib.pyplot as plt
import matplotlib.dates as mpdates
import numpy as np
import floodsystem.analysis as analysis

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


def plot_water_level_with_fit(station, dates, levels, p, show = True):
    year = dates[0].year
    name = station.name
    poly, date_shift = analysis.polyfit(dates, levels, p)
    num_dates = np.array(mpdates.date2num(dates))

    plt.plot(dates, levels, label = "Actual Data")
    plt.plot(dates, poly(num_dates - date_shift), label = "Polynomial Fit")

    plt.xlabel('date')
    plt.ylabel('water level')
    plt.title(name + " Water Levels" + " in " + str(year))
    plt.xticks(rotation=45)

    plt.axhline(station.typical_range[0], color='r', linestyle='--', label = "Typical Range")
    plt.axhline(station.typical_range[1], color='r', linestyle='--')
    plt.legend()
    if show:
        plt.show()

