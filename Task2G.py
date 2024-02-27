import numpy as np
import matplotlib.dates as mpdates
from floodsystem.stationdata import *
from floodsystem.datafetcher import *
from floodsystem.plot import *
from floodsystem.analysis import *
from floodsystem.geo import *
import datetime as dt


def main():

    stations = build_station_list()
    update_water_levels(stations)
    stations.sort(key = lambda x: x.relative_water_level() if x.relative_water_level() != None else 0 , reverse = True)
    #uses cache to avoid fetching data again
    try:
        with open("cache/station_risk.json", "r") as f:
            sorted_stations = json.load(f)
    except:

        potential_risk = potentially_at_flood_risk(stations)
        #find the gradient of the water level for each station
        station_gradient = []
        for station in potential_risk:
            dates, levels = fetch_measure_levels(station.measure_id, dt.timedelta(days=2))
            if dates == []:
                continue
            poly, date_shift = polyfit(dates, levels, 4)
            gradient = current_gradient(poly, mpdates.date2num(dates[-1]) - date_shift)
            station_gradient.append([station.name, gradient])
            #indicates progress
            if len(station_gradient) % 10 == 0:
                print(len(station_gradient))
        #sort the stations by gradient
        sorted_stations = sorted(station_gradient, key = lambda x: x[1], reverse = True)
        #cache the data
        with open("cache/station_risk.json", "w") as f:
            json.dump(sorted_stations, f)

    #defining high risk as high gradient and high current water level
    #high water level is high risk of flooding, high gradient is an indicator of where might be a flood risk soon
    #in proper systems we could use more weather data to better predict the future rainfall
    n = 10
    top_n_increase = {name: gradient for name, gradient in sorted_stations[:n]}
    top_n_level = {stations.name: stations.relative_water_level() for stations in stations[:n]}

    most_at_risk = {}
    for name, gradient in top_n_increase.items():
        most_at_risk[name] = "High gradient with: " + str(gradient)
    for name, level in top_n_level.items():
        if name in most_at_risk:
            most_at_risk[name] += ", High water level with: " + str(level)
        else:
            most_at_risk[name] = "High water level with: " + str(level)

    for name, risk in most_at_risk.items():
        print(name.ljust(35), risk)

    print("\nnow showing the categorized stations")
    below, normal, higher, no_data = station_categorization(stations)
    map_station_type(below, normal, higher, no_data)



if __name__ == "__main__":
    main()