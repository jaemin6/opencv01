import cv2
import numpy as np

# 이미지 불러오기
image = cv2.imread('../img/like_lenna.png')

new_height = 300
new_width = 300

# 이미지 리사이즈
resized_image = cv2.resize(image, (new_width, new_height))

# 이미지 보여주기
cv2.imshow('Original Image', image)
cv2.imshow('Resized Image', resized_image)

dst = np.zeros((new_height, new_width), dtype=np.uint8)
dst = cv2.resize(image, (new_width, new_height))

#cv2.resize(image, (new_width, new_height), dst=dst)


print(image.shape)
print(resized_image.shape)

cv2.waitKey(0)
cv2.destroyAllWindows()
#cv2.imshow(image)

