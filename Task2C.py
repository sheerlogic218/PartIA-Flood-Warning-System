from floodsystem.flood import stations_highest_rel_level
from floodsystem.stationdata import build_station_list


def main():
    # Build list of stations
    stations = build_station_list()

    # Find and print the 5 stations with the highest relative water levels
    N = 5
    print("5 stations with the highest relative water levels:")
    print(stations_highest_rel_level(stations, N))


if __name__ == "__main__":
    main()