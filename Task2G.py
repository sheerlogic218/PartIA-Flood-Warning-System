import numpy as np
import matplotlib.pyplot as plt
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

    potential_risk = potentially_at_flood_risk(stations)
    station_gradient = np.array([])

    #for stations at risk, determine how at risk they are
    for station in potential_risk:
        #find rate of increase of water level

        dates, levels = fetch_measure_levels(station.measure_id, dt.timedelta(days=2))
        if dates == []:
            continue
        poly, date_shift = polyfit(dates, levels, 4)
        gradient = current_gradient(poly, mpdates.date2num(dates[-1]) - date_shift)
        np.append(station_gradient, (station.name, gradient))
        print(station.name, gradient)
    #sort stations by rate of increase
    sorted_stations = sorted(station_gradient, key = lambda x: x[1], reverse = True)
    print(sorted_stations)


    below, normal, higher, no_data = station_categorization(stations)
    map_station_type(below, normal, higher, no_data)



if __name__ == "__main__":
    main()