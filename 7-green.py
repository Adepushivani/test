#7.SOLID COLORS(RGB)
#RED COLOR
import numpy as np
import cv2
img = np.zeros((450,670,3))# BLACK BACKGROUND
img[:]=0,255,0 #Assigning the color (B,G,R)
cv2.imshow('RED',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
