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

def generate_AnimalDetection_Temperature_plot(outputPath):
    plt.clf() 
    bb_temperatures_F = np.load(os.path.join(outputPath,"bb_temperatures_F.npy"))
    bb_temperatures_F = bb_temperatures_F.astype(int)

    # binList, binCount = getBins(bb_temperatures_F)
    # binList, binCount = getBins(baboon_temperatures_F)
    binList = np.linspace(74,100,26)

    plt.hist(bb_temperatures_F, binList, alpha = 0.5, label = "All Animal Detections")

    plt.title("Distribution of Animal Detections by Temperature")
    plt.xlabel("Temperature ($^\circ$F)")
    plt.ylabel("Frequency")
    
    plt.savefig(os.path.join(outputPath,"AnimalDetections_Temperature_plot.jpg"))

def generate_Baboon_Temperature_plot(outputPath):
    plt.clf() 
    baboon_temperatures_F = np.load(os.path.join(outputPath,"baboon_temperatures_F.npy"))
    baboon_temperatures_F = baboon_temperatures_F.astype(int)

    binList = np.linspace(74,100,26)
    plt.hist(baboon_temperatures_F, binList, alpha = 0.5, label = "Baboon Detections")

    plt.title("Distribution of Baboon Detections by Temperature")
    plt.xlabel("Temperature ($^\circ$F)")
    plt.ylabel("Frequency")

    plt.savefig(os.path.join(outputPath,"Baboon_Temperature_plot.jpg"))

def generate_AnimalDectections_Baboon_Temperature_plot(outputPath):
    plt.clf() 
    bb_temperatures_F = np.load(os.path.join(outputPath,"bb_temperatures_F.npy"))
    baboon_temperatures_F = np.load(os.path.join(outputPath,"baboon_temperatures_F.npy"))

    bb_temperatures_F = bb_temperatures_F.astype(int)
    baboon_temperatures_F = baboon_temperatures_F.astype(int)

    binList = np.linspace(74,100,26)

    plt.hist(bb_temperatures_F, binList, alpha = 0.5, label = "All Animal Detections")
    plt.hist(baboon_temperatures_F, binList, alpha = 0.5, label = "Baboon Detections")

    plt.title("Distribution of Animal Detections by Temperature")
    plt.xlabel("Temperature ($^\circ$F)")
    plt.ylabel("Frequency")
    plt.legend()

    plt.savefig(os.path.join(outputPath,"AnimalDetections_Baboon_Temperature_plot.jpg"))
