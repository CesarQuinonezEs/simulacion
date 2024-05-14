import numpy as np
import cv2
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
img = cv2.imread('./assets/Quit Rect.png')
print(img.shape)

img = cv2.resize(img,(177,54))
#img = cv2.flip(img,0)
cv2.imwrite("./assets/Quit Rect.png",img)