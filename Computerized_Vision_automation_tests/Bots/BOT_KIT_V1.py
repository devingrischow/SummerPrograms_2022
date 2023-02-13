"""
This program will test the possibilities of computerizeds vision
RGB Of Healing Cooldown: 97, 7, 23
"""

from tkinter.messagebox import NO
from pyautogui import *
import pyautogui
import time
import keyboard
import random

time.sleep(1)
print('begin')









"""
Demos for computer vision. 

"""

# Region Tester

img = pyautogui.screenshot('region_tester.png',region=(6,389,2538,972))
print('region=(50,40,2500,300)')

# mouse coords display

pyautogui.displayMousePosition()          # displays x y coords and RGB values for every pixel



# tests area for the program 
"""
while keyboard.is_pressed('q') == False:


    if pyautogui.pixelMatchesColor(2123, 43,(221 ,189 ,62)) == True:
        print("color is present")
    else:
        print("Color is not present")


    if pyautogui.locateOnScreen('healing_cooldown.png', confidence=.8) != None:
        print("ON SCREEN")

    else:
        print("NOT ON SCREEN")

"""    