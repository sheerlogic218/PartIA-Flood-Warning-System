from floodsystem.plot import plot_water_levels
from floodsystem.stationdata import build_station_list
import floodsystem.station

sample_stations = [floodsystem.station.MonitoringStation("1", "None", "A", (1, 1), 2, "river", None),
                   floodsystem.station.MonitoringStation("2", "None", "B", (3, 3), 2, "river", None),
                   floodsystem.station.MonitoringStation("3", "None", "C", (2, 2), 2, "river2", None)
                   ]

def test_plot_water_levels():
    #check that the code runs without error
    stations = build_station_list()
    station = stations[0]
    dates = [1, 2, 3, 4, 5]
    levels = [1, 2, 3, 4, 5]
    try:
        plot_water_levels(station, dates, levels, show = False)
    except:
        assert False
    assert True


