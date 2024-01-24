# 영상분석
# => 동영상 = 이미지의 연속
# pip install pafy pygame
# pip install youtube-dl==2020.12.2

import cv2, pafy


url = 'https://www.youtube.com/watch?v=u_Q7Dkl7AIk'
video = pafy.new(url)
print('title = ', video.title)
print('video.rating = ', video.rating)
print('video.duration = ', video.duration)
best = video.getbest()
# print('best.resolution', best.resolution)
 

# cap=cv2.VideoCapture(0) #0번째 카메라 - 내 pc의 카메라
cap=cv2.VideoCapture(best.url) #비디오캡쳐 도구 사용

while(True):
        retval, frame = cap.read()
        if not retval:
                break
        cv2.imshow('frame',frame)
 
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
        edges = cv2.Canny(gray,100,200) #흑백영상
        cv2.imshow('edges',edges)
 
        key = cv2.waitKey(25) #25/1000초 동안 기다려도 사용자가 입력없으면 재생
        if key == 27: # Esc #재생 중 exc 누르면 끝
                break


cv2.destroyAllWindows()
