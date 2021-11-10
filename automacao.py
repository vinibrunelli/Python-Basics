import pyautogui
import time

pyautogui.press('winleft')
pyautogui.write('firefox')
pyautogui.press('enter')
time.sleep(2)
pyautogui.write('web.whatsapp.com')
pyautogui.press('enter')
time.sleep(9)
pyautogui.press('tab')
pyautogui.write('amor')
pyautogui.press('enter')
time.sleep(1)

pyautogui.hotkey('winleft','d')

pyautogui.moveTo(40, 749)
pyautogui.mouseDown()
pyautogui.moveTo(1194, 744)
pyautogui.hotkey('alt','tab')
time.sleep(2)
pyautogui.mouseUp()
time.sleep(2)
pyautogui.press('enter')