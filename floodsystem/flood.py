from floodsystem.utils import sorted_by_key


def stations_level_over_threshold(stations, tol):
    """A function that takes a list of station objects and a threshold value for relative water level and returns a list of station object which
    have a flood level higher than the tolerance. It takes form stations_level_over_threshold(list of station objects, tolerance (float))."""
    list = []
    for station in stations:
        if station.relative_water_level() == None:
            continue
        elif station.relative_water_level() > tol:
            list += (station, station.relative_water_level())
    sorted_by_key(list, 1)
    return list

