#6.SOLID BACKGROUND(WHITE or BLACK BACKGROUND)
#BLACK
import numpy as np
import cv2

img = np.zeros((500,500,3))#500 is length , 500 is width in pixels,3 - depth
#Img variable has an image with white background

cv2.imshow('BLACK BACKGROUND',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
