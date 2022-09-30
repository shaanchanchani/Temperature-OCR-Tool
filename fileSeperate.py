import glob
import fnmatch
import os
import numpy as np


paths = "./2021_3JUIL_7AOU_ANTENNE_CAM1806_CARTE8_747848_1442645"
files = fnmatch.filter(os.listdir(paths), "*1800.jpg")
video_names = []  # empty list of video file names
# fp = open('Somefile', 'w')
for image in files:
    # fp.write(image)
    video_name = image.split('_')[0]
    video_names.append(video_name)
    


np.save('SomeFile',video_names)
# fp.close()