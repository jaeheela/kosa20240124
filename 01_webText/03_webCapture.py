# pip install selenium
# https://chromedriver.chromium.org/


import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options




options = Options()
options.add_argument('--headless')


driver = webdriver.Chrome(options=options)


url = "http://www.naver.com/"
driver.get(url)
driver.implicitly_wait(2)


driver.get_screenshot_as_file("webCapture.png")


driver.quit()

# => webCapture.png 생성됨