import cv2

img = cv2.imread('Pictures/Superhero.png',1)

cv2.imshow('Us',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

dimention = img.shape

print('Dimention of Image:',dimention)

height = img.shape[0]
width = img.shape[1]
channels = img.shape[2]

print('Image Height       : ',height)
print('Image Width        : ',width)
print('Number of Channels : ',channels)
