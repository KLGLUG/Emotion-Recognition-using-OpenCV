The images folder contains the images u wanted to train---------atleast 15 images of each person OR atlest 5-6 emotions of 15 pics in each emotoion of same person

step 1: all the images should be kept in the images folder
step 2: now exicute the file createlabels.py

-->give the give the number of labels
-->give name to each label
-->now assign lable name to each image in the images folder(all the things to be done when the exicuted code asks u to do so)

step 3:now exicute the file traindata.py
-->an argument should be passed along with this command (ex-traindata.py 1)
   1(or)2(or)3 the numbers describe the type of algorithm to be used
   the system gets trained with the data provided i.e images

step 4: now exicute the file predict.py
-->an argument should be sent along with this command(ex-predict.py 1)
   note:-the same argument should be passed that was passed along with the command traindata.py
after this command gets exicuated the webcam gets opened and the face will be detected OR the emotion will be detected as per the given data

things to remember:

all the trained data will be formed into an .xml file
every time you exicute the commnad createlabels.py you need to give number of labels,name them and assign each image the specified label name
never forget to pass arguments along with the commands traindata.py or predict.py
arg'1':LBPHFaceRecognizer
arg'2':EigenFaceRecognize
arg'3':FisherFaceRecognizer



