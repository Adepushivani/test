#14.LIVE SKETCH FROM WEBCAM
import cv2

cap = cv2.VideoCapture(0) #0 reserves the default web cam port and 1 for pc or external cam

while True:
    ret,frame = cap.read() # so it is reading the video from the cap variable
    #ret and frame are 2 variables to be taken ,BUt onlt frame will be used
    #ret is dummy
    cv2.imshow('My Live Sketch',frame)
    if cv2.waitKey(1) == 13:
        break

cap.release() #It releases the port which was reserved
#If cap.release is not done , it might corrupt your webcam drivers
cv2.destroyAllWindows()
