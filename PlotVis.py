import fnmatch
import os
import numpy as np
import matplotlib.pyplot as plt 
import pandas as pd

def getBins(temperatures):
    temperatures = np.sort(temperatures.astype(int))
    binList = np.unique(temperatures)
    binCount = len(np.unique(temperatures))
    return binList, binCount

def generatePlots(outputPath):
    bb_temperatures_F = np.load(os.path.join(outputPath,"bb_temperatures_F.npy"))
    #baboon_temperatures_F = np.load(os.path.join(outputPath,"baboon_temperatures_F_filt.npy"))
    

    bb_temperatures_F = bb_temperatures_F.astype(int)
    #baboon_temperatures_F = baboon_temperatures_F.astype(int)

    # binList, binCount = getBins(bb_temperatures_F)
    # binList, binCount = getBins(baboon_temperatures_F)
    binList = np.linspace(74,100,26)

    plt.hist(bb_temperatures_F, binList, alpha = 0.5, label = "All Animal Detections")
    #plt.hist(baboon_temperatures_F, binList, alpha = 0.5, label = "Baboon Detections")

    plt.title("Distribution of Animal Detections by Temperature")
    plt.xlabel("Temperature ($^\circ$F)")
    plt.ylabel("Frequency")
    #plt.legend()

    # plotName = "_AnimalDetections_Temperature_plot.jpg"
    # outputFilename = outputPath + plotName
    
    plt.savefig(os.path.join(outputPath,"AnimalDetections_Temperature_plot.jpg"))

