#13.RECTANGLE/SQUARE
#to put in text
import cv2
import numpy as np
img = np.zeros((1000,1000,3))


name = input('Enter the name:')

cv2.putText(img,name,(250,250),cv2.FONT_HERSHEY_TRIPLEX,2,(0,0,255),1)

cv2.imshow('IMAGE',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
