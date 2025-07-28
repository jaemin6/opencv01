import cv2
import numpy as np

# 이미지 불러오기
image = cv2.imread('../img/like_lenna.png')

new_height = 300
new_width = 300

# 상하 반전
image_fliped = cv2.flip(image, 0)

# 이미지 리사이즈
resized_image = cv2.resize(image, (new_width, new_height))

# 2. 2배 확대 (비율로 리사이즈)
#image_big = cv2.resize(image, dsize=None, fx=2, fy=2)

# 이미지 보여주기
cv2.imshow('Original Image', image)
cv2.imshow('Resized Image (300x300)', resized_image)
cv2.imshow('Flipped Image (UpDown)', image_fliped)
#cv2.imshow('Zoomed x2 Image', image_big)

dst = np.zeros((new_height, new_width), dtype=np.uint8)
dst = cv2.resize(image, (new_width, new_height))

#cv2.resize(image, (new_width, new_height), dst=dst)


print(image.shape)
print(resized_image.shape)


cv2.waitKey(0)
cv2.destroyAllWindows()
#cv2.imshow(image)

