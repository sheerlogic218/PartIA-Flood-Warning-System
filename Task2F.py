from floodsystem.plot import plot_water_level_with_fit
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.datafetcher import fetch_measure_levels
import datetime as dt

def main():
    stations = build_station_list()
    update_water_levels(stations)
    stations.sort(key = lambda x: x.relative_water_level() if x.relative_water_level() != None else 0 , reverse = True)
    top_5_stations = stations[:5]
    for station in top_5_stations:
        dates, levels = fetch_measure_levels(station.measure_id, dt.timedelta(days=2))
        plot_water_level_with_fit(station, dates, levels, 4)

if __name__ == "__main__":
    main()

