import numpy as np
import matplotlib.pyplot as plt
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.plot import plot_water_levels, plot_water_level_with_fit
from floodsystem.analysis import polyfit    

def main():
    stations = build_station_list()
    update_water_levels(stations)





if __name__ == "__main__":
    main()