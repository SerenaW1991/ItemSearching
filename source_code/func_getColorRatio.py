import numpy

def func_getColorRatio(imageArray, startx, endx, starty, endy):
	B,G,R = 0.0,0.0,0.0
	for x in range(startx, endx):
		for y in range(starty, endy):
			curB, curG, curR = imageArray[x][y]
			B += curB
			G += curG
			R += curR
	allArea = B+G+R
	return [B/allArea, G/allArea, R/allArea]
	