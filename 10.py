#10.EDGE DETECTION - THERE ARE 3 TYPES
#1.SOBEL
#2.LAPLACIAN
#3.CANNY (most accurate and widely used)


#SOBEL
import cv2
img = cv2.imread('123.jpeg',0)#0 converts image into grayscale
sobel_x = cv2.Sobel(img,cv2.CV_8U,dx = 1,dy = 0,ksize = -1)
#CV_8U - unsigned 8bit/pixel

sobel_y = cv2.Sobel(img,cv2.CV_8U,dx = 0,dy = 1 ,ksize = -1)
sobel = cv2.bitwise_or(sobel_x,sobel_y)

cv2.imshow('Sobel X Image',sobel_x)
cv2.imshow('Sobel Y Image',sobel_y)
cv2.imshow('Sobel Image',sobel)
 


cv2.waitkey(0)
cv3.destroyAllWindows()
