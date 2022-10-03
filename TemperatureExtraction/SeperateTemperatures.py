import numpy as np
from CreateTemperatureLists import removeSpecialChars

def checkConversions(far, cel):
    val = 0 
    for i in range(len(far)):
        val = (float(cel[i]) * (9/5)) + 32
        if (abs(val-float(far[i])) > 2):
            print(f"Error {i}:,   C:{cel[i]},   Expected F:{far[i]},   Calculated F:{val:.2f}")

def main():
    video_temps = np.load('video_temps.npy')
    
    video_temps_C = []
    video_temps_F = []
    
    arr = []
    
    for i in range(len(video_temps)):
        arr = video_temps[i].split('F',1)
        if(len(arr) > 1):
            video_temps_F.append(arr[0])
            video_temps_C.append(arr[1])
        else:
            arr = video_temps[i].split(' ',1)
            video_temps_F.append(arr[0])
            video_temps_C.append(arr[1])

    video_temps_C = removeSpecialChars(video_temps_C)
    video_temps_F = removeSpecialChars(video_temps_F)

    checkConversions(video_temps_F,video_temps_C)




if __name__ == '__main__':
    main()
