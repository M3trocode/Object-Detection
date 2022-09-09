import cv2
#from cv2 import waitKey
from cvzone.ClassificationModule import Classifier

cap = cv2.VideoCapture(0)
detect = Classifier(r'C://Users//creat//Documents//code//Detect//keras_model.h5',r'C://Users//creat//Documents//code//Detect//labels.txt')
while True:
    ret, frame = cap.read()
    predict = detect.getPrediction(frame)
    cv2.imshow('frame', frame )
    if cv2.waitKey(20) and 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()    