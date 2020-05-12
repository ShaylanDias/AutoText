import pyautogui
import sys
import time

args = sys.argv[1:]
time_delay = 3

if len(args) != 1:
	print('Please enter exactly one filename.')
	exit()

with open(args[0]) as file:
	time.sleep(time_delay)
	while True: 
		line = file.readline() 
		if not line: 
			break
		pyautogui.write(line)	
		pyautogui.press("enter")
