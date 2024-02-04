import floodsystem.geo
import floodsystem.station
import math

sample_stations = [floodsystem.station.MonitoringStation("1", "None", "A", (1, 1), 2, "river", None),
                   floodsystem.station.MonitoringStation("2", "None", "B", (3, 3), 2, "river", None),
                   floodsystem.station.MonitoringStation("3", "None", "C", (2, 2), 2, "river2", None)
                   ]
R = 6371


def test_haversin():
    coordA = (1 , 1)
    coordB = (2 , 2)
    assert type(floodsystem.geo.haversin(coordA, coordB)) == float

def test_station_by_distance():
    p = (0, 0)
    sample_stations_by_distance = floodsystem.geo.stations_by_distance(sample_stations, p)
    #remove distances from the list of tuples
    sample_stations_by_distance = [station for station, distance in sample_stations_by_distance]
    assert sample_stations_by_distance == [sample_stations[0], sample_stations[2], sample_stations[1]]

def test_stations_within_radius():
    centre = (0, 0)
    r = 2*R*math.pi/180
    sample_stations_within_radius = floodsystem.geo.stations_within_radius(sample_stations, centre, r)
    assert sample_stations_within_radius == [sample_stations[0]]

def test_rivers_with_station():
    sample_rivers_with_station = floodsystem.geo.rivers_with_station(sample_stations)
    assert sample_rivers_with_station == ["river", "river2"]

def test_stations_by_river():
    sample_stations_by_river = floodsystem.geo.stations_by_river(sample_stations)
    assert sample_stations_by_river == {"river": ["A", "B"], "river2": ["C"]}

def test_rivers_by_station_number():
    N = 1
    sample_rivers_by_station_number = floodsystem.geo.rivers_by_station_number(sample_stations, N)
    assert sample_rivers_by_station_number == [("river", 2)]

    N = 2
    sample_rivers_by_station_number = floodsystem.geo.rivers_by_station_number(sample_stations, N)
    assert sample_rivers_by_station_number == [("river", 2), ("river2", 1)]

