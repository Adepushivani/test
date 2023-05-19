#15.MY CANNY SKETCH(EDGE DETECTION)
import cv2

cap = cv2.VideoCapture(0)

while True:
    ret,frame = cap.read()
    canny = cv2.Canny(frame,20,159)
    cv2.imshow('My Live Sketch',canny)
    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
