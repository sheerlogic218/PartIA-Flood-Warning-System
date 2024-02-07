from floodsystem.geo import stations_by_distance, stations_within_radius
from floodsystem.stationdata import build_station_list

def main():

    stations = build_station_list()
    p = (52.2053, 0.1218)

    #find stations within 10km of Cambridge
    valid_stations = stations_within_radius(stations, p, 10)

    #sort by name in alphabetical order
    valid_stations = sorted(valid_stations, key = lambda station: station.name)
    valid_names = [station.name for station in valid_stations]

    print("\nStations within 10km of Cambridge: ")
    for station in valid_stations:
        print(station.name)
    #print(valid_names)
    

if __name__ == "__main__":
    main()