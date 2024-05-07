import numpy as np
import cv2
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
img = cv2.imread('12.png')
img = cv2.resize(img,(16,16))
img = cv2.flip(img,0)
cv2.imwrite("abeja.png",img)