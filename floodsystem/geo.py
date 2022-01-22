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
    Then sorts this list and outputs a touple of format (station, distance)."""

    list_by_distance = []
    for station in stations:
        distance = np.sqrt((station.coord[0] - p[0])**2 + (station.coord[1] - p[1])**2)
        list_by_distance.append((station, distance))
    return sorted_by_key(list_by_distance,1)
