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
WIDTH, HEIGHT = 30, 120
DELTA = 0.01

originPic = cv2.imread(DOWNLOAD_PATH+"sports_blue.png")
testPic = cv2.imread(TEST_PATH+"test_sunscreen.png")

func_findPattern(originPic, testPic, WIDTH, HEIGHT, DELTA)
# func_getContour(orginNyQuil)