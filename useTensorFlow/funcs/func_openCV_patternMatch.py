import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

def func_openCV_patternMatch(template, image):
    img2 = image.copy()
    w,h,channel = template.shape[::-1]
    # All the 6 methods for comparison in a list
    # methods = ['cv.TM_CCOEFF', 'cv.TM_CCOEFF_NORMED', 'cv.TM_CCORR',
    #             'cv.TM_CCORR_NORMED', 'cv.TM_SQDIFF', 'cv.TM_SQDIFF_NORMED']
    methods = ['cv.TM_SQDIFF_NORMED']
    for meth in methods:
        img = img2.copy()
        method = eval(meth)
        
        # Apply template Matching
        res = cv.matchTemplate(img,template,method)
        # Specify a threshold 
        threshold = 0.9
        # Store the coordinates of matched area in a numpy array 
        loc = np.where( res >= threshold)
        if len(loc) >0:
            return True
        # # Draw a rectangle around the matched region. 
        # for pt in zip(*loc[::-1]): 
        #     cv.rectangle(image, pt, (pt[0] + w, pt[1] + h), (0,255,255), 2)

        # Show the final image with the matched area. 
        # cv.imshow('Detected',image)
        # cv.waitKey(0)


        # min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
        
        # # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
        # if method in [cv.TM_SQDIFF, cv.TM_SQDIFF_NORMED]:
        #     top_left = min_loc
        # else:
        #     top_left = max_loc
        # bottom_right = (top_left[0] + w, top_left[1] + h)
        # cv.rectangle(img, top_left, bottom_right,255, 2)
        
        # plt.subplot(121), plt.imshow(res,cmap = 'gray')
        # plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
        # plt.subplot(122),plt.imshow(img,cmap = 'gray')
        # plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
        # plt.suptitle(meth)
        # plt.show()