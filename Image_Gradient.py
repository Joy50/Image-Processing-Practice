import cv2
from matplotlib import pyplot as plt

img = cv2.imread('Pictures/Superhero.png',0)

laplacian = cv2.Laplacian(img,cv2.CV_64F)

plt.imshow(img,cmap = 'gray')
plt.title('Original')
plt.show()
plt.imshow(laplacian,cmap = 'gray')
plt.title('Laplacian')
plt.show()


plt.show()
