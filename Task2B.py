from floodsystem.flood import stations_level_over_threshold
from floodsystem.stationdata import build_station_list, update_water_levels


def main():
    # Build list of stations
    stations = build_station_list()
    # Update water levels
    update_water_levels(stations)
    #print all stations with water levels over the threshold
    tol = 0.8
    print("Stations with water levels over the threshold:")
    print(stations_level_over_threshold(stations, tol))
    



if __name__ == "__main__":
    main()