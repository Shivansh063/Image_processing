#!usr/bin/python3

import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while (1) :
	res,frame =  cap.read()
	hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
	cv2.imshow('Kids Playing', frame)
	cv2.imshow('Kids Playin', hsv)
	if cv2.waitKey(30) & 0xFF == ord('q'):
	      break


cap.release()
cv2.deleteAllWindows()
