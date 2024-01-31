# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""
import math
from .utils import sorted_by_key

def haversin(coordA, coordB):
    #convert degrees to radians
    lat1 = math.radians(coordA[0])
    lat2 = math.radians(coordB[0])
    lon1 = math.radians(coordA[1])
    lon2 = math.radians(coordB[1])
    r = 6371000  # metres
    #haversine 
    distance = 2*r*math.sqrt( math.sin( (lat2-lat1)/2 )**2 + math.cos(lat1)*math.cos(lat2)*math.sin( (lon2-lon1)/2 )**2 )
    return distance



def stations_by_distance(stations, p):
    stations_distance = []
    for station in stations:
        stations_distance.append((station, haversin(station.coord, p)))
    return sorted_by_key(stations_distance,1, reverse=False)

