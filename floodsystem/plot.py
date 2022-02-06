import matplotlib.pyplot as plt
import matplotlib
from datetime import datetime, timedelta
import numpy as np
from floodsystem.analysis import polyfit
import sys, threading


def plot_water_levels(station, dates, level):


    """function that plots the absolute water level as a function of the station, dates and correcponding water levels"""
    # Plot
    plt.plot(dates, level, label = "real time data from station")
    plt.plot(dates, np.full(len(dates), station.typical_range[0]).tolist(), label = "typical low level")
    plt.plot(dates, np.full(len(dates), station.typical_range[1]).tolist(), label = "typical high level")

    # Add axis labels, rotate date labels and add plot title
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45)
    plt.title(station.name)
    plt.tight_layout()  # This makes sure plot does not cut off date labels
    plt.legend()
    plt.show()


def plot_water_level_with_fit(station, dates, levels, p):

    """function that plots the absolute water level as a function of the station, dates and correcponding water levels and adds a correcponding polynomial of best fit of order p"""
    # Plot
    print("calculation ply of o : " + str(p))
    plt.plot(dates, levels, label="real time data from station")
    poly, d0 = polyfit(dates, levels, p)#returns polynomial function
    num_dates = matplotlib.dates.date2num(dates)
    fit_levels = poly((num_dates - d0))
    plt.plot(dates, fit_levels, label="polynomial of best fit") 
    
    # Add axis labels, rotate date labels and add plot title
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45)
    plt.title(station.name)
    plt.tight_layout()  # This makes sure plot does not cut off date labels
    plt.legend()
    plt.show()


