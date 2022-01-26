from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level, stations_level_over_threshold

def test_stations_level_over_threshold():
    """Test for the function returning a sorted list of tuples (station, relative water level) of stations with relative water level over a threshold."""
    x = build_station_list()
    update_water_levels(x)
    station = stations_level_over_threshold(x, 0.5)
    levels = []
    for i in station:
        levels.append(i[1])
    for value in levels:
        assert  value > 0.5
    for i in range(len(levels)):
        assert levels[i+1] <= levels[i]

def test_stations_highest_rel_level():
    """Test for the function that returns the N stations with the highest relative water level."""
    x = build_station_list()
    update_water_levels(x)
    station = stations_highest_rel_level(x, 10)
    levels = []
    for i in station:
        levels.append(i.relative_water_level())
    assert len(station) == 10
    for i in range(len(levels)):
        assert levels[i+1] <= levels[i]