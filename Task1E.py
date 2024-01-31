from floodsystem.geo import rivers_by_station_number
from floodsystem.stationdata import build_station_list

def main():
    stations = build_station_list()
    N = 9
    top_N = rivers_by_station_number(stations, N)
    print("Top", N, "rivers with the most number of stations:")
    print(top_N)

if __name__ == "__main__":
    main()
