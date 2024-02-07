
import matplotlib.pyplot as plt

def plot_water_levels(station, dates, levels):
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
    plt.show()

