from floodsystem.geo import stations_by_distance
from floodsystem.geo import stations_within_radius
from floodsystem.stationdata import build_station_list
from floodsystem.utils import sorted_by_key

def run():
    stations = build_station_list()
    list = stations_within_radius(stations, (52.2053, 0.1218), 10)
    list.sort()
    for item in list:
        print(item.name)


if __name__ == "__main__":
    print("*** Task 1C: CUED Part IA Flood Warning System ***")
    run()