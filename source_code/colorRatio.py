from __future__ import print_function
import imutils
import cv2
import numpy

import pkgutil
import sys

from funcs.func_closestColor import *
from funcs.func_findPattern import *
from funcs.func_getColorRatio import *


TEST_PATH= "test_images/"
DOWNLOAD_PATH = "download/"

DELTA = 0.5 # color ratio range
nLargest = 3 # number of dominant colors

originPic = cv2.imread(DOWNLOAD_PATH+"sports_blue.jpeg") # 1327*400
smallOrg = cv2.resize(originPic, (0,0), fx=0.1, fy=0.1)  # 133*40

testPic = cv2.imread(TEST_PATH+"test_sunscreen.png")     # 871, 1298
smallTest = cv2.resize(testPic, (0,0), fx=0.2, fy=0.2)

func_findPattern(smallOrg, smallTest, DELTA, nLargest)
