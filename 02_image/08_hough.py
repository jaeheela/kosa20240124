# hough 알고리즘

# 필요한 Module(Library) 임포트
import numpy as np
import cv2 as cv


# 도로 이미지 읽어서 표시
cimg = cv.imread('./data/Roads.png')
cv.imshow('Roads - original', cimg)


# 도로이미지 이진화, 에지 추출 후 표시
img = cv.cvtColor(cimg, cv.COLOR_BGR2GRAY)
_, img = cv.threshold(img, 100, 255, cv.THRESH_BINARY)
img = cv.Canny(img, 50, 200, None, 3)
cv.imshow('Image - binary & edge', img)


# Hough를 이용한 직선 검출
lines = cv.HoughLines(img, 1, np.pi / 180, 150)


# 추출한 선을 원본 이미지 위에 표시
if lines is not None:
    for i in range(0, len(lines)):
        rho = lines[i][0][0]
        theta = lines[i][0][1]
        a = np.cos(theta)
        b = np.sin(theta)
        x = a * rho
        y = b * rho
        pt1 = (int(x + 1000 * (-b)), int(y + 1000 * (a)))
        pt2 = (int(x - 1000 * (-b)), int(y - 1000 * (a)))
        cv.line(cimg, pt1, pt2, (0,0,255), 2)


# 원본 이미지 + Line 표시
cv.imshow('Hough Lines', cimg)


# 사용자 입력키 대기 및 종료
cv.waitKey()
cv.destroyAllWindows()