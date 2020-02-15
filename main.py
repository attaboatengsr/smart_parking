import cv2
import numpy as py

# get frames from default camera
cap = cv2.VideoCapture(0)

#loop runs if capturing occurs

while 1:

    #read frames from camera
    ret, img = cap.read()
    
    #convert each frame to grayscale image
    gray = cv2.cvtColor(img, cv2.COLOR2BGRGRAY)
    
    #display image in window
    cv2.imshow('Display', img)
    
    #wait for esc key to stop
    esc = cv2.waitKey(30) & 0xff
    if esc == 27:
        break

#close window
cap.release()

#de-allocate any associated memory usage
cv2.destoryAllWindows()+
    