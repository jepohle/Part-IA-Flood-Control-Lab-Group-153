from distutils.command.build import build
from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_by_station_number, stations_by_distance, stations_within_radius
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

def test_station_within_radius():
    """Test if funcion station_within_radius works correctly"""
    stations = build_station_list()
    stations_within_10k = stations_within_radius(stations, (52.2053, 0.1218) , 10)
    id_list = []
    for station in stations_within_10k:
        id_list.append(station.name)
    id_list.sort()
    assert id_list == ['Bin Brook', 'Cambridge Baits Bite', "Cambridge Byron's Pool",
 'Cambridge Jesus Lock', 'Comberton', 'Dernford', 'Girton',
 'Haslingfield Burnt Mill', 'Lode', 'Oakington', 'Stapleford']

def test_rivers_by_station_number():
    """Test to see if rivers_by_station_number is callable and if it returns valid data"""
    stations = build_station_list()
    rivers_by_station = rivers_by_station_number(stations, 1)
    test_river_name = rivers_by_station[0][0]
    print("testing number of stations for " + test_river_name)
    n = 0
    for station in stations:
        if(station.river == test_river_name):
            n += 1
    assert n == rivers_by_station[0][1] 




    