import cv2

image = cv2.imread('../img/like_lenna.png')
image_small = cv2.resize(image, (100, 100))

# 이미지를 보여주는 명령어
#cv2.imshow('Image Window', image)
cv2.imshow('Image Window', image_small)

cv2.waitKey(0)
cv2.destoryAllWindow()
#cv2.imshow(image)

