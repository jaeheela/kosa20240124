import cv2


# 사람 이미지
template = cv2.imread('./data/wili.png')
th, tw = template.shape[:2]
cv2.imshow('template', template)


# step1) webCAM 이미지 준비
image = cv2.imread('./data/original.jpg')


# step2) 이미지 특징 매칭
result = cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)


# step3) 매칭 좌표를 이미지에 그리기
minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(result)
top_left = maxLoc
match_val = maxVal
bottom_right = (top_left[0] + tw, top_left[1] + th)
cv2.rectangle(image, top_left, bottom_right, (0, 0, 255), 2)
cv2.imshow('Result', image)




cv2.waitKey(0)
cv2.destroyAllWindows()