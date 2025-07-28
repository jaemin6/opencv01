import cv2

# 이미지 불러오기
image = cv2.imread('../img/like_lenna.png')
image_big = cv2.resize(image, dsize=None, fx=2, fy=2)

# 복사본 만들기 (원본 유지)
img_display = image_big.copy()

text = "handsome guy"
font = cv2.FONT_HERSHEY_TRIPLEX
scale = 1
color = (0, 0, 0)
thickness = 2

# 전역 변수로 텍스트 위치 저장 (초기값)
text_pos = (50, 100)

# 마우스 콜백 함수 정의
def mouse_event(event, x, y, flags, param):
    global img_display, text_pos
    
    if event == cv2.EVENT_LBUTTONDOWN:
        text_pos = (x, y)
        img_display = image_big.copy()  # 이미지 초기화
        cv2.putText(img_display, text, text_pos, font, scale, color, thickness, cv2.LINE_AA)

# 윈도우 생성
cv2.namedWindow("Image with Text")
cv2.setMouseCallback("Image with Text", mouse_event)

# 처음 텍스트 그리기
cv2.putText(img_display, text, text_pos, font, scale, color, thickness, cv2.LINE_AA)

while True:
    cv2.imshow("Image with Text", img_display)
    if cv2.waitKey(1) & 0xFF == 27:  # ESC 키 누르면 종료
        break

cv2.destroyAllWindows()
