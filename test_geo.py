from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance
from floodsystem.geo import stations_by_river
from floodsystem.geo import rivers_with_station

def test_stations_by_distance():
    """Tests the function of the sort by distance algorithm by checking for an increase in distance by checking the difference between the first and second entry
    in the sorted list."""
    x = build_station_list()
    sorted = stations_by_distance(x, (51.5072, -0.1276))
    sortedfirst = sorted[0]
    sortedsecond = sorted[1]
    diff = sortedfirst[1] - sortedsecond[1]
    assert  diff < 0


def test_rivers_with_stations():
    """Tests if function rivers_with_station in callable and returns the expected datatype"""
    x = build_station_list()
    rivers = rivers_with_station(x)
    assert type(rivers) == set

def test_stations_by_river():
    """Tests if function stations_by_rivers in callable and returns the expected datatype"""
    x = build_station_list()
    stations = stations_by_river(x)
    assert type(stations) == dict



    