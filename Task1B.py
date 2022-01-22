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
    
    list_far = []
    for n in range(10):
        station_and_distance = i[n-10]
        my_station = station_and_distance[0]
        tuple = (my_station.name, my_station.town, station_and_distance[1])
        list_far.append(tuple)
    print("The ten closest measuring stations are:", list)
    print()
    print("The ten furthest measuring stations are:", list_far)


if __name__ == "__main__":
    print("*** Task 1B: CUED Part IA Flood Warning System ***")
    run()