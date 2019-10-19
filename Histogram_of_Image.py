import cv2
import matplotlib.pyplot as plt

img = cv2.imread('Pictures/Superhero.png',1)

b,g,r = cv2.split(img)


plt.hist(b.ravel(),256,[0,256])
plt.hist(g.ravel(),256,[0,256])
plt.hist(r.ravel(),256,[0,256])
plt.show()

cv2.imshow('Image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
