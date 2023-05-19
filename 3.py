#3.READ the INFORMATION ABOUT THE IMAGE
import cv2
img = cv2.imread('abc.jpeg')#reading the image
print(img.shape)


#output:
#(168, 300, 3)
#168 - Height of image in pixels
#300 - Width of image in pixels
#3 - Channel number/depth(3 colors -RGB)
