import numpy as np 
import cv2

g_dontset = 0
g_run = 1

cap = None

def onTrackbarSlide(pos):
    global g_dontset, g_run

    cap.set(cv2.CAP_PROP_POS_FRAMES, pos)

    if g_dontset == 0:
        g_run = 1
    g_dontset = 0
    
cv2.namedWindow('demo1', cv2.WINDOW_AUTOSIZE)

cap = cv2.VideoCapture('./img/skier.mp4')
# cap.read()
frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
tmpH = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
tmpW = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print('Video has', frames, ' frames of dimesion(', tmpW, ',', tmpH, ' )')

cv2.createTrackbar('VideoBar', 'demo1', 0, frames, onTrackbarSlide)

while True:
    if g_run != 0:
        ret, frame = cap.read()
        if ret == False:
            break

        tmp_pos = int(cap.get(cv2.CAP_PROP_POS_FRAMES))
        g_dontset = 1
        cv2.setTrackbarPos('VideoBar', 'demo1', tmp_pos)
        cv2.imshow('demo1', frame)

        g_run -= 1

    key = cv2.waitKey(1) & 0xFF
    if key == ord('s'):
        g_run = 1
        # print('Single step, run =', g_run)
    elif key == ord('r'):
        g_run = -1
        # print('Run mode, run =', g_run)
    elif key == 27:
        break

cap.release()
cv2.destroyAllWindows()

