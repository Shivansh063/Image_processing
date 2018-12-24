#!/usr/bin/python3

import cv2
import numpy as np


#reading image(pagal.jpg) from current folder ML with 0 (grayscale mode) through imread() and saving into another variable hashtag 
hashtag = cv2.imread('pagal.jpg',0)

#imshow() take 2 parameters (window name and image name)
cv2.imshow('Kids Playing', hashtag)

#waitKey() is used hold image 2window for the time defined in parameter (in milliseconds)
k = cv2.waitKey(0)

#  k == 27 for 'ESC' key
if k == 27 :
	cv2.destroyAllWindows()

# ord('s') is used when we want to perform task (save or exit) with specific key. 
elif k == ord('s') :
	cv2.imwrite('Kids_Playing.png',hashtag)
	cv2.destroyAllWindows()


