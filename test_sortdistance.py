from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance

def test_stations_by_distance():
    """Tests the function of the sort by distance algorithm by comparing the nearest station to the coordinate of a random point in central London
    to its calculated station (by using the town). Tests increase in distance by checking the difference between the first and second entry
    in the sorted list."""
    x = build_station_list()
    sorted = stations_by_distance(x, (51.5072, -0.1276))
    sortedfirst = sorted[0]
    sortedfirststation = sortedfirst[0]
    sortedsecond = sorted[1]
    assert sortedfirststation.town == 'Streatham'
    assert sortedfirst[1] - sortedsecond[1] > 0



    