import cv2
import numpy as np
import pytesseract
import glob
import pdb

def cleanTempOutput(list):
    tempList = []
    for i in range(len(list)):
        temp = ''.join(filter(lambda x: x.isdigit(), list[i]))
        tempList.append(temp)
    return tempList

def main():
    crop_path = '/Users/shaanchanchani/Desktop/VIP/VIPTest/CroppedImages/'
    resize_path = '/Users/shaanchanchani/Desktop/VIP/VIPTest/ResizedImages/'
    blur_crop_path = '/Users/shaanchanchani/Desktop/VIP/VIPTest/BlurredCroppedImages/'
    blur_resize_path = '/Users/shaanchanchani/Desktop/VIP/VIPTest/BlurredResizedImages/'

    count = 0

    cropOutputList = []
    resizeOutputList = []
    blurCropOutputList = []
    blurResizeOutputList = []
    correctOutputList = [8931,8529,7624,7926,9333,9132,8328] 

    paths = sorted(glob.glob('/Users/shaanchanchani/Desktop/VIP/VIPTest/SevenFrames/*'))

    for path in paths:
        count += 1 #Keeps track of images for labeling image output files

        img = cv2.imread(path)

        startRow = img.shape[0]-40
        endRow = img.shape[0]

        startColumn = 400 
        endColumn = 600

        crop = img[startRow:endRow,startColumn:endColumn,:]
        
        h, w, _ = crop.shape
        resize = cv2.resize(crop, [3*w, 3*h]) #Resizes each crop by a scale factor of 3
        
        blurCrop = cv2.GaussianBlur(resize,(5,5), 0) #Applies a 5x5 kernel gaussian blur to the resized cropped images
        blurResize = cv2.GaussianBlur(resize,(5,5),0) 

        custom_config = r'--oem 3 --psm 6'
        
        #Scanning Raw Crops
        cropOutput = pytesseract.image_to_string(crop, config=custom_config)
        cropOutputList.append(cropOutput)

        #Scanning Resized Crops
        resizeOutput = pytesseract.image_to_string(resize, config=custom_config)
        resizeOutputList.append(resizeOutput)

        #Scanning Blurred Crops
        blurCropOutput = pytesseract.image_to_string(blurCrop, config=custom_config)
        blurCropOutputList.append(blurCropOutput)

        #Scanning Resized and Blurred Crops 
        blurResizeOutput = pytesseract.image_to_string(blurResize, config=custom_config)
        blurResizeOutputList.append(blurResizeOutput)

        #cv2.imwrite(crop_path + "Crop"+ str(count) +".JPG",crop)
        #cv2.imwrite(resize_path + "Resize"+ str(count) +".JPG",resize)
        #cv2.imwrite(blur_crop_path + "BlurCrop"+ str(count) +".JPG",blurCrop)
        #cv2.imwrite(blur_resize_path + "BlurResize"+ str(count) +".JPG",blurResize)
    
    cropOutputList = cleanTempOutput(cropOutputList)
    resizeOutputList = cleanTempOutput(resizeOutputList)
    blurCropOutputList = cleanTempOutput(blurCropOutputList)
    blurResizeOutputList = cleanTempOutput(blurResizeOutputList)

    np.save('cropOutputList.npy', cropOutputList)
    np.save('resizeOutputList.npy', resizeOutputList)
    np.save('blurCropOutputList.npy', blurCropOutputList)
    np.save('blurResizeOutputList.npy', blurResizeOutputList)

    testCrop = np.load('cropOutputList.npy')
    testResize = np.load('resizeOutputList.npy')
    testBlurC = np.load('blurCropOutputList.npy')
    testBlurR = np.load('blurResizeOutputList.npy')

    print("\nCorrect Output:\n")
    print(correctOutputList)
    print("\nOutput from raw crops:\n")
    print(testCrop)
    print("\nOutput from resized crops:\n")
    print(testResize)
    print("\nOutput from blurred crops:\n")
    print(testBlurC)
    print("\nOutput from blurred and resized crops:\n")
    print(testBlurR)



    

if __name__ == '__main__':
    main()