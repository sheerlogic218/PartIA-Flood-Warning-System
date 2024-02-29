import floodsystem.geo
import floodsystem.station
import floodsystem.stationdata
import floodsystem.analysis
import math
import pandas as pd
import numpy as np

sample_stations = [floodsystem.station.MonitoringStation("1", "None", "A", (1, 1), (1,2), "river", None),
                   floodsystem.station.MonitoringStation("2", "None", "B", (3, 3), (1,3), "river", None),
                   floodsystem.station.MonitoringStation("3", "None", "C", (2, 2), (0,2), "river2", None)
                   ]

def test_polyfit():
    dates = [1, 2, 3, 4, 5]
    levels = [1, 2, 3, 4, 5]
    assert type(floodsystem.analysis.polyfit(dates, levels, 1)) == tuple

def test_current_gradient():
    dates = [1, 2, 3, 4, 5]
    levels = [1, 2, 3, 4, 5]
    poly, date_shift = floodsystem.analysis.polyfit(dates, levels, 1)
    assert type(floodsystem.analysis.current_gradient(poly, 5)) == np.float64

