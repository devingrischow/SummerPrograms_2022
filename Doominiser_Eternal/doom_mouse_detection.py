"""
This part of the program detects the clicks from the users mouse and then activates the weapon switcher
This will only occur when not in standby mode however
Standby mode is going to be in a while loop, and if the user has not turned on standby mode, then nothing will happen. 
when in standby mode, weapon switching will occur. 
"""



from doom_main import *
from pynput.mouse import Listener
from pynput.keyboard import Key,Controller
import time
import win32api
import keyboard




class Simulate_clicks:
    standby = 0
    random_weapon_number_generated = Active_weapons_switcher.random_number_generator()        
    i = Active_weapons_switcher(random_weapon_number_generated)
    print("Press CTRL + C to stop program")


    x = input("Press K to begin ")
    if x == "k":
        time.sleep(4)
        standby += 1
        print("Begin The Rippin and the Randomizin")
        while standby == 1:
            shoot = win32api.GetKeyState(0x01)
            keyboarded = Controller()
            state_left = win32api.GetKeyState(0x01)

            if shoot != state_left:
                state_left = shoot
                if shoot >= 0:
                    a = i.get_weapon_key()
                    if a == 1 or a == 4 or a == 5 or a == 6:
                        print(("-----")*5)
                        print("Current gun is: " + str(i.get_weapon_key()))
                        time.sleep(.5)     
                        keyboarded.press(str(a))
                        keyboarded.release(str(a))
                        i.generate_new_numbers(Active_weapons_switcher.random_number_generator())
                        
                        print("New Gun is: " + str(i.get_weapon_key()))
                        print(("-----")*5)
                    else:
                        pass

                elif shoot < 0:
                    a = i.get_weapon_key()
                    if a == 2 or a == 3 or a == 7:
                        print(("-----")*5)
                        print("Current gun is: " + str(i.get_weapon_key()))
                        time.sleep(3)
                        keyboarded.press(str(a))
                        keyboarded.release(str(a))
                        i.generate_new_numbers(Active_weapons_switcher.random_number_generator())
                        print("New Gun is: " + str(i.get_weapon_key()))
                        print(("-----")*5)
                    else:
                        pass
            
    
    
                        
        else:
            pass



g = Simulate_clicks()
g