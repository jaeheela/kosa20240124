# pyautogui는 GUI 자동화를 위한 라이브러리로, 마우스 및 키보드 이벤트를 시뮬레이트 가능
import time
import pyautogui

def run_putty():
    # Putty 실행 (Putty의 경로에 따라 수정 필요)
    putty_path = r'C:\Program Files\PuTTY\putty.exe'
    pyautogui.hotkey('winleft', 'r')
    pyautogui.write(putty_path)
    pyautogui.press('enter')

    time.sleep(1)  # Putty가 열릴 때까지 잠시 기다립니다.

    # Putty에 접속 정보 입력
    pyautogui.write('175.113.214.98')
    pyautogui.press('tab')  
    pyautogui.write('22')
    pyautogui.press('enter')

    time.sleep(1)  # 접속할 때까지 잠시 기다립니다.

    # 접속한 후 명령어 실행
    pyautogui.write('username!!!')
    pyautogui.press('enter')
    pyautogui.write('password!!!!')
    pyautogui.press('enter')
    
    pyautogui.write('cd promo/was/apache-tomcat-7.0.41/logs')
    pyautogui.press('enter')
    pyautogui.write('tail -f catalina.out')
    pyautogui.press('enter')
    

    # 사용자가 Putty 창을 닫을 때까지 계속 실행
    while True:
        time.sleep(1)
        try:
            # Putty 창이 닫혔는지 확인
            if pyautogui.getWindowsWithTitle('PuTTY Configuration').visible:
                break
        except pyautogui.FailSafeException:
            # 사용자가 마우스를 화면의 왼쪽 상단에 가져다 놓으면 프로그램 종료
            break

if __name__ == "__main__":
    run_putty()
