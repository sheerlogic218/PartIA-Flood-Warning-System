from floodsystem.flood import stations_level_over_threshold
import floodsystem.station
from floodsystem.stationdata import update_water_levels


sample_stations = [floodsystem.station.MonitoringStation("1", "None", "A", (1, 1), [0,2], "river", None),
                   floodsystem.station.MonitoringStation("2", "None", "B", (3, 3), [0,2], "river", None),
                   floodsystem.station.MonitoringStation("3", "None", "C", (2, 2), [0,2], "river2", None)
                   ]
sample_stations[0].latest_level = 1.8
sample_stations[1].latest_level = 0.9
sample_stations[2].latest_level = 0.1


def test_stations_level_over_threshold():
    assert stations_level_over_threshold(sample_stations, tol = 0.5)[0][0] == sample_stations[0]



