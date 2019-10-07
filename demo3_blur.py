
import numpy as np 
import cv2

cv2.namedWindow('img_in', cv2.WINDOW_AUTOSIZE)
cv2.namedWindow('img_out', cv2.WINDOW_AUTOSIZE)

img_in = cv2.imread('./img/lena.jpg', -1)
img_in = cv2.cvtColor(img_in, cv2.COLOR_BGR2GRAY)

#img_out = cv2.GaussianBlur(img_in, (5, 5), 3)
#img_out = cv2.GaussianBlur(img_out, (3, 3), 3)

#img_out = cv2.pyrDown(img_in)

img_out = cv2.pyrDown(img_in)
img_out = cv2.pyrDown(img_out)

img_out = cv2.Canny(img_out, 10, 50)

cv2.imshow('img_in', img_in)
cv2.imshow('img_out', img_out)

cv2.waitKey(0)
cv2.destroyAllWindows()