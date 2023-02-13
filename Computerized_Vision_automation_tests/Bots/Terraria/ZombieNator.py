
from pyautogui import *
import pyautogui
import keyboard
import win32api
import win32con
from pathlib import Path


class ZombieKill:


    def __init__(self, X=1):
        self.X = X


    def search_ground_zombie_night(self):
        while keyboard.is_pressed('o') == False:

            try:

                # get the path/directory
                __folder_path = 'D:\Summer_Programs_2021\Computerized_Vision_automation_tests\Bots\Terraria\Zombie_Sprites_folder'
                images = Path(__folder_path).glob('*.png')
                for __folder_path in images:
                    xb,yb = pyautogui.locateOnScreen(__folder_path,region=(6,389,2538,972), grayscale = False, confidence=.7)
                    print(f'I can see it at: {xb}x{yb}')
                    click(xb,yb)
                	
                
            except TypeError:
                print("I Cant See" + str(__folder_path)) 

                




def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)



__start_zombie_kill = ZombieKill()
__loop_input = input("Type 'die' to begin")
while __loop_input == "die":
    __start_zombie_kill.search_ground_zombie_night()












# xb,yb = pyautogui.locateCenterOnScreen(r'D:\Summer_Programs_2021\Computerized_Vision_automation_tests\Bots\Terraria\20220906220716_1.png',region = , grayscale = True, confidence=.7)