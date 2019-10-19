import cv2
from matplotlib import pyplot as plt

img = cv2.imread('Pictures/Superhero.png',0)

sobelx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
sobely = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)

plt.imshow(img,cmap = 'gray')
plt.title('Original')
plt.show()
plt.imshow(sobelx,cmap = 'gray')
plt.title('Sobel X')
plt.show()
plt.imshow(sobely,cmap = 'gray')
plt.title('Sobel Y')

plt.show()
