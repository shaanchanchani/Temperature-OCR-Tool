import cv2
import numpy as np
import pytesseract
import glob

def main():
    paths = sorted(glob.glob('/Users/shaanchanchani/Desktop/VIP/VIPTest/data/videos/2021_3JUIL_7AOU_ANTENNE_CAM1806_CARTE8_747848_1442645/100EK113/*'))
    save_path = '/Users/shaanchanchani/Desktop/VIP/VIPTest/TemperatureExtraction/CapturedFrames/     '

    #https://www.geeksforgeeks.org/python-program-extract-frames-using-opencv/
    count = 1

    for path in paths:
        vid = cv2.VideoCapture(path)
        if not vid.isOpened():
            print("Could not open!")
        else:
            total_frames = int(vid.get(cv2.CAP_PROP_FRAME_COUNT))
            for i in range(total_frames):
                success = vid.grab()
                if (i == (total_frames-1)):
                    ret, image = vid.retrieve()
                    cv2.imwrite(save_path + "Frame"+ str(count) +".JPG",image)
                    count += 1 


if __name__ == '__main__':
    main()