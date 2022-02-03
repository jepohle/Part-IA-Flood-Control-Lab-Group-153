import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import numpy as np

from floodsystem.datafetcher import fetch_measure_levels

def plot_water_levels(station, dates, level):


    """function that plots the absolute water level as a function of the station, dates and correcponding water levels"""
    # Plot
    print(np.full((1,10), 1).tolist())
    plt.plot(dates, level)
    plt.plot(dates, np.full(len(dates), station.typical_range[0]).tolist())
    plt.plot(dates, np.full(len(dates), station.typical_range[1]).tolist())


    # Add axis labels, rotate date labels and add plot title
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45)
    plt.title(station.name)

    # Display plot
    plt.tight_layout()  # This makes sure plot does not cut off date labels

    plt.show()