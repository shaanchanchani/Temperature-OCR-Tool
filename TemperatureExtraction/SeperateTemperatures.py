import numpy as np
from CreateTemperatureLists import removeSpecialChars
'''Arguments take farenhight and celsius values. It converts the celsius values to farenheight and compares
the calculated values to the actual farenheight values'''
def checkConversions(far, cel):
    tolerance = 1
    val = 0 
    for i in range(len(far)): #loops through ever farenheight value
        val = (float(cel[i]) * (9/5)) + 32 #formula to convert celsius to farenheight
        if (abs(val-float(far[i])) > tolerance): #if the difference between calculated and expected value is greater than tolerance, print error
            print(f"Error {i}:,   C:{cel[i]},   Expected F:{far[i]},   Calculated F:{val:.2f}")

def main():
    video_temps = np.load('video_temps.npy')#load file
    
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

    video_temps_C = removeSpecialChars(video_temps_C)
    video_temps_F = removeSpecialChars(video_temps_F)

    checkConversions(video_temps_F,video_temps_C)




if __name__ == '__main__':
    main()