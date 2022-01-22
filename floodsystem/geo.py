# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""
import numpy as np
from utils import sorted_by_key  # noqa


def stations_by_distance(stations, p):
    list_by_distance = []
    for station in stations:
        distance = np.sqrt((station.coord[0] - p[0])**2 + (station.coord[1] - p[1])**2)
        list_by_distance.append((station, distance))
    return sorted_by_key(list_by_distance,1)
