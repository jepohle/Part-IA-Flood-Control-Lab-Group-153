from floodsystem.stationdata import build_station_list
from floodsystem.flood import stations_level_over_threshold

def test_stations_level_over_threshold():
    x = build_station_list()
    stations_level_over_threshold(x, 0.5)
    levels = []
    for i in x:
        levels.append(i[1])
    for value in levels:
        assert  value > 0.5
    for i in range(len(levels)):
        assert levels[i+1] <= levels[i]
