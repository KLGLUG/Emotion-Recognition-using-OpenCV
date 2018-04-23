import numpy as np
import cv2
import pickle
import time
import sys

    
if __name__=="__main__":
    FaceRecognizer=None
    if sys.argv[1]=="1":
        FaceRecognizer=cv2.face.LBPHFaceRecognizer_create()
    elif sys.argv[1]=="2":
        FaceRecognizer=cv2.face.EigenFaceRecognizer_create()
    else:
        FaceRecognizer=cv2.face.FisherFaceRecognizer_create()
    FaceRecognizer.read("FaceRecognizer.xml")
    f=open("labelnames.pkl","rb")
    labelnames=pickle.load(f)
    f.close()
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    font = cv2.FONT_HERSHEY_SIMPLEX
    cap=cv2.VideoCapture(0)
    roi_gray=None
    while(True):
        ret,frame=cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        for (x,y,w,h) in faces:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
            roi_gray = gray[y:y+h, x:x+w]
            #roi_color = frame[y:y+h, x:x+w]
            resized_img=cv2.resize(roi_gray,(250,250))
            #edgeimg=cv2.Canny(resized_img,100,200)
            detectedvalues=FaceRecognizer.predict(resized_img)
            detectedlabel=detectedvalues[0]
            detectionaccur=detectedvalues[1]
            text=labelnames[detectedlabel-1]
            print text,detectionaccur
            cv2.putText(frame,text,(x,y),font,1,(255,255,255),2,cv2.LINE_AA)
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xff==ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
    '''plt.imshow(resize_img,cmap="gray")
    plt.show()'''
