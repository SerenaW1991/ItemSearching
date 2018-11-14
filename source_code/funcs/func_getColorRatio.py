import numpy

def func_getColorRatio(imageArray, startx, endx, starty, endy):
	B,G,R = 0.0, 0.0, 0.0
	for x in range(startx, endx):
		for y in range(starty, endy):
			curB, curG, curR = imageArray[y][x]
			B += curB
			G += curG
			R += curR
	allArea = B+G+R
	if(allArea == 0):
		return [0,0,0]
	else:
		return [B/allArea, G/allArea, R/allArea]
	