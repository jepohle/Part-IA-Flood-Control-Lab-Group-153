import numpy as np
import matplotlib.pyplot as plt
import matplotlib

def polyfit(dates, levels, p):
    dates_num = matplotlib.dates.date2num(dates)
    poly_coeff = np.polyfit(dates_num - dates_num[0], levels, p)#get best fit coefficients
    poly = np.poly1d(poly_coeff)
    return poly, dates_num[0]