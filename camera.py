#!/usr/bin/python3
import sys,time
import cv2

#  we are using  camera first 
cap=cv2.VideoCapture(0)
i=1


while i in range(6) :
	status,frame=cap.read()
	cv2.imshow('live',frame)
	cv2.imwrite('/home/shivansh/Desktop/ML/data/pagal'+str(i)+'.jpg',frame)
	i=i+1
	if cv2.waitKey(10)  &  0xFF  == ord('a'):
		break
               
cv2.destroyAllWindows()
cap.release()


