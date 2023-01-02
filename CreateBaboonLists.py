import fnmatch
import os
import numpy as np
from CreateBBLists import getTemperatures

''' 
Function Name: makeBBlists(outputPath,bbFramePath)

Input Argument(s):
    1. outputPath - path to output folder
    2. baboonFramePath - path to folder containing bounding boxes 

Output Argument(s): (0 return arguments, just .npy save)
    1. baboon_temperatures_F - list of baboon bounding box temperatures in fahrenheit
    2. baboon_temperatures_C - list of baboon bounding box temperatures in celcius
    3. baboon_names - list of filenames of each bounding box

This function is very similar to makeBBlists() in CreateBBLists.py. It creates 2 new lists to store temperature values with 
index positions corresponding with the list of baboon filenames.
'''
def makeBaboonlists(outputPath,baboonFramePath):

    video_temps_C = np.load(os.path.join(outputPath,"video_temps_C.npy"))
    video_temps_F = np.load(os.path.join(outputPath,"video_temps_F.npy"))
    video_names = np.load(os.path.join(outputPath,"video_names.npy"))

    paths = baboonFramePath
    paths = fnmatch.filter(os.listdir(paths), "*.jpg")

    baboon_names = []  # intialize empty list to bounding box filenames

    for path in paths:
        filename = path.split('_')[0]
        baboon_names.append(filename)

    baboon_temperatures_F = getTemperatures(video_names, baboon_names, video_temps_F)
    baboon_temperatures_C = getTemperatures(video_names, baboon_names, video_temps_C)


    np.save(os.path.join(outputPath,"baboon_temperatures_F.npy"), baboon_temperatures_F)
    np.save(os.path.join(outputPath,"baboon_temperatures_C.npy"), baboon_temperatures_C)
    np.save(os.path.join(outputPath,"baboon_names.npy"), baboon_names)
    



