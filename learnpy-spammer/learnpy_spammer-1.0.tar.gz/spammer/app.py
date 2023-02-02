import pyautogui
import time

message="yeah, and"
time.sleep(0.00001)
for _ in range(100):
    pyautogui.write(message)
    pyautogui.press('enter')