#!/usr/bin/python

import cv2
import os
import time

#  we are using  camera first 
cap=cv2.VideoCapture(0)
i=1
face_cascade=cv2.CascadeClassifier('/home/shivansh/Desktop/ML/face.xml')
roi_color = None
path = '/home/shivansh/Desktop/face_Recognition/Images/s'
z=1
diru = None
Directory_name= None
option = str(input("Want to Create a new Directory or not : "))
if option == 'n' or option == 'N' :
  Directory_name = str(input("Enter your Directory in which you want to save : "))

	
time.sleep(3)

if option == 'y' or option == 'Y' : 
	while (True) :
	    try:
	    	os.makedirs(path + str(z))
	    except OSError:  
    		z =z+1	
	    else:  
    		print("Successfully created the directory")
    		break

while (True) :
	status,frame=cap.read()
	faces = face_cascade.detectMultiScale(frame, 1.15, 5)
	
	for x,y,w,h in faces :
		roi_color = frame[y:y+h, x:x+w]

	cv2.imshow('live',frame)

	if cv2.waitKey(10) & 0xFF == ord('c') :
		if option == 'y' or option == 'Y' : 
			cv2.imwrite('/home/shivansh/Desktop/face_Recognition/Images/s'+str(z)+'/'+str(i)+'.jpeg',roi_color)
			i=i+1
			if i == 10 :
				break
		else:
			cv2.imwrite('/home/shivansh/Desktop/face_Recognition/Images/'+Directory_name+'/'+str(i)+'.jpeg',roi_color)
			num = random.randint(1,13000)	
			cv2.imwrite('/home/shivansh/Desktop/face_Recognition/Images/s'+str(z)+'/'+str(num)+'.jpeg',roi_color)
			i=i+1
			if i == 10 :
				break
	if cv2.waitKey(10) & 0xFF == ord('q') :
		break
	
 
cap.release()               
cv2.destroyAllWindows()




