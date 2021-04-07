# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 10:06:58 2021

@author: Sebastien
"""

import pandas as pd
import numpy as np
import cv2
import matplotlib.pyplot as plt


########## Import data ##########

data_folder = 'C:/Users/Sebastien/Documents/Semi BACKUP Laptop 08.01.20/Documents/4. Master/3rd Quarter/Autonomous MAV/Individual assignment/WashingtonOBRace/'
image_prefix = 'image_'
mask_prefix = 'mask_'
image_type = '.png'
mask_type = '.png'


image_nr = 164
mask_nr = 164

im_loc = data_folder+image_prefix+str(image_nr)+image_type
ma_loc = data_folder+mask_prefix+str(mask_nr)+mask_type


columns = ['Image','x_top_left','y_top_left','x_top_right','y_top_right','x_bottom_right','y_bottom_right','x_bottom_left','y_bottom_left']
corners = pd.read_csv(data_folder+'corners.csv', header=None, names=columns)

data = {}

for index, row in corners.iterrows():
    if row[0] in data:
        data[row[0]] = [data[row[0]],[(row[1],row[2]),(row[3],row[4]),(row[5],row[6]),(row[7],row[8])]]
    else:
        data[row[0]] = [(row[1],row[2]),(row[3],row[4]),(row[5],row[6]),(row[7],row[8])]


##########  ##########

##########  ##########

##########  ##########

