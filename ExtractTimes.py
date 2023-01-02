import json
import os
import numpy
import numpy as np
import matplotlib.pyplot as plt 
import pandas as pd
#This file imports and processes time data for each camera trigger that is stored in the json file. This data is then extracted
#from the json and matched with the actual temperature values for each time which is then graphed.
def main():
    f = open("C:\\Users\\krish\\Downloads\\2021_3JUIL_7AOU_ANTENNE_CAM1806_CARTE8_747848_1442645.json")
    data = json.load(f)
    #extracts video names from json into python list and same thing for hours data
    names = data['video_names']
    times = data['hours']
    #imports names of videos into python list
    extractNames = numpy.load("C:\\Users\\krish\\Downloads\\video_names.npy")
    extractTemps = numpy.load("C:\\Users\\krish\\Downloads\\video_temps.npy")

    #loops through names and removes the '.MP4' for each name using the .split() function
    Nsplits = []
    for name in names:
        name = name.split(".MP4")[0]
        Nsplits.append(name)

    #finds matches where the json file names match the imported file names and adds the times that correspond to that match
    hours = []
    for i in range(len(extractNames)):
        for j in range(len(Nsplits)):
            if extractNames[i] == Nsplits[j]:
                hours.append(int(times[j]))
    #
    tempF = numpy.load("C:\\Users\\krish\\Downloads\\video_temps_F.npy")
    temps = []
    #casts all the temperature values into integer from the numpy file
    for temp in tempF:
        temps.append(int(temp))
    
    #removes large outliers for temperature values
    i = 0
    for temp in temps:
        i+=0
        if temp > 150:
            temps.remove(temp)
            hours.remove(hours[i])
    #removes smaller temperature outliers
    j = 0
    for temp in temps:
        j+=0
        if temp < 50:
            temps.remove(temp)
            hours.remove(hours[i])

    #graph temperature values over the hours
    plt.scatter(hours, temps)
    plt.xticks(hours)
    plt.xlabel("Hours during the day")
    plt.ylabel("Temperature in Farenheight for each hour")
    plt.show()       

if __name__ == '__main__':
    main()