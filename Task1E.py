from floodsystem.geo import rivers_with_station
from floodsystem.stationdata import build_station_list
from floodsystem.utils import sorted_by_key
from floodsystem.geo import stations_by_river
from floodsystem.geo import rivers_by_station_number



def run():
    # Build list of stations
    stations = build_station_list()
    my_list = rivers_by_station_number(stations, 9)
    print(my_list)





if __name__ == "__main__":
    print("*** Task 1E: CUED Part IA Flood Warning System ***")
    run()
