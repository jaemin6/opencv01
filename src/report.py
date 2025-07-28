import cv2
import numpy as np

# 1. 이미지 불러오기
image = cv2.imread('../img/like_lenna.png')  # 이미지 경로 수정
image_big = cv2.resize(image, dsize=None, fx=2, fy=2)

# 2. 이미지 위에 텍스트 추가
cv2.putText(image_big, "handsome guy", (50, 100),         # 위치(x, y)
            cv2.FONT_HERSHEY_TRIPLEX,                     # 폰트 종류
            1,                                            # 글자 크기
            (0, 0, 0),                                # 색 (보라색)
            1,                                            # 두께
            cv2.LINE_AA)                                  # 선 형태

# 3. 보여주기
cv2.imshow("Image with Text", image_big)
cv2.waitKey(0)
cv2.destroyAllWindows()
