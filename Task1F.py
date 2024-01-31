from floodsystem.station import inconsistent_typical_range_stations
from floodsystem.stationdata import build_station_list


def main():
    stations = build_station_list()
    inconsistent = inconsistent_typical_range_stations(stations)
    inconsistent = sorted(inconsistent, key=lambda station: station.name)
    names = [station.name for station in inconsistent]
    print(names)


if __name__ == "__main__":
    main()