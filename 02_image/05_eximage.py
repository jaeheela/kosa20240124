# pip install opencv-python : open-cv가 numpy에 종속적이라 함께 설치됨
import cv2
import numpy as np
 
imageFile = './data/lena.jpg'
img = cv2.imread(imageFile)
cv2.imshow('Lena color',img)


cv2.imwrite('./data/Lena.bmp', img) # 비트맵으로 저장
cv2.imwrite('./data/Lena.png', img) # png로 저장
cv2.imwrite('./data/Lena2.jpg', img, [cv2.IMWRITE_JPEG_QUALITY, 90]) # JPEG로 저장하는데, 퀄리티 90으로 저장
 
imageFile = './data/Lena.png'
img  = cv2.imread(imageFile, cv2.IMREAD_GRAYSCALE) # 이미지를 읽는데 흑백영상으로 바꿔서 읽기
cv2.imshow('Lena gray',img) #보여줘
 
cv2.waitKey() #사용자가 임의의 키 누를 때까지 기다림
cv2.destroyAllWindows() #클릭하면 모두 종료