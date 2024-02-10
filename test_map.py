from floodsystem.geo import map_stations
from floodsystem.stationdata import build_station_list

def test_map_stations():
    try:
        stations = build_station_list()
        map_stations(stations)
    except:
        assert False
    assert True


def main():
    stations = build_station_list()
    map_stations(stations, show=True)



if __name__ == "__main__":  
    main()
