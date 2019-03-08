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

def bruteForceSlidingWindow(SW_R, SW_C, domColorInPattern, patternColors, testImage, DELTA):
	testImageRow, testImageCol,_ = testImage.shape
	row,col = 0,0
	maxRow,maxCol = row+SW_R, col+SW_C

	print ("Current Sliding Window size: ", SW_R, SW_C)

	while maxRow<testImageRow:
		while maxCol<testImageCol:
			print ("Currently Analysing ", row, maxRow, col, maxCol)
			
			SW_color = func_getColorRatio(testImage, 0, maxRow,0, maxCol)

			if compareTwoDics(domColorInPattern, patternColors, SW_color, 3, DELTA):
				func_drawRectAndshow(testImage, row, maxRow, col, maxCol)
				cv2.imshow("FoundArea", testImage)
				cv2.waitKey(0)
				return True
			else:
				col += 1
				maxCol = col+SW_C
		col = 0
		maxCol = col+SW_C
		row += 1
		maxRow = row+SW_R
	
	return False


def func_findPattern(pattern, testImage, DELTA, nLargest):
	patternRow, patternCol, _ = pattern.shape
	patternColors = func_getColorRatio(pattern, 0, patternRow,0, patternCol)  # get a dic of all colors:pixel numbers

	domColorInPattern = nlargest(nLargest, patternColors, key=patternColors.get)
	print (domColorInPattern)

	testImageRow, testImageCol,_ = testImage.shape
	SW_R, SW_C = testImageRow-1, testImageCol-1

	while SW_R>=0:
		while SW_C>=0:
			if bruteForceSlidingWindow(SW_R, SW_C, domColorInPattern, patternColors, testImage, DELTA):
				break
			else:
				SW_C -= 1
		SW_C = testImageCol-1
		SW_R -= 1





	
