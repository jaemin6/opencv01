import cv2
import numpy as np

# 흰 배경 이미지 만들기
img = np.ones((300, 600, 3), dtype=np.uint8) * 255

cv2.putText(img, "sexy guy", (100, 150),    # 위치(x, y)
            cv2.FONT_HERSHEY_SIMPLEX,       # 폰트
            2,                              # 글자 크기 (scale)
            (255, 0, 255),                  # 색상 (보라색)
            3,                              # 두께
            cv2.LINE_AA)   

# 이미지 불러오기
#image = cv2.imread('../img/like_lenna.png')  # 경로는 이미지 위치에 맞게 수정

# 2배 확대
#image_big = cv2.resize(image, dsize=None, fx=2, fy=2)

# 이미지 보여주기
#cv2.imshow('Zoomed x2 Image', image_big)
cv2.imshow("Sexy Text", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
