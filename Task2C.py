from floodsystem.flood import stations_highest_rel_level
from floodsystem.stationdata import build_station_list, update_water_levels


def main():
    stations = build_station_list()
    update_water_levels(stations)
    N = 10
    print("10 stations with the highest relative water levels:")
    stations = stations_highest_rel_level(stations, N)
    for station in stations:
        print(station[0].name, station[1])

if __name__ == "__main__":
    main()