import glob
import cv2
import fnmatch
import os
import numpy as np
import pdb
import pytesseract

''' 
 In PytesseractTesting.py, we found that applying a Gaussian blur to our images before feeding them to
 Pytesseract generates a more accurate output. The following function takes an image path as an input and
 starts by cropping the image at the location of the path down to only its temperature values. The temperature 
 values are located at the same position in each frame so we were able to hard-code the dimensions of our crop. 
 Next, the function utilizes cv2's Gaussian blur method to apply a 5x5 kernel blur to the crop. Finally, the 
 blurred-crop is sent to Pytessaract's image to string method (the OCR) and the function returns the output.
'''  
def extract_temperature(image_path):
    img = cv2.imread(image_path)
    if (img.size == 0): #cv2's documentation for imread() specifies that an empty matrix is returned on error.
        return 0 #If our function detects an empty matrix it'll return false.

    else:
        startRow = img.shape[0]-40 #Hard-coded variables to retrieve bottom 40 rows
        endRow = img.shape[0]

        startColumn = 400 #Hard-coded variables to retrieve columns 400-600 
        endColumn = 600

        cropIm = img[startRow:endRow,startColumn:endColumn,:] #Crops frame using hard-coded variables

        blur_cropIm = cv2.GaussianBlur(cropIm,(5,5), 0) #Applies a 5x5 kernel gaussian blur 

        custom_config = r'--oem 3 --psm 6'
        blurCropOutput = pytesseract.image_to_string(blur_cropIm, config=custom_config)
    
    return(blurCropOutput)

'''
Function copied from PytessaractTesting.py. Takes a list as an input, and returns the same list with 
all special characters filtered out of each element.
'''
def removeSpecialChars(list):
    tempList = []
    for i in range(len(list)):
        temp = ''.join(filter(lambda x: x.isdigit(), list[i]))
        tempList.append(temp)
    return tempList

def main():
    cam_name = "3JUIL_Extracted_Data/"

    paths = "./data/frames/2021_3JUIL_7AOU_ANTENNE_CAM1806_CARTE8_747848_1442645"
    files = fnmatch.filter(os.listdir(paths), "*1800.jpg")

    video_names = []  # empty list of video file names
    video_temps = []  # empty list of temperatures per video

    for image in files:
        video_name = image.split('_')[0]
        video_names.append(video_name)

        image_path = paths + '/' + image
        if(extract_temperature(image_path)): 
            video_temps.append(extract_temperature(image_path)) #Executes as long as our function does not return false for that frame
    
    np.save(os.path.join(cam_name,'video_names.npy'),video_names)
    np.save(os.path.join(cam_name,'video_temps.npy'),video_temps)

    



if __name__ == '__main__':
    main()
