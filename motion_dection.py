import  cv2
import numpy as np

face_cascade= cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
cap= cv2.VideoCapture(0)
while True:
    ret,img=cap.read()
    gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(gray)
    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x,y),(x+w,y+h),(255,0,0),2)
        #roi_gray=Gray[y:y+h,x:x+w]
        #roi_colour=img[y:y+h,x:x+w]
        cv2.imshow('mption_img',img)
        k=cv2.waitKey(0) & 0xff
        if k == 27:
            break
cap.release()
cv2.destroyAllWindows()

	
