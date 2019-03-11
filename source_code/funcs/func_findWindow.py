import numpy as np
import time
from funcs.func_drawRectAndshow import *

def compareTwoDics(domColorInPattern, SW_Dic, DELTA):
	for key,value in domColorInPattern.items():
		if key not in SW_Dic:
			return False
		if abs(value-SW_Dic[key])>DELTA:
			return False
	return True

def del_dicOne(dic1, dic2):
	result = {}
	for key,value in dic2.items():
		if key not in dic1:
			result[key] = value
		else:
			result[key] = value-dic1[key]
	return result

def add_TwoDics(dic1, dic2):
	result = {}
	for key, value in dic1.items():
		if key not in dic2:
			result[key] = value
		else:
			result[key] = value+dic2[key]

	for key, value in dic2.items():
		if key not in dic1:
			result[key] = value
	return result

def slideWindow(SW_R, SW_C, domColorInPattern, testPicPredCountRow, DELTA, testPic):
	testImageRow, testImageCol = len(testPicPredCountRow), len(testPicPredCountRow[0])
	row,col = 0,0
	maxRow,maxCol = row+SW_R, col+SW_C

	print ("Current Sliding Window size: ", SW_R, SW_C)

	while maxRow<testImageRow:
		while maxCol<testImageCol:
			# print ("Currently Analysing ", row, maxRow, col, maxCol)
			SW_Dic = {}
			
			for num in range(row, maxRow+1):
				if col <= 0:
					SW_Dic = add_TwoDics(SW_Dic, testPicPredCountRow[num][maxCol])
				else:
					tmp = del_dicOne(testPicPredCountRow[num][col-1], testPicPredCountRow[num][maxCol])
					SW_Dic = add_TwoDics(SW_Dic, tmp)
			
			for key,value in SW_Dic.items():
				SW_Dic[key] = 1.0*value/(SW_R*SW_C)

			if compareTwoDics(domColorInPattern, SW_Dic, DELTA):
				func_drawRectAndshow(testPic, row, maxRow, col, maxCol)
				return True
			else:
				col += 1
				maxCol = col+SW_C
		col = 0
		maxCol = col+SW_C
		row += 1
		maxRow = row+SW_R	
	return False


def func_findWindow(testPic, patternModel, domainRatio, DELTA):
	testImageRow, testImageCol,_ = testPic.shape
	SW_R, SW_C = testImageRow-1, testImageCol-1
	testPicPrediction = np.zeros(shape=(testImageRow,testImageCol))
	testPicPredCountRow = [[0 for y in range(testImageCol)] for x in range(testImageRow)] 

	predictionTimeSum = 0
	for row in range(0, testImageRow):
		for col in range(0, testImageCol):
			curPixel = testPic[row][col]
			
			# TODO: prediction step is time consuming, findout why
			start = time.time()
			predResult = patternModel.predict([[curPixel[0], curPixel[1], curPixel[2]]])[0]
			predictionTimeSum += time.time()-start

			testPicPrediction[row][col] = predResult

			if col <= 0:
				testPicPredCountRow[row][col] = {predResult:1}
			else:
				testPicPredCountRow[row][col] = testPicPredCountRow[row][col-1].copy()
				if predResult in testPicPredCountRow[row][col]:
					testPicPredCountRow[row][col][predResult] += 1
				else:
					testPicPredCountRow[row][col][predResult] = 1
	
	print ("prediction time: ", predictionTimeSum)

	while SW_R>0:
		while SW_C>0:
			if slideWindow(SW_R, SW_C, domainRatio, testPicPredCountRow, DELTA, testPic):
				break
			else:
				SW_C = int(SW_C/2)
		SW_C = int(testImageCol-1)
		SW_R = int(SW_R/2)

	cv2.imshow("FoundArea", testPic)
	cv2.waitKey(0)