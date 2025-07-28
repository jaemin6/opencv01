import cv2
import numpy as np

# 이미지 불러오기
image = cv2.imread('../img/like_lenna.png')
image_big = cv2.resize(image, dsize=None, fx=2, fy=2)

img_display = image_big.copy()

text = "handsome guy"
font = cv2.FONT_HERSHEY_TRIPLEX
scale = 1
thickness = 2

text_pos = (50, 100)

# 색상 변화를 위한 함수 (RGB 튜플 생성)
def color_animation(t):
    # t: 0~255 사이 값, RGB 색상이 천천히 변하게 만듦
    r = (t * 2) % 256
    g = (255 - t * 3) % 256
    b = (128 + t * 5) % 256
    return (b, g, r)  # OpenCV는 BGR 순서

# 마우스 콜백 함수 (텍스트 위치 변경)
def mouse_event(event, x, y, flags, param):
    global img_display, text_pos
    if event == cv2.EVENT_LBUTTONDOWN:
        text_pos = (x, y)

cv2.namedWindow("Image with Text")
cv2.setMouseCallback("Image with Text", mouse_event)

t = 0  # 색상 변화 인자

while True:
    img_display = image_big.copy()  # 초기화
    
    # 현재 색상 계산
    color = color_animation(t)
    
    # 텍스트 쓰기
    cv2.putText(img_display, text, text_pos, font, scale, color, thickness, cv2.LINE_AA)
    
    cv2.imshow("Image with Text", img_display)
    
    t = (t + 1) % 256  # 색상 순환
    
    if cv2.waitKey(30) & 0xFF == 27:  # ESC 키 누르면 종료
        break

cv2.destroyAllWindows()
