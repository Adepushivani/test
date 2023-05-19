#2.CREATING A DUPLICATE IMAGE
import cv2
img = cv2.imread('abc.jpeg') #read the image
cv2.imshow('OUTPUT1',img)#We display the image
cv2.imwrite('amn.png',img)#we create a new image and download it

cv2.waitKey(0)
cv2.destroyAllWindows()

