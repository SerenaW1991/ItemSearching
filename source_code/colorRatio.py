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
WIDTH, HEIGHT = 20, 40
DELTA = 0.01


orginNyQuil = cv2.imread(DOWNLOAD_PATH+"pattern.png")
testStore = cv2.imread(TEST_PATH+"test_complicated.png")

func_findPattern(orginNyQuil, testStore, WIDTH, HEIGHT, DELTA)
# func_getContour(orginNyQuil)