import numpy as np 
import cv2

img = cv2.imread('./images/CAM00085.jpg', -1)

cv2.namedWindow('Demo1', cv2.WINDOW_NORMAL)
cv2.imshow('Demo1', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
