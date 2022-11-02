import numpy as np
import cv2
import os
from CreateTemperatureLists import removeSpecialChars

'''Arguments take farenhight and celsius values. It converts the celsius values to farenheight and compares
the calculated values to the actual farenheight values. Returns an array with the index positions of all discrepencies.'''

def checkConversions(far, cel, names):
    errors = []
    tolerance = 2
    
    val = 0 

    for i in range(len(far)): #loops through ever farenheight value
        val = (float(cel[i]) * (9/5)) + 32 #formula to convert celsius to farenheight
        if (abs(val-float(far[i])) > tolerance): #if the difference between calculated and expected value is greater than tolerance, print error
            print(f"Error with {names[i]} (index {i}):,   C:{cel[i]},  Calculated F:{val:.2f}, Scanned F:{far[i]}")
            error = (names[i],i)
            errors.append(error)

    return errors

def main():
    cam_name = "3JUIL_Extracted_Data/"

    video_temps = np.load(os.path.join(cam_name,'video_temps.npy'))  #load file
    video_names = np.load(os.path.join(cam_name,'video_names.npy'))
    
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

    np.save(os.path.join(cam_name,'video_temps_C.npy'), video_temps_C)
    np.save(os.path.join(cam_name,'video_temps_F.npy'), video_temps_F)
    
    errors = checkConversions(video_temps_F,video_temps_C,video_names)
    
    np.save(os.path.join(cam_name,'errors.npy'), errors)
    
    




if __name__ == '__main__':
    main()



