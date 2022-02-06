from floodsystem.stationdata import build_station_list
from floodsystem.warning import categorise_town_flood_risk


def run():
    x = build_station_list
    output = categorise_town_flood_risk(x, 2, 4)
    print(output)

if __name__ == "__main__":
    print("*** Task 2G: CUED Part IA Flood Warning System ***")
    run()