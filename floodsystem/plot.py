
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