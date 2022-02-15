import cv2 
import numpy as np
img = cv2.imread("testbot1.jpg")
blurred = cv2.blur(img, (1,9))
cv2.imshow('ImageWindow', img)
