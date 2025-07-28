import cv2
import numpy as np

# 이미지 불러오기
image = cv2.imread('../img/like_lenna.png')
image_big = cv2.resize(image, dsize=None, fx=2, fy=2)

text = "handsome guy"
font = cv2.FONT_HERSHEY_TRIPLEX
scale = 1
thickness = 2
text_pos = (50, 100)

def color_animation(t):
    r = (t * 2) % 256
    g = (255 - t * 3) % 256
    b = (128 + t * 5) % 256
    return (b, g, r)

def mouse_event(event, x, y, flags, param):
    global text_pos
    if event == cv2.EVENT_LBUTTONDOWN:
        text_pos = (x, y)

cv2.namedWindow("Image with Text")
cv2.setMouseCallback("Image with Text", mouse_event)

t = 0
grid_spacing = 50
grid_color = (200, 200, 200)
grid_thickness = 1

while True:
    img_display = image_big.copy()

    # 격자 그리기
    for x in range(0, img_display.shape[1], grid_spacing):
        cv2.line(img_display, (x, 0), (x, img_display.shape[0]), grid_color, grid_thickness)
    for y in range(0, img_display.shape[0], grid_spacing):
        cv2.line(img_display, (0, y), (img_display.shape[1], y), grid_color, grid_thickness)

    # 텍스트 색상 계산
    color = color_animation(t)

    # 텍스트 그리기
    cv2.putText(img_display, text, text_pos, font, scale, color, thickness, cv2.LINE_AA)

    cv2.imshow("Image with Text", img_display)

    t = (t + 1) % 256

    if cv2.waitKey(30) & 0xFF == 27:
        break

cv2.destroyAllWindows()
