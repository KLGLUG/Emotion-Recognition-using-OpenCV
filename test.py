import pickle
import cv2
from copy import deepcopy
import numpy as np
import sys
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
FaceRecognizer=None
if sys.argv[1]=="1":
    FaceRecognizer=cv2.face.LBPHFaceRecognizer_create()
elif sys.argv[1]=="2":
    FaceRecognizer=cv2.face.EigenFaceRecognizer_create()
else:
    FaceRecognizer=cv2.face.FisherFaceRecognizer_create()
FaceRecognizer.read("FaceRecognizer.xml")
f=open("imagenames.pkl",'rb')
imagenames=pickle.load(f)
f.close()
print imagenames
img=cv2.imread("predict_images\\test4.jpg",0)
faces = face_cascade.detectMultiScale(img, 1.3, 5)
x,y,w,h=faces[0]
roi_gray = img[y:y+h, x:x+w]
resized_img=cv2.resize(roi_gray,(128,128))
print FaceRecognizer.predict(resized_img)
