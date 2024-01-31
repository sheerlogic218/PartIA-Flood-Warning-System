# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""
import math
from .utils import sorted_by_key

def haversin(coordA, coordB):
    '''Returns the arc length between two points on the earth's surface for the great circle joining the two points.'''
    #convert degrees to radians
    lat1 = math.radians(coordA[0])
    lat2 = math.radians(coordB[0])
    lon1 = math.radians(coordA[1])
    lon2 = math.radians(coordB[1])
    r = 6371  # kilometres
    #haversine 
    distance = 2*r*math.sqrt( math.sin( (lat2-lat1)/2 )**2 + math.cos(lat1)*math.cos(lat2)*math.sin( (lon2-lon1)/2 )**2 )
    return distance


def stations_by_distance(stations, p):
    '''Returns a list of tuples with stations and their distances from the point p in ascending order of distance.'''
    return sorted_by_key( [ (station , haversin(station.coord,p)) for station in stations ], 1)

def stations_within_radius(stations, centre, r):
    '''Returns a list of stations within a distance r from the centre.'''
    return [station for station in stations if haversin(station.coord, centre) <= r]


def rivers_with_station(stations):
    '''Returns a list of rivers with at one or more monitoring stations.'''
    rivers = [station.river for station in stations if station.river is not None]
    return sorted(set(rivers))

def stations_by_river(stations):
    '''Returns a dictionary where keys correspond to rivers and values to lists of stations on that river.'''
    rivers = rivers_with_station(stations)
    river_stations = {river: [] for river in rivers}
    for station in stations:
        if station.river is not None:
            river_stations[station.river].append(station.name)
    return river_stations


def rivers_by_station_number(stations, N):
    '''Returns a list of tuples with rivers and their numbers of stations, sorted in descending order of the number of stations of each river.'''
    river_stations = stations_by_river(stations)
    river_num_stations = [(river, len(stations)) for river, stations in river_stations.items()]
    river_num_stations = sorted_by_key(river_num_stations, 1, reverse=True)
    first_N = river_num_stations[:N]
    #include rivers with same number of stations as the last river in the top N
    for river, num_stations in river_num_stations[N:]:
        if num_stations == first_N[-1][1]:
            first_N.append((river, num_stations))
    return first_N
