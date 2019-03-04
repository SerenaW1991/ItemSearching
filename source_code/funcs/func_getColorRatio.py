import numpy
from funcs.func_closestColor import *
import cv2
import time

def func_getColorRatio(imageArray, minRow, maxRow, minCol, maxCol):
	allColors = {}
	numPixels = 0
	for row in range(minRow, maxRow):
		for col in range(minCol, maxCol):
			numPixels+=1
			curB, curG, curR = imageArray[row][col]
			_,curColorName = get_colour_name([curR, curG, curB])
			if curColorName in allColors:
				allColors.update({curColorName:allColors[curColorName]+1})
			else:
				allColors.update({curColorName:1})
	for key,value in allColors.items():
		allColors[key] = allColors[key]/numPixels
	return allColors


	