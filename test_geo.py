from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance

def test_stations_by_distance():
    """Tests the function of the sort by distance algorithm by checking for an increase in distance by checking the difference between the first and second entry
    in the sorted list."""
    x = build_station_list()
    sorted = stations_by_distance(x, (51.5072, -0.1276))
    sortedfirst = sorted[0]
    sortedsecond = sorted[1]
    diff = sortedfirst[1] - sortedsecond[1]
    assert  diff < 0



    