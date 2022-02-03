from floodsystem.utils import sorted_by_key


def stations_level_over_threshold(stations, tol):
    """A function that takes a list of station objects and a threshold value for relative water level and returns a list of station object which
    have a flood level higher than the tolerance. It takes form stations_level_over_threshold(list of station objects, tolerance (float))."""
    list = []
    for station in stations:
        rellevel = station.relative_water_level()
        if rellevel == None:
            continue
        elif rellevel > tol:
            if rellevel > 10:
                continue
            else:
                list.append((station, station.relative_water_level()))
    return sorted_by_key(list, 1, reverse=True)

def stations_highest_rel_level(stations, N):
    """Returns the N stations with the highest relative water level from a list of station objects (stations)."""
    list = []
    for station in stations:
        rellevel = station.relative_water_level()
        if rellevel == None:
            continue
        else:
            list.append((station, station.relative_water_level()))
    listsorted = sorted_by_key(list, 1, reverse=True)
    output = [x[0] for x in listsorted]
    return output[:N]