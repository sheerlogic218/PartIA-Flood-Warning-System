from floodsystem.geo import stations_by_distance
from floodsystem.stationdata import build_station_list



def main():
    # Build list of stations
    stations = build_station_list()

    p = (52.2053, 0.1218)
    stations_distance = stations_by_distance(stations, p)
    print("The 10 closest stations to Cambridge are: \n")
    #prints nicely
    # for station in stations_distance[:10]:
    #     print("Station name: ", station[0].name+
    #            ", Town: ", station[0].town,
    #             "\nDistance: ", station[1]
    #             ,"\n")
    closest_10 = [(station[0].name, station[0].town, station[1]) for station in stations_distance[:10]]
    print(closest_10)
    
    print("\n\nThe 10 furthest stations to Cambridge are: \n")
    #prints nicely
    # for station in stations_distance[-10:]:
    #     print("Station name: ", station[0].name+
    #            ", Town: ", station[0].town,
    #             "\nDistance: ", station[1]
    #             ,"\n")
    
    furthest_10 = [(station[0].name, station[0].town, station[1]) for station in stations_distance[-10:]]
    print(furthest_10)


if __name__ == "__main__":
    main()
