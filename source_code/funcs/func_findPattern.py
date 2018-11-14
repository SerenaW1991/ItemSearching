from funcs.func_getColorRatio import *
from funcs.func_drawRectAndshow import *
import cv2
import math

def func_findPattern(pattern, testImage, WIDTH, HEIGHT, DELTA):
	patternHeight, patternWidth, channels = pattern.shape
	patternB, patternG, patternR = func_getColorRatio(pattern, 0,patternWidth,0,patternHeight)

	testImageHeight, testImageWidth, testImageChannels = testImage.shape
	startX, startY = 0,0

	print (patternHeight, patternWidth, channels)
	print (patternB, patternG, patternR)

	while(startX < testImageWidth-WIDTH):
		while(startY < testImageHeight-HEIGHT):
			endX = startX+WIDTH
			endY = startY+HEIGHT

			tmpB, tmpG, tmpR = func_getColorRatio(testImage, startX, endX, startY, endY)

			if(math.fabs(tmpB-patternB) <= DELTA and math.fabs(tmpG-patternG) <= DELTA and math.fabs(tmpR-patternR) <= DELTA):
				func_drawRectAndshow(testImage, startX, endX, startY, endY)
			startY+=HEIGHT
		startX+=WIDTH
		startY=0
	cv2.imshow("FoundArea", testImage)
	cv2.waitKey(0)
