import cv2
import numpy as py


face_cascade = cv2.CascadeClassifier('haar.xml')

img = cv2.imread('fsamp1.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray,1.01,7)
print(type(faces))
for (x,y,w,h) in faces:
    img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# get frames from default camera
#cap = cv2.VideoCapture(0)

#loop runs if capturing occurs

# while 1:

    #read frames from camera
    # ret, img = cap.read()
    
    #onvert each frame to grayscale image
    # gray = cv2.cvtColor(img, cv2.COLOR2BGRGRAY)
    
    #display image in window
    # cv2.imshow('Display', img)
    
    #wait for esc key to stop
    # esc = cv2.waitKey(30) & 0xff
    # if esc == 27:
        # break

#close window
# cap.release()

#de-allocate any associated memory usage
# cv2.destoryAllWindows()
    