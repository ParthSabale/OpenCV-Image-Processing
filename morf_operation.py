import cv2 
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("testbot2.jpg")
img = cv2.getStructuringElement(cv2.MORPH_RECT, (210, 70))
img = cv2.morphologyEx(img, cv2.MORPH_CLOSE, img)

cv2.imshow('ImageWindow', img)
