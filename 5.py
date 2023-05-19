#5.BINARY IMAGE CONVERSION(HIGH CONTRAST)
import cv2
img = cv2.imread('abc.jpeg',0)#0 converts image into grayscale
cv2.imshow('GRAY SCALE Image',img)
cv2.waitKey(2000)

ret,binary = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
#re,binary are the 2 variables to be taken .Ret is a dummy variable
#and Binary is the actual variable

cv2.imshow('Binary',binary)
cv2.waitKey(0)
cv2.destroyAllWindows()
