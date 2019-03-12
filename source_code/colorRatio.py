from __future__ import print_function
import imutils
import cv2
import numpy

import pkgutil
import sys

from funcs.func_findWindow import *
from funcs.func_clusterPixels import *
from funcs.func_fastClustering import *


TEST_PATH= "test_images/"
DOWNLOAD_PATH = "download/"

DELTA = 0.2 # color ratio range
nLargest = 3 # number of dominant colors

originPic = cv2.imread(DOWNLOAD_PATH+"sports_blue.jpeg") # 1327*400
originPic = cv2.resize(originPic, (0,0), fx=0.25, fy=0.25)
testPic = cv2.imread(TEST_PATH+"test_sunscreen.png")     # 871*1298
testPic = cv2.resize(testPic, (0,0), fx=0.25, fy=0.25)

patternModel,centroids, domainRatio = func_clusterPixels(originPic, nLargest)  # 3.67seconds
func_fastClustering(testPic, centroids, domainRatio, DELTA)

# func_findWindow(testPic, patternModel, domainRatio, DELTA)
# func_findPattern(originPic, testPic, DELTA, nLargest)