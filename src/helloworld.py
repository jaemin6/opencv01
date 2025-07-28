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

# 컬러 입히기
space = np.zeros((768, 1388, 3), dtype=np.uint8)

#space = np.zeros((768, 1388), dtype=np.uint8)
# color = 255
# obj1 = np.array([[300, 500], [500, 500], [400, 600], [200, 600]])
# obj2 = np.array([[600, 500], [800, 500], [700, 200]])
# #space = cv2.circle(space, (600, 200), 100, color, 4, 1)

# space = cv2.polylines(space, [obj1], True, color, 3)
# space = cv2.fillPoly(space, [obj2], color)

grid_spacing = 50
colors = [
    (255, 0, 0),     # 파랑
    (255, 165, 0),   # 주황
    (255, 255, 0),   # 노랑
    (0, 255, 0),     # 초록
    (0, 255, 255),   # 하늘
    (0, 0, 255),     # 빨강
    (255, 0, 255),   # 보라
]
#grid_color = (0, 255, 255)
#grid_color = 225

#for x in range(0, space.shape[1], grid_spacing):
#    cv2.line(space, (x, 0), (x, space.shape[0]), grid_color, 1)

#for y in range(0, space.shape[0], grid_spacing):
#    cv2.line(space, (0, y), (space.shape[1], y), grid_color, 1)

# 세로선 (x축)
for idx, x in enumerate(range(0, space.shape[1], grid_spacing)):
    color = colors[idx % len(colors)]
    cv2.line(space, (x, 0), (x, space.shape[0]), color, 1)

# 가로선 (y축)
for idx, y in enumerate(range(0, space.shape[0], grid_spacing)):
    color = colors[idx % len(colors)]
    cv2.line(space, (0, y), (space.shape[1], y), color, 1)

#line_color = 255

# 선 그리기: 시작점(100,100), 끝점(800,400), 두께 3, 선 종류 1(8-connected line)
#space = cv2.line(space, (100, 100), (800, 400), line_color, 3, 1)

#cv2.imshow('Line on Space', space)
#cv2.imshow('Circle', space)
#cv2.imshow('Polygons', space)
cv2.imshow("Color Grid", space)
cv2.waitKey(0)
cv2.destroyAllWindows()
