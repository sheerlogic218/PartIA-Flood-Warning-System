from floodsystem.plot import plot_water_levels
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.datafetcher import fetch_measure_levels
import datetime as dt



def main():
    # Build list of stations
    stations = build_station_list()
    update_water_levels(stations)

    #10 stations with the highest relative water levels, may contain None type
    stations.sort(key = lambda x: x.relative_water_level() if x.relative_water_level() != None else 0 , reverse = True)

    top_10_stations = stations[:10]
    #print(top_10_stations)
    for station in top_10_stations:
        dates, levels = fetch_measure_levels(station.measure_id, dt.timedelta(days=10))
        plot_water_levels(station, dates, levels)
    


if __name__ == "__main__":
    print("*** Task 2E: CUED Part IA Flood Warning System ***")
    main()

