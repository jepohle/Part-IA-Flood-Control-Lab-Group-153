from floodsystem.stationdata import build_station_list
from floodsystem.warning import categorise_town_flood_risk


def run():
    x = build_station_list()
    print(len(x))
    short = x[:20]
    output = categorise_town_flood_risk(short, 2, 4, 1)
    print(output)

if __name__ == "__main__":
    print("*** Task 2G: CUED Part IA Flood Warning System ***")
    run()