from floodsystem.plot import plot_water_levels
from floodsystem.stationdata import build_station_list
from floodsystem.datafetcher import fetch_measure_levels
import datetime as dt



def main():
    # Build list of stations
    stations = build_station_list()
    # Choose a station
    station = stations[10]
    # Fetch the water level data
    dates, levels = fetch_measure_levels(station.measure_id, dt.timedelta(days=5))
    # Plot
    plot_water_levels(station, dates, levels)

if __name__ == "__main__":
    print("*** Task 2E: CUED Part IA Flood Warning System ***")
    main()

