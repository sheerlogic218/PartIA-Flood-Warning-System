from floodsystem.flood import stations_level_over_threshold
from floodsystem.stationdata import build_station_list, update_water_levels


def main():
    stations = build_station_list()
    update_water_levels(stations)
    tol = 0.8
    print("Stations with water levels over the threshold:")
    stations = stations_level_over_threshold(stations, tol)
    for station in stations:
        print(station[0].name, station[1])


if __name__ == "__main__":
    main()