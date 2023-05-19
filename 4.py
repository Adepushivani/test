#4.GRAYSCALE IMAGE - BLACK and WHITE
import cv2
img = cv2.imread('abc.jpeg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('NORMAL IMAGE',img)
cv2.imshow('GRAY SCALE IMAGE',gray)

cv2.waitKey(0)
cv2.destroyAllWindows()
