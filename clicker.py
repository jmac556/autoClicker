import pyautogui
import time

def clicker():

	#This is for the primary monitor
	width, height = 1170, 855



	#width, height = 4294966559, 881
	#Prints current cordinates of mouse
	#print(pyautogui.position())
	#Prints current in width/height
	#print(width, height)



	pyautogui.click(width, height)

while True:
	clicker()
	time.sleep(25)