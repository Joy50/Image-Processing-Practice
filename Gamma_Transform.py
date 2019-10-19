import cv2
import numpy as np

img = cv2.imread('Pictures/Superhero.png',0)

gamma = int(input('Value of gamma:'))

conv_image = np.power(img,gamma)

cv2.imshow('Converted Image',conv_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
