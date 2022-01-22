from floodsystem.geo import stations_by_distance
from floodsystem.stationdata import build_station_list
import numpy as np

def run():
    stations = build_station_list()
    
    i = stations_by_distance(stations, (0,0))
    print(i[:10])

if __name__ == "__main__":
    print("*** Task 1B: CUED Part IA Flood Warning System ***")
    run()