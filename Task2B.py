from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_level_over_threshold

def run():
    x = build_station_list()
    update_water_levels(x)
    stations = stations_level_over_threshold(x, 0.8)
    for station in stations:
        stationob = station[0]
        level = station[1]
        print(stationob.name, level)

if __name__ == "__main__":
    print("*** Task 2B: CUED Part IA Flood Warning System ***")
    run()
