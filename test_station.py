# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""Unit test for the station module"""

from floodsystem.station import *


def test_create_monitoring_station():

    # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    assert s.station_id == s_id
    assert s.measure_id == m_id
    assert s.name == label
    assert s.coord == coord
    assert s.typical_range == trange
    assert s.river == river
    assert s.town == town


def test_typical_range_consistent():

    # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    # Test if the above typical range is consistent
    assert s.typical_range_consistent() is True

    # Test if this new atypical range is inconsistent
    s.typical_range = (118.0, 1.0)
    assert s.typical_range_consistent() is False


def test_inconsistent_typical_range_stations():

    # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

     # Create another station
    s_id2 = "test-s-id"
    m_id2 = "test-m-id"
    label2 = "another station"
    coord2 = (-3.0, 8.0)
    trange2 = (4.2, -5.7)
    river2 = "River X"
    town2 = "My Town"
    s2 = MonitoringStation(s_id2, m_id2, label2, coord2, trange2, river2, town2)

    # Test if the function returns the correct list
    stations = [s,s2]

    assert len(inconsistent_typical_range_stations(stations)) == 1
    assert inconsistent_typical_range_stations(stations)[0] == s2