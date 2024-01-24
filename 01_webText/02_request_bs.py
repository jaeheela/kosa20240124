# pip install requests


import requests
from bs4 import BeautifulSoup


res = requests.get('https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EA%B0%9C%EB%B0%9C%EC%9E%90')
print(res.content)
print("1--------------")

soup = BeautifulSoup(res.content, 'html.parser')


# Title 확인
title = soup.find('title')
print(title.get_text())
print("2--------------")

# 나무위키 찾기
# 선택자를 사용하여 HTML 요소를 가져옵니다.


element = soup.select_one('#main_pack section.sc_new.sp_ntotal._sp_ntotal._prs_sit_4po._fe_root_sit_4po > div > ul > li > div.total_wrap.api_ani_send > div.total_group > div > div > div > a')
# 요소의 텍스트를 출력합니다.
print(element.getText())
print("3--------------")
# element = soup.select_one('//*[@id="main_pack"]/section[1]/div/ul/li/div[1]/div[3]/div/div/div/a')
element = soup.select_one('#main_pack section:nth-of-type(1) div ul li div:nth-of-type(1) div:nth-of-type(3) div div div a')
# 요소의 텍스트를 출력합니다.
print(element.getText())
print("4--------------")

total_tit = soup.find_all( class_ = 'total_tit')
for one in total_tit:
    print(one.getText())