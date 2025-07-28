import cv2
import numpy as np

# 1. 흰 배경 이미지 만들기 + 텍스트 추가
img = np.ones((300, 600, 3), dtype=np.uint8) * 255
cv2.putText(img, "handsome guy", (100, 150),    
            cv2.FONT_HERSHEY_SIMPLEX,       
            2,                              
            (255, 0, 255),                  
            3,                              
            cv2.LINE_AA)

# 2. 이미지 불러와서 2배 확대
image = cv2.imread('../img/like_lenna.png')  # 이미지 경로 수정
image_big = cv2.resize(image, dsize=None, fx=2, fy=2)


# 5. 보여주기
cv2.imshow("Text + Zoomed Image", combined)
cv2.waitKey(0)
cv2.destroyAllWindows()
