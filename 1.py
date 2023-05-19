#1.READ AN IMAGE and DISPLAY it.

import cv2 #importing the opencv library
img = cv2.imread('abc.jpeg') # reading the image and storing it in variable img
cv2.imshow('OUTPUT1',img)#display the image

cv2.waitKey(0)
cv2.destroyAllWindows()
