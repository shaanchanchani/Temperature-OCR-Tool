# OCR Calibration

## PytesseractTesting.py
In this file we explore how Pytesseract, an Optical Character Recognition tool, responds to scanning images from our dataset. Using various combinations of standard image data preprocessing techniques (Gaussian Blur, Image Resizing, and Cropping), we scanned a sample dataset and evaluated the accuracy of each trial.

# Temperature Extraction:

## CreateTemperatureLists.py
`extract_temperature(image_path)`
 In PytesseractTesting.py, we found that applying a Gaussian blur to our images before feeding them to
 Pytesseract generates a more accurate output. The following function takes an image path as an input and
 starts by cropping the image at the location of the path down to only its temperature values. The temperature 
 values are located at the same position in each frame so we were able to hard-code the dimensions of our crop. 
 Next, the function utilizes cv2's Gaussian blur method to apply a 5x5 kernel blur to the crop. Finally, the 
 blurred-crop is sent to Pytessaract's image to string method (the OCR) and the function returns the output as a string.

`makeTemperatureList(inputPaths,outputPath)`
This function starts by iterating through each image in our list of input paths.
At each image, the filename is appended to a list and the extract_temperature() 
function is called to append the image's temperature.

## SeperateTemperatures.py
`seperateUnits(outputPath)`
This function iterates through each element in the list of temperatues and seperates the fahrenheit values from celcius.
It calls the checkConversions function to save a list of errors.

`removeSpecialChars(list)`
Takes a list of strings, and returns the same list with everything but numbers removed.

`checkConversions(far, cel, names)`
This function starts by iterating through each element in the celcius and fahrenheit lists. It converts the celsius values to fahrenheit and then compares the calculated values to the actual fahrenheit values. If it's within the set tolerance in the function (2 degrees), an error tuple is made with the first element being the filename where the bad read occurs and the second element being the index position of the bad read.

# Bounding Box Temperature Visualization

## CreateBBFilenameList.py
`filterErrors(video_names,bb_names,errors,video_temps_C,video_temps_F)`
This function iterates through each element in each input lists and filters out the values from our list of error tuples.

`getTemperatures(video_names, bb_names, temperatures)`
This function iterates through each element in the list of bounding box filenames and each element of the list of video filenames. If a match between two elements is found, the value at the index position in the temperature list is added to the output list.

