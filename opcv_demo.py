import numpy as np
import pygame
import sys
import cv2

pygame.init()

screen = pygame.display.set_mode((640, 480))

cap = cv2.VideoCapture(0)

clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            cap.release()
            sys.exit(0)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.ESCAPE :
                break

    ret, frame = cap.read()

    if not ret:
        break
    
    img = cv2.flip(frame, 1)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    surf = pygame.image.frombuffer(img, (img.shape[1], img.shape[0]), 'RGB')
    screen.blit(surf, (0, 0))
    pygame.display.update()
    clock.tick(30)
    
cap.release()


'''
cv2.imshow('image',img)
k = cv2.waitKey(0)
if k == 27:         # wait for ESC key to exit
    cv2.destroyAllWindows()
elif k == ord('s'): # wait for 's' key to save and exit
    cv2.imwrite('messigray.png',img)
    cv2.destroyAllWindows()
'''