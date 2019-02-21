from __future__ import print_function
import imutils
import cv2
import numpy
from funcs.func_getColorRatio import *
from funcs.func_getContour import *
from funcs.func_findPattern import *
from funcs.func_openCV_patternMatch import *


TEST_PATH= "test_images/"
DOWNLOAD_PATH = "download/"

orginNyQuil = cv2.imread(DOWNLOAD_PATH+"NyQuil_Severe.png")
testStore = cv2.imread(TEST_PATH+"test_complicated.png")

DEST_WIDTH = 20.0

# resize the image
height, width, depth = orginNyQuil.shape
imgScale = DEST_WIDTH/width

newX,newY = orginNyQuil.shape[1]*imgScale, orginNyQuil.shape[0]*imgScale
newimg = cv2.resize(orginNyQuil,(int(newX),int(newY)))

func_openCV_patternMatch(newimg, testStore)