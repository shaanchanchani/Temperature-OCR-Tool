from TemperatureExtraction.CreateTemperatureLists import makeTemperatureList 
from TemperatureExtraction.SeperateTemperatures import seperateUnits
from BoundingBoxTemperatureVisualization.CreateBBFilenameList import makeBBlists
from BoundingBoxTemperatureVisualization.PlotVis import generatePlots

def main():
    cam_num = int(input("Enter '1' for cam 1 or '2' for cam 2: "))

    if (cam_num == 1):
        framePaths = "./data/frames/2021_3JUIL_7AOU_ANTENNE_CAM1806_CARTE8_747848_1442645"
        outputPath = "3JUIL_Extracted_Data/"
        bbFramePath = "./data/bbs/2021_3JUIL_7AOU_ANTENNE_CAM1806_CARTE8_747848_1442645"

    elif (cam_num == 2):
        framePaths = "./data/frames/2021_7AOU_11SEP_ANTENNE_CAM1806_CARTE1806_747491_1442649"
        outputPath = "7AOU_Extracted_Data/"
        bbFramePath = "./data/bbs/2021_7AOU_11SEP_ANTENNE_CAM1806_CARTE1806_747491_1442649"

    makeTemperatureList(framePaths,outputPath)
    seperateUnits(outputPath)
    makeBBlists(outputPath,bbFramePath)
    generatePlots(outputPath)



if __name__ == '__main__':
    main()
