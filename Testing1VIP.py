import cv2
import numpy as np
import pytesseract
import glob

def main():
    #Opens filIPe and erases content 
    #file = open("extractedText.txt", "w+")
    #file.write("")
    #file.close()
    src_path = '/Users/shaanchanchani/Desktop/VIP/VIPTest/TenFrames/'
    count = 0
    paths = sorted(glob.glob('/Users/shaanchanchani/Desktop/VIP/VIPTest/TenFrames/*'))
    for path in paths:
        count += 1
        img = cv2.imread(path)
        startRow = img.shape[0]-40
        endRow = img.shape[0]
        startColumn = 400 
        endColumn = 600
        crop = img[startRow:endRow,startColumn:endColumn,:]
        h, w, _ = crop.shape
        crop2 = cv2.resize(crop, [3*w, 3*h])
        custom_config = r'--oem 3 --psm 6'
        text = pytesseract.image_to_string(crop, config=custom_config)
        print(text)
        cv2.imwrite(src_path + "Crop"+ str(count) +".JPG",crop2)
    # file = open("extractedText.txt", "a")
    # file.write(text)
    # file.write("\n")
    # file.close 

if __name__ == '__main__':
    main()