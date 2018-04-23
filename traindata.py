import cv2
import numpy as np
import sys
import pickle
#try:
FaceRecognizer=None
if sys.argv[1]=="1":
    FaceRecognizer=cv2.face.LBPHFaceRecognizer_create()
elif sys.argv[1]=="2":
    FaceRecognizer=cv2.face.EigenFaceRecognizer_create()
else:
    FaceRecognizer=cv2.face.FisherFaceRecognizer_create()
images=[]
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
filen=open("imagenames.pkl",'rb')
imagenames=pickle.load(filen)
filen.close()
filen=open("labels.pkl",'rb')
labels=pickle.load(filen)
filen.close()
print labels
lab=[]
for i,j in zip(imagenames,labels):
    img=cv2.imread("images\\"+i,0)
    faces = face_cascade.detectMultiScale(img, 1.3, 5)
    try:
        x,y,w,h=faces[0]
        roi_gray = img[y:y+h, x:x+w]
        resized_img=cv2.resize(roi_gray,(128,128))
        images.append(resized_img)
        lab.append(j)
    except Exception as e:
        print "face not detected at "+i
FaceRecognizer.train(images,np.array(lab))
FaceRecognizer.save("FaceRecognizer.xml")
#except Exception as e:
    #print e
    
