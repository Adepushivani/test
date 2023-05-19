#9.CHECKER BOARD
import numpy as np
import cv2

img = np.zeros((200,200,3))#creates a black background of 200x200 pixels
img[0:100,0:100] = 255,255,255#white
img[100:200,100:200] = 255,255,255

cv2.imshow('CHECKER BOARD',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
