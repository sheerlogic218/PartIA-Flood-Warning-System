from floodsystem.geo import map_stations
from floodsystem.stationdata import build_station_list

def test_map_stations():
    stations = build_station_list()
    map_stations(stations)
    return

test_map_stations()
