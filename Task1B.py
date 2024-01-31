from floodsystem.geo import stations_by_distance
from floodsystem.stationdata import build_station_list



def main():
    # Build list of stations
    stations = build_station_list()

    #find the 10 closest stations to Cambridge
    p = (52.2053, 0.1218)
    stations_distance = stations_by_distance(stations, p)
    print("The 10 closest stations to Cambridge are: \n")
    for station in stations_distance[:10]:
        print("Station name: ", station[0].name+
               ", Town: ", station[0].town,
                "\nDistance: ", station[1]
                ,"\n")
    
    print("\n\nThe 10 furthest stations to Cambridge are: \n")
    for station in stations_distance[-10:]:
        print("Station name: ", station[0].name+
               ", Town: ", station[0].town,
                "\nDistance: ", station[1]
                ,"\n")



if __name__ == "__main__":
    main()
