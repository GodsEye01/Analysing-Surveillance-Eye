import cv2
import numpy 

cap=cv2.VideoCapture(0)

while True:
	ret,showcase=cap.read()
	cv2.imshow('showcase',showcase) 
	cv2.imshow('gray',gray)#picshow
	if cv2.waitKey(10000) & 0xFF==ord('q'):
		break
