import glob
import cv2
import fnmatch
import os
import numpy as np
import pdb
import pytesseract
def extract_temp(image_path):
    img = cv2.imread(image_path)

    startRow = img.shape[0]-40
    endRow = img.shape[0]

    startColumn = 400 
    endColumn = 600

    cropIm = img[startRow:endRow,startColumn:endColumn,:]
    
    h, w, _ = cropIm.shape
    # resizedIm = cv2.resize(cropIm, [3*w, 3*h]) #Resizes each crop by a scale factor of 3
    
    blur_cropIm = cv2.GaussianBlur(cropIm,(5,5), 0) #Applies a 5x5 kernel gaussian blur to the resized cropped images
    # blur_resizedIm = cv2.GaussianBlur(resizedIm,(5,5),0) 

    custom_config = r'--oem 3 --psm 6'
    
    #Scanning Raw Crops
    blurCropOutput = pytesseract.image_to_string(blur_cropIm, config=custom_config)
    
    return(blurCropOutput)

if __name__ == '__main__':
    paths = "./data/frames/2021_3JUIL_7AOU_ANTENNE_CAM1806_CARTE8_747848_1442645"
    files = fnmatch.filter(os.listdir(paths), "*1800.jpg")
    video_names = []  # empty list of video file names
    video_temps = []  # empty list of temperatures per video
    # fp = open('Somefile', 'w')
    for image in files:
        # fp.write(image)
        video_name = image.split('_')[0]
        # pdb.set_trace()
        video_names.append(video_name)
        image_path = paths + '/' + image
        video_temps.append(extract_temp(image_path))
        
        


    np.save('video_names.npy',video_names)
    np.save('video_temps.npy',video_temps)
    # fp.close()