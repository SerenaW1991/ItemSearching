import cv2
from funcs.func_drawRectAndshow import *

def func_drawRectAndshow(image, startX, endX, startY, endY):
	cv2.rectangle(image, (startX, startY), (endX, endY), (0,0,255), 2)
	