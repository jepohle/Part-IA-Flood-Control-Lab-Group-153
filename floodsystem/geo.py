# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""
import numpy as np
from floodsystem.utils import sorted_by_key  # noqa


def stations_by_distance(stations, p):
    """Takes a list of measuring stations and calculates the distance to a given coordinate p.
    Then sorts this list and outputs a list of tuples of format (station, distance)."""

    list_by_distance = []
    for station in stations: ## distances in km
        distance = calc_distance(station, p)
        list_by_distance.append((station, distance))
    return sorted_by_key(list_by_distance,1)


def calc_distance(station, p):
    return 2 * 6371 *np.sqrt(np.sin((station.coord[0] - p[0]) * np.pi/360)**2 + np.cos(station.coord[0] * np.pi/180)
    *np.cos(p[0]*np.pi/180)*(np.sin((station.coord[1] - p[1])*np.pi/360)**2))

def stations_within_radius(stations, center, r):
    list = []
    for station in stations:
        if(calc_distance(station, center) <= r):
            list.append(station)
    return list

def rivers_with_station(stations):
    """Returns a set of all rivers that have a monitoring station from a list of station objects. This function has form rivers_with_stations(list of
    station objects)."""
    rivers = {station.river for station in stations}
    return rivers

def stations_by_river(stations):
    """Returns a dictionary with rivers as keys and station names as the values. This function has form stations_by_rivers(list of station objects)."""
    rivers = rivers_with_station(stations)                      #get a list of all the possible river names
    dictionary = {river:[] for river in rivers}                 #create dictionary with rivers as keys
    for station in stations:
        dictionary[station.river].append(station)               #append the empty dictionary with the respective station objects
    return dictionary