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
    #cam_name = "3JUIL_Extracted_Data/"

    bb_temperatures_F = np.load(os.path.join(outputPath,"bb_temperatures_F_filt.npy"))
    baboon_temperatures_F = np.load(os.path.join(outputPath,"baboon_temperatures_F_filt.npy"))
    
    #video_temps_F = np.load(os.path.join(cam_name,"video_temps_F_filt.npy"))
   ## df = pd.DataFrame(bb_temperatures_F.astype(int))
   #df2 = pd.DataFrame(bb_temperatures_F.astype(int))
   # 
    bb_temperatures_F = bb_temperatures_F.astype(int)
    baboon_temperatures_F = baboon_temperatures_F.astype(int)

    # binList, binCount = getBins(bb_temperatures_F)
    # binList, binCount = getBins(baboon_temperatures_F)
    binList = np.linspace(74,100,26)

    #hist = df2.hist(bins = binCount)

    import pdb
    # pdb.set_trace()
    plt.hist(bb_temperatures_F, binList, alpha = 0.5, label = "All Animal Detections")
    # plt.hist(baboon_temperatures_F, binCount, alpha = 0.5, label = "Baboon Detections")
    plt.hist(baboon_temperatures_F, binList, alpha = 0.5, label = "Baboon Detections")

    # plt.xticks(binList)
    plt.title("Distribution of Animal Detections by Temperature")
    plt.xlabel("Temperature ($^\circ$F)")
    plt.ylabel("Frequency")
    plt.legend()

    plt.savefig(os.path.join(outputPath,"plot2.jpg"))
    #plt.show()


