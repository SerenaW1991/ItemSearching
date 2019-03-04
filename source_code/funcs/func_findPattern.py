from funcs.func_getColorRatio import *
from funcs.func_drawRectAndshow import *
import cv2
import math
from heapq import nlargest

def compareTwoDics(domColorInPattern, patternDic, SW_Dic, numDomColors, DELTA):
	for key in domColorInPattern:
		if key not in SW_Dic:
			return False
		else:
			if abs(patternDic[key]-SW_Dic[key])>DELTA:
				return False
	return True


def func_findPattern(pattern, testImage, DELTA, nLargest):
	patternRow, patternCol, _ = pattern.shape
	patternColors = func_getColorRatio(pattern, 0, patternRow,0, patternCol)  # get a dic of all colors:pixel numbers

	domColorInPattern = nlargest(nLargest, patternColors, key=patternColors.get)
	print (domColorInPattern)

	testImageRow, testImageCol,_ = testImage.shape
	row = 0
	curRatio = 0.1
	
	while curRatio<10:
		while(row < testImageRow):
			maxRow = int(row+patternRow*curRatio)
			if maxRow >= testImageRow:
				break;
			SW_color = func_getColorRatio(testImage, row, maxRow, 0, testImageCol-1)

			if compareTwoDics(patternColors, patternColors, SW_color, 3, DELTA):
				func_drawRectAndshow(testImage, row, maxRow, 0, testImageCol-1)
				cv2.imshow("FoundArea", testImage)
				cv2.waitKey(0)

			row = maxRow
		curRatio *= 10