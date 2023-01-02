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
Function Name: keepOnlyDigits(list)

Input Argument(s):
    list - each element is a string

Output Argument(s): 
    temperatureList - each element is a string 

Takes a list of strings, and returns the same list with everything but numbers removed.
'''

def keepOnlyDigits(list):
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
    
    for i in range(len(video_temps)): #loops through video temperatures
        arr = video_temps[i].split('F',1) #seperates out the farenheight and celsius temp
        if(len(arr) > 1):
            video_temps_F.append(arr[0]) #adds farenheight to seperate list
            video_temps_C.append(arr[1])
        else:
            arr = video_temps[i].split(' ',1) #
            video_temps_F.append(arr[0])
            video_temps_C.append(arr[1])

    video_temps_C = keepOnlyDigits(video_temps_C)
    video_temps_F = keepOnlyDigits(video_temps_F)

    '''
    Hard-coded corrections for Camera Site 1:

    Output from checkConversions()
        Error with 07120039 (index 36):,   C:27,  Calculated F:80.60, Scanned F:2
        Error with 07030003 (index 41):,   C:34,  Calculated F:93.20, Scanned F:4
        Error with 08040100 (index 45):,   C:34,  Calculated F:93.20, Scanned F:4
        Error with 07130041 (index 55):,   C:35,  Calculated F:95.00, Scanned F:6
        Error with 08020095 (index 57):,   C:42,  Calculated F:107.60, Scanned F:08
        Error with 08020094 (index 58):,   C:41,  Calculated F:105.80, Scanned F:06
        Error with 07260071 (index 59):,   C:28,  Calculated F:82.40, Scanned F:4
        Error with 07290081 (index 61):,   C:36,  Calculated F:96.80, Scanned F:07
        Error with 07120040 (index 63):,   C:35,  Calculated F:95.00, Scanned F:5
        Error with 07290078 (index 69):,   C:35,  Calculated F:95.00, Scanned F:5
        Error with 07250069 (index 81):,   C:32,  Calculated F:89.60, Scanned F:0
    '''
    if outputPath == "3JUIL_Extracted_Data/":
        video_temps_F[36] = 82
        video_temps_F[41] = 94
        video_temps_F[45] = 94
        video_temps_F[55] = 96
        video_temps_F[57] = 108
        video_temps_F[58] = 106
        video_temps_F[59] = 84
        video_temps_F[61] = 97
        video_temps_F[63] = 95
        video_temps_F[69] = 95
        video_temps_F[81] = 90



    '''
    Hard-coded correction for Camera Site 2:

    Output from checkConversions()
        Error with 09010027 (index 32):,   C:23,  Calculated F:73.40, Scanned F:

    This error was due to a bad read from the OCR. 74 was scanned as 'TA'.
    After keepOnlyDigits() was called it became ' ' because there were no digits to keep.
    '''
    if outputPath == "7AOU_Extracted_Data/":
        video_temps_F[32] = 74


    np.save(os.path.join(outputPath,'video_temps_C.npy'), video_temps_C)
    np.save(os.path.join(outputPath,'video_temps_F.npy'), video_temps_F)
    
    errors = checkConversions(video_temps_F,video_temps_C,video_names)

    np.save(os.path.join(outputPath,'errors.npy'), errors)
    
    



