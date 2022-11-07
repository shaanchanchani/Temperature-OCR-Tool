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



def main():
    cam_name = "3JUIL_Extracted_Data/"

    bb_temperatures_F = np.load(os.path.join(cam_name,"bb_temperatures_F_filt.npy"))
    #video_temps_F = np.load(os.path.join(cam_name,"video_temps_F_filt.npy"))
    df = pd.DataFrame(bb_temperatures_F.astype(int))

    binList, binCount = getBins(bb_temperatures_F)

    hist = df.hist(bins = binCount)
    plt.xticks(binList)
    plt.title("Distribution of Animal Detections by Temperature")
    plt.xlabel("Temperature ($^\circ$F)")
    plt.ylabel("Frequency")
    plt.show()

if __name__ == '__main__':
    main()
