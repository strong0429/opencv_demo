import numpy as np 
import cv2

cv2.namedWindow('Demo2', cv2.WINDOW_NORMAL)

cap = cv2.VideoCapture('./images/mvi_3739.mov')

while True:
    ret, frame = cap.read()

    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('Demo2', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()