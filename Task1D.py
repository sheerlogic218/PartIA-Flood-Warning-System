from floodsystem.geo import rivers_with_station, stations_by_river
from floodsystem.stationdata import build_station_list


def main():

    stations = build_station_list()

    rivers = rivers_with_station(stations)
    print("\nNum rivers with station", len(rivers))
    print("List of first 10 rivers with at least one monitoring station:")
    print(rivers[:10])

    river_stations = stations_by_river(stations)
    sample_rivers = ["River Aire", "River Cam", "River Thames"]
    print("\nsample rivers with their stations:\n")
    for river in sample_rivers:
        print(river, ":", sorted(river_stations[river]),"\n")

if __name__ == "__main__":
    main()