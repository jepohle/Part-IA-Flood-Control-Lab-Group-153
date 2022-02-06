#%%

import datetime


from floodsystem.flood import stations_highest_rel_level
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.plot import plot_water_levels

def run():
    stations = build_station_list()
    update_water_levels(stations)
    highest = stations_highest_rel_level(stations, 5)
    for station in highest:
        date, level = fetch_measure_levels(station.measure_id, datetime.timedelta(9))
        plot_water_levels(station, date, level)


if __name__ == "__main__":
    print("*** Task 2E: CUED Part IA Flood Warning System ***")
    run()