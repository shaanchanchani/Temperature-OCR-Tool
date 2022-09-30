import cv2
import numpy as np
import pytesseract
import glob
import pdb

def removeSpecialChars(list):
    tempList = []
    for i in range(len(list)):
        temp = ''.join(filter(lambda x: x.isdigit(), list[i]))
        tempList.append(temp)
    return tempList

def main():
    crop_path = '/Users/shaanchanchani/Desktop/VIP/VIPTest/OCRCalibration/CroppedImages/'
    resize_path = '/Users/shaanchanchani/Desktop/VIP/VIPTest/OCRCalibration/ResizedImages/'
    blur_crop_path = '/Users/shaanchanchani/Desktop/VIP/VIPTest/OCRCalibration/BlurredCroppedImages/'
    blur_resized_path = '/Users/shaanchanchani/Desktop/VIP/VIPTest/OCRCalibration/BlurredResizedImages/'

    count = 0

    crop_OutputList = []
    resized_OutputList = []
    blur_crop_OutputList = []
    blur_resized_OutputList = []
    
    expected_OutputList = [8931,8529,7624,7926,9333,9132,8328] 

    paths = sorted(glob.glob('/Users/shaanchanchani/Desktop/VIP/VIPTest/OCRCalibration/SevenFrames/*'))

    for path in paths:
        count += 1 #Keeps track of images for labeling image output files

        img = cv2.imread(path)

        startRow = img.shape[0]-40
        endRow = img.shape[0]

        startColumn = 400 
        endColumn = 600

        cropIm = img[startRow:endRow,startColumn:endColumn,:]
        
        h, w, _ = cropIm.shape
        resizedIm = cv2.resize(cropIm, [3*w, 3*h]) #Resizes each crop by a scale factor of 3
        
        blur_cropIm = cv2.GaussianBlur(cropIm,(5,5), 0) #Applies a 5x5 kernel gaussian blur to the resized cropped images
        blur_resizedIm = cv2.GaussianBlur(resizedIm,(5,5),0) 

        custom_config = r'--oem 3 --psm 6'
        
        #Scanning Raw Crops
        cropOutput = pytesseract.image_to_string(cropIm, config=custom_config)
        crop_OutputList.append(cropOutput)

        #Scanning Resized Crops
        resizedOutput = pytesseract.image_to_string(resizedIm, config=custom_config)
        resized_OutputList.append(resizedOutput)

        #Scanning Blurred Crops
        blurCropOutput = pytesseract.image_to_string(blur_cropIm, config=custom_config)
        blur_crop_OutputList.append(blurCropOutput)

        #Scanning Resized and Blurred Crops 
        blurResizeOutput = pytesseract.image_to_string(blur_resizedIm, config=custom_config)
        blur_resized_OutputList.append(blurResizeOutput)

        cv2.imwrite(crop_path + "Crop"+ str(count) +".JPG",cropIm)
        cv2.imwrite(resize_path + "Resize"+ str(count) +".JPG",resizedIm)
        cv2.imwrite(blur_crop_path + "BlurCrop"+ str(count) +".JPG",blur_cropIm)
        cv2.imwrite(blur_resized_path + "BlurResized"+ str(count) +".JPG",blur_resizedIm)
    
    crop_OutputList = removeSpecialChars(crop_OutputList)
    resized_OutputList = removeSpecialChars(resized_OutputList)
    blur_crop_OutputList = removeSpecialChars(blur_crop_OutputList)
    blur_resized_OutputList = removeSpecialChars(blur_resized_OutputList)

    np.save('crop_OutputList.npy', crop_OutputList)
    np.save('resized_OutputList.npy', resized_OutputList)
    np.save('blur_crop_OutputList.npy', blur_crop_OutputList)
    np.save('blur_resized_OutputList.npy', blur_resized_OutputList)

    testCrop = np.load('crop_OutputList.npy')
    testResize = np.load('resized_OutputList.npy')
    testBlurC = np.load('blur_crop_OutputList.npy')
    testBlurR = np.load('blur_resized_OutputList.npy')

    print("\nCorrect Output:\n")
    print(expected_OutputList)
    print("\nOutput from raw crops:\n")
    print(testCrop)
    print("\nOutput from resized crops:\n")
    print(testResize)
    print("\nOutput from blurred crops:\n")
    print(testBlurC)
    print("\nOutput from blurred and resized crops:\n")
    print(testBlurR)


'''
Correct Output:

[8931, 8529, 7624, 7926, 9333, 9132, 8328]

Output from raw crops:

['8931' '8529' '7624' '7926' '9333' '9132' '8398']

Output from resized crops:

['8934' '8529' '' '1926' '9333' '0132' '8398']

Output from blurred crops:

['8931' '8529' '7624' '7926' '9333' '9432' '8328']
'''



    

if __name__ == '__main__':
    main()