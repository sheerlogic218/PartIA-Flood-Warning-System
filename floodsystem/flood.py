
from .utils import sorted_by_key
from .station import MonitoringStation


def stations_level_over_threshold(stations, tol):
    '''Returns list of stations with water levels over the threshold'''
    tol_stations = [(station, station.relative_water_level) for station in stations if station.relative_water_level() is not None and station.relative_water_level() > tol]
    return sorted_by_key(tol_stations, 1, reverse=True)