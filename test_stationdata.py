# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""Unit test for the stationdata module"""
import floodsystem.station
from floodsystem.stationdata import build_station_list, update_water_levels
import floodsystem.stationdata

sample_stations = [floodsystem.station.MonitoringStation("1", "None", "A", (1, 1), (1,2), "river", None),
                   floodsystem.station.MonitoringStation("2", "None", "B", (3, 3), (1,3), "river", None),
                   floodsystem.station.MonitoringStation("3", "None", "C", (2, 2), (0,2), "river2", None)
                   ]


def test_build_station_list():
    """Test building list of stations"""
    station_list = build_station_list()
    assert len(station_list) > 0


def test_update_level():
    """Test update to latest water level"""

    # Build list of stations
    stations = build_station_list()
    for station in stations:
        assert station.latest_level is None

    # Update latest level data for all stations
    update_water_levels(stations)
    counter = 0
    for station in stations:
        if station.latest_level is not None:
            counter += 1

    assert counter > 0

def test_potentially_at_flood_risk():
    sample_stations[0].latest_level = 0.5
    sample_stations[1].latest_level = 2
    sample_stations[2].latest_level = 5
    assert floodsystem.stationdata.potentially_at_flood_risk(sample_stations, 1) == [sample_stations[1], sample_stations[2]]


def test_station_categorization():
    sample_stations[0].latest_level = 0.5
    sample_stations[1].latest_level = 2
    sample_stations[2].latest_level = 5
    below, normal, above, no_data = floodsystem.stationdata.station_categorization(sample_stations)
    assert below == [sample_stations[0]]
    assert normal == [sample_stations[1]]
    assert above == [sample_stations[2]]
    assert no_data == []
