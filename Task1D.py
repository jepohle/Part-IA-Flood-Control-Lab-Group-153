from floodsystem.geo import rivers_with_station
from floodsystem.stationdata import build_station_list
from floodsystem.utils import sorted_by_key
from floodsystem.geo import stations_by_river

def run():
    """Prints the number of rivers that have a monitoring station and the first ten rivers in alphabetical order. Also prints the names of stations
    located along rivers: River Aire, River Cam, River Thames"""

    stations = build_station_list()                                                     #build list of stations used in this task
    rivers = rivers_with_station(stations)                                              #use river_with_stations function to create set of rivers
    riversorted = sorted(rivers)                                                                       #sort the set which has just been created
    print (len(riversorted),'rivers with stations. First 10 rivers - ', riversorted[:10])        #print the length of the set and the first 10 values in the set
    print()

    river_stations = stations_by_river(stations)                                        #use stations_by_river function to create a dictionary of stations by name
    Aireobject = river_stations['River Aire']                                           #create a list of the station objects at the Aire, Cam and Thames
    Camobject = river_stations['River Cam']
    FatherThamesobject = river_stations['River Thames']
    Aire =[stations.name for stations in Aireobject]                                    #Create empty list for the names
    Cam = [stations.name for stations in Camobject]
    FatherThames = [stations.name for stations in FatherThamesobject]

    Aire.sort()                                                                         #Sort and print the list of station names
    Cam.sort()
    FatherThames.sort()
    print('River Aire: ', Aire)
    print()
    print('River Cam: ', Cam)
    print()
    print('River Thames: ', FatherThames)




if __name__ == "__main__":
    print("*** Task 1D: CUED Part IA Flood Warning System ***")
    run()