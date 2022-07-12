import pyautogui
import keyboard
from time import sleep

while True:
    sleep(0.5)
    pyautogui.press('enter')
    if keyboard.is_pressed('esc'):
        exit()