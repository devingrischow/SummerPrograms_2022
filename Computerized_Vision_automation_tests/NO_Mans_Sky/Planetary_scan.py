"""
This program is designed to scan for specific systems you can searcg from
"""

from pyautogui import *
import pyautogui
import time
import keyboard
import random



star_input = input(str("Enter Your Requested Star Type: "))

species_input = input(str("Enter Your Requested Species Type: "))

    


while True:

    
    if star_input == "orange":

        # scanns for the inputed planet
        if pyautogui.pixelMatchesColor(2123, 43,(221 ,189 ,62)) == True:
            print("color is present")
        else:
            print("Color is not present")

    elif star_input == "red":


        if pyautogui.pixelMatchesColor(2123, 43,(221 ,189 ,62)) == True:
            print("color is present")
        else:
            print("Color is not present")

    elif star_input == "green":


        if pyautogui.pixelMatchesColor(2123, 43,(221 ,189 ,62)) == True:
            print("color is present")
        else:
            print("Color is not present")
            
    elif star_input == "blue":


        if pyautogui.pixelMatchesColor(2123, 43,(221 ,189 ,62)) == True:
            print("color is present")
        else:
            print("Color is not present")

