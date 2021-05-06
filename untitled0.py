# -*- coding: utf-8 -*-
"""
Created on Tue May  4 21:10:02 2021

@author: donut
"""
import csv
import math
import numpy as np
import cv2
import imutils
zero=[0,0]

def Average(lst):
    return sum(lst) / len(lst)
img = cv2.imread('frame0.jpg')
cv2.imshow('image',img)
cv2.waitKey(0) 
cv2.destroyAllWindows() 
cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
#nose_cascade = cv2.CascadeClassifier('./cascade_files/haarcascade_mcs_nose.xml')
def convertTuple(tup):
    str =  ''.join(tup)
    return str
l=[]
d=[]
while True:
    
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 5)
        roi_gray = gray[y:y+w, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray, 1.3, 5)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 5)
            cv2.line(roi_color,(ex,ey),(ex+ew,ey+eh),(255, 0, 0))
            centx=int((ex+ex+ew)//2)
            centy=int((ey+ey+eh)//2)
            centxs=str(centx)
            centys=str(centy)
            centps=(centxs,centys)
            centp=(centx,centy)
            cv2.line(roi_color,centp,(0,0),(0,255,0),3)
            x=(convertTuple(centps))
            print(centp)
            l.append(centp)
            y='(',centx,',',centy,')'
            z=[centx,centy]
            dist= (math.dist(z,zero))
            y=str(y)
            cv2.putText(frame, 
                str(dist), 
                (50, 50), 
                cv2.FONT_HERSHEY_SIMPLEX, 1, 
                (0, 255, 255), 
                2, 
                cv2.LINE_4)
            for i in range(len(l)+1):
                print(l[i-1])
                cv2.line(roi_color,l[0],l[i-1],(255, 0, 0),5)
                p1=list(l[0])
                p2=list(l[i-1])
                distc= (math.dist(p1,p2))
                d.append(distc)
    
       
    cv2.imshow('frame', frame)
    i = 0
    if cv2.waitKey(1) == ord('q'):
        
        break
    cv2.imwrite('Frame'+str(i)+'.jpg', frame)
    i += 1

cap.release()
cv2.destroyAllWindows()
print('test')
print(d)
dist=(Average(d))
with open('idistances.csv', 'a', newline='') as file:
    writer = csv.writer(file)
    writer.writerow([dist])
    
