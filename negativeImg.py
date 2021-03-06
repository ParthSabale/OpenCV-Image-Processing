import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('testbot1.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


equ = cv2.equalizeHist(img)
res = np.hstack((img,equ)) #stacking images side-by-side
cv2.imshow("Frame", res)
key = cv2.waitKey(1) & 0xFF
