#12.RESIZE / SCALING the image

import cv2
import numpy as np
img = cv2.imread('abc.jpeg')
cv2.imshow('Original Image',img)
cv2.waitKey(500)

#Now let us reduce the scale of our image from 100 to 75%
img1 = cv2.resize(img,None,fx = 0.75,fy = 0.75)
cv2.imshow('Scale down',img1)


cv2.waitKey(0)
cv2.destroyAllWindows()
