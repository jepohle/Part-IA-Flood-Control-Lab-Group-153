from floodsystem.geo import stations_by_distance
from floodsystem.stationdata import build_station_list

def run():
    stations = build_station_list()
    i = stations_by_distance(stations, (52.2053,0.1218))
    list = []
    for n in range(10):
        station_and_distance = i[n]
        my_station = station_and_distance[0]
        tuple = (my_station.name, my_station.town, station_and_distance[1])
        list.append(tuple)
    print(list)

    
if __name__ == "__main__":
    print("*** Task 1B: CUED Part IA Flood Warning System ***")
    run()