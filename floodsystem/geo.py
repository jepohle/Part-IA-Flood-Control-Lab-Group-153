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
    """Calculates the distance of stations in a list of station objects from a center point p (latitude, longitude).
    This function has form calc_distance(list of station object, coordinate of center) """
    return 2 * 6371 *np.sqrt(np.sin((station.coord[0] - p[0]) * np.pi/360)**2 + np.cos(station.coord[0] * np.pi/180)
    *np.cos(p[0]*np.pi/180)*(np.sin((station.coord[1] - p[1])*np.pi/360)**2))

def stations_within_radius(stations, center, r):
    """Returns list of station objects from a list of station objects within a certain radius r (in km) 
    of a coordinate tuple 'center' (latitude, longitude). This function has form stations_within_radius(list of station objects, coordinates of center,
    radius in km)."""
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

def rivers_by_station_number(stations, N):
    """Returns N rivers with the gratest number of monitoring stations on them, given the list of stations(stations) and the number of stations required (N)
    if more than one river have as many monitoring stations as the Nth entry, those rivers are included in the list
    The data is returned in the form of a list of tuples, where each tuple contains the river name and the number of monitoring stations (river name, numer of stations)"""
    stations_by_river = {}
    for station in stations:
        try:
            stations_by_river[station.river] = stations_by_river[station.river] + 1
        except:
            stations_by_river[station.river] = 1
    
    ls = []
    for key, value in stations_by_river.items():
        ls.append((key, value))
    
    ls = sorted_by_key(ls, 1, True)
    boundary = ls[N][1]
    rivers_final = []
    for item in ls:
        if(item[1] >= boundary):rivers_final.append(item)
    
    return rivers_final



