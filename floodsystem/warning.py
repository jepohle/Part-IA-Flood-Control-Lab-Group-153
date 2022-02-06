import matplotlib
from floodsystem.analysis import polyfit
from floodsystem.datafetcher import fetch_measure_levels
import datetime
import numpy as np

from floodsystem.utils import sorted_by_key

def categorise_town_flood_risk(stations, dt, degree, risklevel=3):
    """A function that takes a list "stations" of station objects, performs polyfit over a period of "dt" days up to a "degree" degree and then returns towns with their respective flood risk.
    The flood risk is determined by three tolerances (tol1, tol2, tol3) which are taken in as arguments. tol1 defines the lower boundary of severe flood risk. tol2 defines the lower boundary
    of high flood risk and tol3 defines the lower boundary of moderate flood risk. Any towns with a flood risk index below tol3 are deemed to have a low risk of flooding. These tolerances are
    calculated internally by modelling the risks as a normal distribution. tol1 == mean + 2 * standard deviation, tol2 == mean + standard deviation, tol3 == mean. This is not an accurate warning
    system when all stations have risk of flooding, but it gives a good indication for stations that have a higher than normal increase in water level. The vara"""

    towns = {}
    for station in stations:                                                                    #iterate through list of station objects and create dictionary of stations in a town
        if station.town in towns.keys():
            towns[station.town].append(station)
        else:
            towns[station.town] = [station]
    townsandrisks = []                                                                          #create empty list for towns and their risk rating
    total_risks = []                                                                            #create empty list for all risk-indices to calculate spread of risk and thresholds for flooding
    risk_by_town = []                                                                           #create empty list for towns and their highes risk-index
    
    for town in towns.keys():
        riskindicator = []
        stations = towns.get(town)
        for station in stations:
            dates, levels = fetch_measure_levels(station.measure_id, datetime.timedelta(dt))
            if len(dates) == 0:                                                                 #use polyfit function to extract coefficients and d0 from the stations in question
                continue        
            poly, d0 = polyfit(dates, levels, degree)
            coeffs = poly.c
            diffcoeffs = np.zeros(len(coeffs))
            for i in range(len(coeffs)):
                diffcoeffs[i] = coeffs[i]*(len(coeffs)-i-1)                                     #create list with differentiated coefficients (original coefficient multiplied by the grade of the polynomial (determined by i))
            diff_value = 0                                                                      #calculate the instantaneus rate of change at the last date in the list of dates
            x = matplotlib.dates.date2num(dates)
            for i in range(len(diffcoeffs)):
                diff_value += diffcoeffs[i]*(x[-1]+d0)**i
            riskindicator.append(diff_value)
            total_risks.append(diff_value)
        if len(riskindicator) == 0:
            continue
        risk_by_town.append((town, max(riskindicator)))

    mean = np.mean(total_risks)                                                                 #as we are trying to find relative flood risks and want to determine the towns with the highest flood risk in the country, we can assume that the risk-index is distributed normally
    st_dev = np.std(total_risks)                                                                #using the mean and standard deviation we can set the boundaries for severe, high, moderate and low flood risk
    tol1 = mean + 2 * st_dev
    tol2 = mean + st_dev
    tol3 = mean

    for town in risk_by_town:
        if town[1] > tol1:                                                              #append and sort a list of towns and their risk level as tuples. 0 == low, 1 == moderate, 2 == high, 3 == severe 
            townsandrisks.append((town[0], 3))                                        #Exact tolerances to be determined once 2F completed!
        elif town[1] <= tol1 and town[1] > tol2:
            townsandrisks.append((town[0], 2))
        elif town[1] <= tol2 and town[1] > tol3:
            townsandrisks.append((town[0], 1))
        elif town[1] <= tol3:
            townsandrisks.append((town[0], 0))
    sorted_by_key(townsandrisks, 1, reverse=True)
    greatestrisks = []
    for town in townsandrisks:
        if town[1] >= risklevel:
            greatestrisks.append(town)                                                  #return list of towns with severe flood risk
    return greatestrisks