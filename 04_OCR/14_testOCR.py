# pip install speechrecognition
# pip install gTTs  
# pip install playsound==1.2.2
# pip install pillow
# pip install pytesseract


from PIL import Image
import pytesseract
import speech_recognition as sr
from gtts import gTTS
import playsound


filename = '.\data\sound.mp3'
def speak(text):
     tts = gTTS(text=text, lang='ko')
     tts.save(filename)
     playsound.playsound(filename)


# => https://github.com/UB-Mannheim/tesseract/wiki 에서 tesseract OCR 다운
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract'


myConfig = ('-l kor --oem 3 --psm 4')
str = pytesseract.image_to_string(Image.open('.\data\sample.jpg'), config=myConfig)


print(str)
speak(str)
