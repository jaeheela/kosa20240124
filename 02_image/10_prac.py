# 영상에 선과 사각형 그리기
import cv2, pafy
import numpy as np



url = 'https://www.youtube.com/watch?v=u_Q7Dkl7AIk'
video = pafy.new(url)
print('title = ', video.title)
print('video.rating = ', video.rating)
print('video.duration = ', video.duration)
best = video.getbest()
print('best.resolution', best.resolution)
# print('best.url', best.url)

cap=cv2.VideoCapture(best.url) #비디오캡쳐 도구 사용

while(True):
        retval, frame = cap.read()
        if not retval:
                break
        cv2.imshow('original',frame)
 
 
        # 선과 사각형 그리기
        pt1 = 100, 100
        pt2 = 300, 300
        cv2.rectangle(frame, pt1, pt2, (0, 255, 0), 10) #초록색 사각형, 마지막은 굵기
        cv2.line(frame, (0, 0), (400, 0), (255, 0, 0), 10) #빨간색 선
        cv2.line(frame, (0, 0), (0, 400), (0,0,255), 10) #파란색 선
        frame[10:50, 10:50] = 0 # 특정 영역의 색상 변경 - 0~50을 검정으로
        # 텍스트 출력
        font = cv2.FONT_HERSHEY_SIMPLEX
        text = "Hello"
        cv2.putText(frame, text, (300, 300), font, 1, (255, 255, 255), 4)


        cv2.imshow('exYouTube_draw',frame)
 

        key = cv2.waitKey(25) #25/1000초 동안 기다려도 사용자가 입력없으면 재생
        if key == 27: # Esc #재생 중 exc 누르면 끝
                break


cv2.destroyAllWindows()