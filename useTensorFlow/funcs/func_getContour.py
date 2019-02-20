import cv2

def func_getContour(image):
	grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	thresh = cv2.threshold(grayImage, 127, 255, cv2.THRESH_BINARY_INV)[1]
 
	contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
	 
	# draw the contours on the image
	cv2.drawContours(image, contours, -1, (0,255,0), 3)
	cv2.imshow("Image", image)
	cv2.waitKey(0)
