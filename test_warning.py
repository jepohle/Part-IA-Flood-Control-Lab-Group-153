from floodsystem.stationdata import build_station_list
from floodsystem.warning import categorise_town_flood_risk


def test_warning():
    x = build_station_list()
    short = x[:20]
    output = categorise_town_flood_risk(short, 2, 4, 1)
    assert len(output) == 20
