import cv2
import numpy as np

img = cv2.imread('Pictures/Superhero.png',0)

img1 = np.uint8(np.log1p(img))

thres = 1

img2 = cv2.threshold(img1,thres,255,cv2.THRESH_BINARY)[1]

cv2.imshow('Converted Image',img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
