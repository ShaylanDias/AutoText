import pyautogui
import sys
import time
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('filename')
parser.add_argument('-t', required=False, type=int)
parser.add_argument('--byline', action='store_true', required=False)

args = parser.parse_args()
time_delay = 3 if args.t is None else args.t
by_line = args.byline

with open(args.filename) as file:
	time.sleep(time_delay)
	while True: 
		line = file.readline() 
		if not line: 
			break
		if not by_line:
			for blob in line.split():
				pyautogui.write(blob)	
				pyautogui.press("enter")
		else:
			pyautogui.write(line)	
			pyautogui.press("enter")
