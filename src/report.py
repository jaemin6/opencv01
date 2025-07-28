import cv2

# 이미지 불러오기
image = cv2.imread('../img/like_lenna.png')  # 경로는 이미지 위치에 맞게 수정

# 2배 확대
image_big = cv2.resize(image, dsize=None, fx=2, fy=2)

# 이미지 보여주기
cv2.imshow('Zoomed x2 Image', image_big)
cv2.waitKey(0)
cv2.destroyAllWindows()
