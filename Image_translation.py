import cv2
import numpy as np

img = cv2.imread('Pictures/Superhero.png',1)

cv2.imshow('Us',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

h,w = img.shape[:2]

nh,nw = h/4,w/4

T = np.float32([[1,0,nw],[0,1,nh]])
imgT = cv2.warpAffine(img,T,(w,h))

cv2.imshow('Modifided data',imgT)
cv2.waitKey(0)
cv2.destroyAllWindows()
