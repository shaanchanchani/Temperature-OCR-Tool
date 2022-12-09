import numpy as np
import cv2
import os

''' 
Function Name: checkConversions(far, cel, names)

Input Argument(s):
    far - list of fahrenheit values
    cel - list of celcius values 
    names - list of filenames 

Output Argument(s): 
    errors - list of errors (tuple)

This function starts by iterating through each element in the celcius and fahrenheit lists. It converts the celsius values to fahrenheit and
then compares the calculated values to the actual fahrenheit values. If it's within the set tolerance in the function (2 degrees), an error tuple is made 
with the first element being the filename where the bad read occurs and the second element being the index position of the bad read.
'''
def checkConversions(far, cel, names):
    errors = []
    tolerance = 2
    
    val = 0 

    for i in range(len(far)): #loops through ever fahrenheit value
        val = (float(cel[i]) * (9/5)) + 32 #formula to convert celsius to fahrenheit
        if(far[i] == ''): #'' would make the the float cast in the elif condition result in a value error
            print(f"Error with {names[i]} (index {i}):,   C:{cel[i]},  Calculated F:{val:.2f}, Scanned F:{far[i]}")
            error = (names[i],i)
            errors.append(error)
        elif (abs(val-float(far[i])) > tolerance): #if the difference between calculated and expected value is greater than tolerance, print error
                print(f"Error with {names[i]} (index {i}):,   C:{cel[i]},  Calculated F:{val:.2f}, Scanned F:{far[i]}")
                error = (names[i],i)
                errors.append(error)

    return errors

''' 
Function Name: removeSpecialChars(list)

Input Argument(s):
    list - each element is a string

Output Argument(s): 
    temperatureList - each element is a string 

Takes a list of strings, and returns the same list with everything but numbers removed.
'''

def removeSpecialChars(list):
    tempList = []
    for i in range(len(list)):
        temp = ''.join(filter(lambda x: x.isdigit(), list[i]))
        tempList.append(temp)
    return tempList

''' 
Function Name: seperateUnits(outputPath)

Input Argument(s):
    only takes 1 input arguement, however, loads 2 .npy files from outputPath folder
    outputPath - path to folder containing output data 
    video_temps.npy - list of temperatues containing values for both fahrenheit and celcius (string)
    video_names.npy - list of filenames (string)

Output Argument(s): 
   No return arguments, but 3 .npy list saves
    1. video_temps_C.npy - list of temperatures in celcius (string)
    2. video_temps_F.npy - list of temperatures in fahrenheit (string)
    3. errors.npy - list of errors (tuple)

This function iterates through each element in the list of temperatues and seperates the fahrenheit values from celcius.
It calls the checkConversions function to save a list of errors.
'''
def seperateUnits(outputPath):
    #cam_name = "7AOU_Extracted_Data/"
    video_temps = np.load(os.path.join(outputPath,'video_temps.npy'))  #load file
    video_names = np.load(os.path.join(outputPath,'video_names.npy'))
    
    video_temps_C = []
    video_temps_F = []
    
    arr = []
    errorList = []
    
    for i in range(len(video_temps)): #loops through video temperatures
        arr = video_temps[i].split('F',1) #seperates out the farenheight and celsius temp
        if(len(arr) > 1):
            video_temps_F.append(arr[0]) #adds farenheight to seperate list
            video_temps_C.append(arr[1])
        else:
            arr = video_temps[i].split(' ',1) #
            video_temps_F.append(arr[0])
            video_temps_C.append(arr[1])

    video_temps_C = removeSpecialChars(video_temps_C)
    video_temps_F = removeSpecialChars(video_temps_F)

    np.save(os.path.join(outputPath,'video_temps_C.npy'), video_temps_C)
    np.save(os.path.join(outputPath,'video_temps_F.npy'), video_temps_F)
    
    errors = checkConversions(video_temps_F,video_temps_C,video_names)

    np.save(os.path.join(outputPath,'errors.npy'), errors)
    
    



