import cv2

img = cv2.imread('Pictures/Superhero.png',1)

cv2.imshow('Us',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

cv2.imshow('PAST',gray)
cv2.waitKey(0)
cv2.destroyAllWindows()
