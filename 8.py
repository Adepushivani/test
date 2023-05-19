#8.Let us create an image of 300x300 pixels
#and divide the image into 3 parts of 3 different colors

import cv2
import numpy as np
image = np.zeros((300,300,3))#creates a black image

#image[y-coordinates,x-coordinates]
image[0:100,0:300] = 0,255,0 # GREEN
image[100:200,0:300] = 255,255,255 #WHITE
image[200:300,0:300] = 0,0,255 #RED

cv2.imshow('COLORS',image)
cv2.waitKey(0)
cv2.destroyAllWindows()
