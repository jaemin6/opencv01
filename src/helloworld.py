import cv2
import numpy as np

# 이미지 불러오기
# image = cv2.imread('../img/like_lenna.png')

# new_height = 300
# new_width = 300

# # crop: 이미지의 (50,50)부터 (150,150)까지 잘라서 변수에 저장
# croped_image = image[50:150, 50:150]

# # 잘린 부분을 회색(값 200)으로 채우기 → 원본 이미지에 바로 영향 줌
# croped_image[:] = 200

# # 상하 반전
# image_fliped = cv2.flip(image, 0)

# # 이미지 리사이즈
# resized_image = cv2.resize(image, (new_width, new_height))

# # 2. 2배 확대 (비율로 리사이즈)
# #image_big = cv2.resize(image, dsize=None, fx=2, fy=2)

# # 이미지 보여주기
# cv2.imshow('Original Image', image)
# cv2.imshow('Resized Image (300x300)', resized_image)
# cv2.imshow('Flipped Image (UpDown)', image_fliped)
# cv2.imshow('Modified Image', image)
# #cv2.imshow('Zoomed x2 Image', image_big)

# dst = np.zeros((new_height, new_width), dtype=np.uint8)
# dst = cv2.resize(image, (new_width, new_height))

# #cv2.resize(image, (new_width, new_height), dst=dst)


# print(image.shape)
# print(resized_image.shape)


# cv2.waitKey(0)
# cv2.destroyAllWindows()
# #cv2.imshow(image)

space = np.zeros((500, 1000), dtype=np.uint8)
color = 255
space = cv2.circle(space, (600, 200), 100, color, 4, 1)

#line_color = 255

# 선 그리기: 시작점(100,100), 끝점(800,400), 두께 3, 선 종류 1(8-connected line)
#space = cv2.line(space, (100, 100), (800, 400), line_color, 3, 1)

#cv2.imshow('Line on Space', space)
cv2.imshow('Circle', space)
cv2.waitKey(0)
cv2.destroyAllWindows()
