#!/usr/bin/python

import cv2

#  we are using  camera first 
cap=cv2.VideoCapture(0)
i=1
face_cascade=cv2.CascadeClassifier('face.xml')
roi_color = None

for i in range(100000) :
	status,frame=cap.read()
	grayimg=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	faces = face_cascade.detectMultiScale(grayimg, 1.15, 5)
	
	for x,y,w,h in faces :
		roi_color = grayimg[y:y+h, x:x+w]
	for x,y,w,h in faces :
		cv2.rectangle(grayimg,(x,y),(x+w,y+h),(255,255,255),2)	
	cv2.imshow('live',grayimg)
	if cv2.waitKey(10) & 0xFF == ord('c') :
		cv2.imwrite('Destination Folder+Image name',roi_color)
		i=i+1
	if cv2.waitKey(10) & 0xFF == ord('q') :
		break
	

cap.release()               
cv2.destroyAllWindows()



