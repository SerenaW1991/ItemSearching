import cv2
from funcs.func_drawRectAndshow import *

def func_drawRectAndshow(image, startRow, endRow, startCol, endCol):
	cv2.rectangle(image, (startCol, startRow), (endCol, endRow), (0,0,255), 2) # rectangle is using (col, row)
	