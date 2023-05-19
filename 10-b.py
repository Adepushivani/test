#10.EDGE DETECTION - THERE ARE 3 TYPES
#1.SOBEL
#2.LAPLACIAN
#3.CANNY (most accurate and widely used)


#LAPLACIAN and CANNY
import cv2
img = cv2.imread('download.jpeg',0)

laplacian = cv2.Laplacian(img,cv2.CV_8U)
cv2.imshow('LAPLACIAN IMAGE',laplacian)

canny = cv2.Canny(img,125,200)
cv2.imshow('Canny Image',canny)

cv2.waitKey(0)
cv2.destroyAllWindows()
