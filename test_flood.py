from floodsystem.flood import stations_level_over_threshold
import floodsystem.station


sample_stations = [floodsystem.station.MonitoringStation("1", "None", "A", (1, 1), 2, "river", None),
                   floodsystem.station.MonitoringStation("2", "None", "B", (3, 3), 2, "river", None),
                   floodsystem.station.MonitoringStation("3", "None", "C", (2, 2), 2, "river2", None)
                   ]


def test_stations_level_over_threshold():
    tol = 0.5
