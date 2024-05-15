import numpy as np
import cv2
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
img = cv2.imread('./assets/fondoMenu.jpg')
print(img.shape)

img = cv2.resize(img,(800,650))
#img = cv2.flip(img,0)
cv2.imwrite("./assets/fondoMenu.jpg",img)