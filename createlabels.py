import pickle
import sys
import os
arr=[f for f in os.listdir("images") if os.path.isfile("images//"+f)]
filen=open('imagenames.pkl','wb')
pickle.dump(arr,filen)
filen.close()
print arr
n=int(raw_input("Enter number of labels:"))
labelnames=[]
for i in range(1,n+1):
    labelnames.append(raw_input("Enter name for the label "+str(i)+":"))
labels=[]
for i in arr:
    labels.append(int(raw_input("Assign label to image "+i+":")))
filen=open('labels.pkl','wb')
pickle.dump(labels,filen)
filen.close()
filen=open("labelnames.pkl",'wb')
pickle.dump(labelnames,filen)
filen.close()
    
