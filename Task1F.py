from floodsystem.stationdata import build_station_list
from floodsystem.station import inconsistent_typical_range_stations

def run():
    """Prints a list of the names of stations with faulty range data."""
    x = build_station_list()
    inconsistentstations = inconsistent_typical_range_stations(x)
    names = [station.name for station in inconsistentstations]
    names.sort()
    print(names)



if __name__ == "__main__":
    print("*** Task 1F: CUED Part IA Flood Warning System ***")
    run()
