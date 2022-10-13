import pyautogui as gui
import time

n = 1000 #int(input('So luong: '))
time.sleep(10)

for i in range(n):
	str = ''
	i = i + 1
	message = f'{i} {str}'
	gui.typewrite(message)
	gui.press('Enter')