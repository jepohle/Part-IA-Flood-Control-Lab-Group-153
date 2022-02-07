from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.datafetcher import fetch_measure_levels
import numpy as np
from floodsystem.analysis import polyfit 
import datetime


def test_polyfit():
    x = build_station_list()
    update_water_levels(x)
    dates, levels = fetch_measure_levels(x[0].measure_id, datetime.timedelta(3))
    test_levels = np.full(len(dates), 1).tolist()
    p, d0 = polyfit(dates, test_levels, 3)
    print(p)
    assert round(p.c[0], 10) == 0
    assert round(p.c[1], 10) == 0
    assert round(p.c[2], 10) == 0
    assert round(p.c[3], 10) == 1

