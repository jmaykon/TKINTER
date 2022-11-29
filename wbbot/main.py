import pyautogui,webbrowser
from time import sleep


webbrowser.open("https://web.whatsapp.com/send?phone=+59168150129")
sleep(10)


pyautogui.typewrite("hola como estas")
pyautogui.press("enter")