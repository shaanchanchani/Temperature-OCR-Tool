import fnmatch
import os
import numpy as np

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

def getTemperatures(video_names, bb_names, temperatures):
    #Initialize new list to return temperature values 
    bb_temperatures = []

    for i in range(len(bb_names)): #Iterates through each name in list of Bounding Box names
        for j in range(len(video_names)): #Iterates through each name in list of video names
            #Find the index position in video names list that matches BB name. Add the value at that index position in the temperature
            # list to return list.
            if (int(bb_names[i]) == int(video_names[j])): 
                bb_temperatures.append(temperatures[j]) 

    return bb_temperatures

def main():
    errors = np.load("errors.npy")
    video_temps_C = np.load("video_temps_C.npy")
    video_temps_F = np.load("video_temps_F.npy")
    video_names = np.load("video_names.npy")

    paths = "./data/bbs/2021_3JUIL_7AOU_ANTENNE_CAM1806_CARTE8_747848_1442645"
    paths = fnmatch.filter(os.listdir(paths), "*.jpg")

    bb_names = []  # intialize empty list to bounding box filenames

    for path in paths:
        filename = path.split('_')[0]
        bb_names.append(filename)

    print(f"Number of errors: {len(errors)}")
    print(f"BB Names before filter: {len(bb_names)}")
    print(f"Celsius Temps before filter: {len(video_temps_C)}")
    print(f"Far Temps before filter: {len(video_temps_F)}")
    print(f"Vid Names before filter: {len(video_names)}")
    print()
        
    video_names2, bb_names2, video_temps_C2, video_temps_F2 = filterErrors(video_names, bb_names, errors, video_temps_C, video_temps_F)
    
    print()
    print(f"BB Names after filter: {len(bb_names2)}")
    print(f"Celsius Temps after filter: {len(video_temps_C2)}")
    print(f"Far Temps after filter: {len(video_temps_F2)}")
    print(f"Vid Names after filter: {len(video_names2)}")

    bb_temperatures = []
    bb_temperatures_F = getTemperatures(video_names2, bb_names2, video_temps_F2)
    bb_temperatures_C = getTemperatures(video_names2, bb_names2, video_temps_C2)

    print(f"Found BB Cel values: {len(bb_temperatures_C)}")
    print(f"Found BB Far values: {len(bb_temperatures_F)}")

    np.save("bb_temperatures_F_filt.npy", bb_temperatures_F)
    np.save("bb_temperatures_C_filt.npy", bb_temperatures_C)








if __name__ == '__main__':
    main()
