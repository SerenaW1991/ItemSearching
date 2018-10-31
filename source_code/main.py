from __future__ import print_function
import imutils
import cv2
import numpy
from func_getColorRatio import *
from func_getContour import *

TEST_PATH= "test_images/"
DOWNLOAD_PATH = "download/"

orginNyQuil = cv2.imread(DOWNLOAD_PATH+"NyQuil_Severe.jpg")
testStore = cv2.imread(TEST_PATH+"test_complicated.png")

# B,G,R = func_getColorRatio(image, 200, 500, 200, 500)
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

func_getContour(orginNyQuil)
func_getContour(testStore)
