import fnmatch
import os
import numpy as np

''' 
Function Name: getTemperatures(video_names, bb_names, temperatures)

Input Argument(s):
    1. video_names - list of filenames corresponding to the temperature lists
    2. bb_names - list of filenames of each bounding box
    3. temperatures - temperatures

Output Argument(s): 
    bb_temperatures - list of temperatures that corresponds with the bb_names index positions

This function iterates through each element in the list of bounding box filenames and each element of the 
list of video filenames. If a match between two elements is found, the value at the index position in the temperature list
is added to the output list.
'''
def getTemperatures(video_names, bb_names, temperatures):
    #Initialize new list to return temperature values 
    bb_temperatures = []
    
    for i in range(len(bb_names)): #Iterates through each name in list of Bounding Box names
        for j in range(len(video_names)): #Iterates through each name in list of video names
            #Find the index position in video names list that matches BB name. Add the value at that index position in the temperature
            # list to return list.
            if ((bb_names[i]) == (video_names[j])): 
                bb_temperatures.append(temperatures[j])         
            
    return bb_temperatures


''' 
Function Name: makeBBlists(outputPath,bbFramePath)

Input Argument(s):
    1. outputPath - path to output folder
    2. bbFramePath - path to folder containing bounding boxes 

Output Argument(s): (0 return arguments, just .npy save)
    1. bb_temperatures_F - list of bounding box temperatures in fahrenheit
    2. bb_temperatures_C - list of bounding box temperatures in celcius
    3. bb_names - list of filenames of each bounding box

This function creates 2 new lists to store temperature values with index positions corresponding
with the list of bounding box filenames.
'''
def makeBBlists(outputPath,bbFramePath):
    
    video_temps_C = np.load(os.path.join(outputPath,"video_temps_C.npy"))
    video_temps_F = np.load(os.path.join(outputPath,"video_temps_F.npy"))
    video_names = np.load(os.path.join(outputPath,"video_names.npy"))

    paths = bbFramePath
    paths = fnmatch.filter(os.listdir(paths), "*.jpg")

    bb_names = []  # intialize empty list to bounding box filenames

    for path in paths:
        filename = path.split('_')[0]
        bb_names.append(filename)

    bb_temperatures_F = getTemperatures(video_names, bb_names, video_temps_F)
    bb_temperatures_C = getTemperatures(video_names, bb_names, video_temps_C)


    np.save(os.path.join(outputPath,"bb_temperatures_F.npy"), bb_temperatures_F)
    np.save(os.path.join(outputPath,"bb_temperatures_C.npy"), bb_temperatures_C)
    np.save(os.path.join(outputPath,"bb_names.npy"), bb_names)
    
    # np.save(os.path.join(outputPath,"baboon_names_filt.npy"), bb_names)


''' 
Function Name: filterErrors(video_names,bb_names,errors,video_temps_C,video_temps_F)

Input Argument(s):
    1. video_temps_C - list of temperatures in celcius (string)
    2. video_temps_F - list of temperatures in fahrenheit (string)
    3. video_names - list of filenames corresponding to the temperature lists
    4. bb_names - list of filenames of each bounding box
    5. errors - list of error tuples 

Output Argument(s): 
    1. video_temps_C2 - list of filtered temperatures in celcius (string)
    2. video_temps_F2 - list of filtered temperatures in fahrenheit (string)
    3. video_names2 - list of filtered filenames corresponding to the temperature lists
    4. bb_names2 - list of filtered filenames of each bounding box

This function iterates through each element in each input lists and filters out the values 
from our list of error tuples.
'''
def filterErrors(video_names,bb_names,errors,video_temps_C, video_temps_F):
    #Split Error Tuple list
    error_names = [error[0] for error in errors] #Creates list of error names by grabbing first element from each tuple in error tuple list
    error_indicies = [error[1] for error in errors] #Creates list of error indicies by grabbing second element

    #Initialize empty arrays to hold filtered lists 
    bb_names2 = []
    video_names2 = []
    video_temps_C2 = []
    video_temps_F2 = []

    for i in range(len(bb_names)): #Iterates through each name in list of Bounding Box names
        check = 0 
        for name in error_names: #Iterates through each name in list of error names
            if (bb_names[i] == name): #If current BB name matches any of the error names
                check = 1 #Set check to 1
        if (check == 0): #If check is still 0 after comparing current BB name with all error names
            bb_names2.append(bb_names[i]) #add BB name to filtered return list

    for i in range(len(video_names)):
        check = 0 
        for name in error_names:
            if (video_names[i] == name):
                check = 1
        if (check == 0):
            video_names2.append(video_names[i])
            video_temps_F2.append(video_temps_F[i])
            video_temps_C2.append(video_temps_C[i])

    return video_names2, bb_names2, video_temps_C2, video_temps_F2
