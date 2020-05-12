import pyautogui
import sys
import time

args = sys.argv[1:]

if len(args) != 1:
	print('Please enter exactly one filename.')
	exit()

with open(args[0]) as file:
	time.sleep(3)
	while True: 
		line = file.readline() 
		if not line: 
			break
		pyautogui.write(line)	
		pyautogui.press("enter")
