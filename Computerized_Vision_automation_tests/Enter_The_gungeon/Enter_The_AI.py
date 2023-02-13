from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

time.sleep(3)
print('begin')



# pyautogui.displayMousePosition()  



dodge_screen = pyautogui.screenshot('diabetes.png',region=(1192,592,400,400))

# scan screen check



class Game:


    def __init__(self, bullet_enemy=None, evil_Ghost_AK=None, shotgun_enemies=None, red_slime_basic=None, evil_knight_face=None):
        self.bullet_enemy = bullet_enemy
        self.evil_Ghost_AK = evil_Ghost_AK
        self.shotgun_enemies = shotgun_enemies
        self.red_slime_basic = red_slime_basic            
        self.evil_knight_face = evil_knight_face


    # set
    def scan_screen(self):
        if keyboard.is_pressed('y'):
            print('BEGIN SCAN')


            


           
            # bullet enemy check
            if pyautogui.locateOnScreen('Computerized_Vision_automation_tests\Enter_The_gungeon\Tracked_objects\Bullet_guy.png', confidence=.8) != None:
                self.bullet_enemy = True
                print('located bullet enemy')
            elif pyautogui.locateOnScreen('Computerized_Vision_automation_tests\Enter_The_gungeon\Tracked_objects\Bullet_basic_back.png', confidence=.8) != None:
                self.bullet_enemy = True
                print('located bullet enemy')

            # ghost enemy check
            if pyautogui.locateOnScreen('Computerized_Vision_automation_tests\Enter_The_gungeon\Tracked_objects\Evil_ghost_face.png', confidence=.8) != None:
                self.evil_Ghost_AK = True
                print('located ghost enemy')
            elif pyautogui.locateOnScreen('Computerized_Vision_automation_tests\Enter_The_gungeon\Tracked_objects\ghost_guy_back.png', confidence=.8) != None:
                self.evil_Ghost_AK = True
                print('located ghost enemy')

            # shotgun enemy check
            if pyautogui.locateOnScreen('Computerized_Vision_automation_tests\Enter_The_gungeon\Tracked_objects\Shotgun_guy.png',grayscale=True, confidence=.8) != None:
                self.shotgun_enemies = True
                print('located shotgun enemy')
            elif pyautogui.locateOnScreen('Computerized_Vision_automation_tests\Enter_The_gungeon\Tracked_objects\Shotgun_back.png',grayscale=True, confidence=.8) != None:
                self.shotgun_enemies = True
                print('located shotgun enemy')

            # slime check
            if pyautogui.locateOnScreen('Computerized_Vision_automation_tests\Enter_The_gungeon\Tracked_objects\Red_slime_gungeon.png', confidence=.8) != None:
                self.red_slime_basic = True
                print('located slime enemy')


            # knight check
            if pyautogui.locateOnScreen('Computerized_Vision_automation_tests\Enter_The_gungeon\Tracked_objects\Evil_knight.png', confidence=.8) != None:
                self.evil_knight_face = True
                print('located knight enemy')
        else:
            press("no scan requested")

                

            

        

        

        


        # main loop
    def main_loop(self):
        while keyboard.is_pressed('q') == False:
            self.scan_screen()
            
            self.attack()

            self.dodge_bullets()

    

            



    def attack(self):
        print("KILL")
        print(self.bullet_enemy)
        print(self.evil_Ghost_AK)
        print(self.red_slime_basic)
        print(self.shotgun_enemies)
        print(self.evil_knight_face)

        if self.bullet_enemy == True:
            self.aim_at_basic()
        elif self.evil_Ghost_AK == True:
            self.kill_ghost()
        elif self.shotgun_enemies== True:
            self.kill_shotgun()
        elif self.red_slime_basic == True:
            self.kill_slime()
        elif self.evil_knight_face == True:
            self.kill_knight()
            
            

        




    def click(self,x,y):
        win32api.SetCursorPos((x,y))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
        time.sleep(0.01)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)




    def aim_at_basic(self):
        #bullet guy
        try:
            xa,ya = pyautogui.locateCenterOnScreen('Computerized_Vision_automation_tests\Enter_The_gungeon\Tracked_objects\Bullet_guy.png',grayscale = True, confidence=.8)
            print(f'I can see it at: {xa}x{ya}')
            self.click(xa,ya)
            self.click(xa,ya)
            self.click(xa,ya)
            self.click(xa,ya)
            self.click(xa,ya)

        except TypeError:
            print("No Basic Bullet Enemy")

        
        try:
            xa,ya = pyautogui.locateCenterOnScreen('Computerized_Vision_automation_tests\Enter_The_gungeon\Tracked_objects\Bullet_basic_back.png',grayscale = True, confidence=.8)
            print(f'I can see it at: {xa}x{ya}')
            self.click(xa,ya)
            self.click(xa,ya)
            self.click(xa,ya)
            self.click(xa,ya)
            self.click(xa,ya)

        except TypeError:
            print("No Basic Bullet Enemy")


    def kill_shotgun(self):
      
        #shotgun guy
        try:
            xb,yb = pyautogui.locateCenterOnScreen('Computerized_Vision_automation_tests\Enter_The_gungeon\Tracked_objects\Shotgun_guy.png',grayscale = True, confidence=.8)
            print(f'I can see it at: {xb}x{yb}')
            self.click(xb,yb)
            self.click(xb,yb)
            self.click(xb,yb)
            self.click(xb,yb)
            self.click(xb,yb)

        except TypeError:
            print("No Shotgun face")

    #shotgun guy back
        try:
            xb,yb = pyautogui.locateCenterOnScreen('Computerized_Vision_automation_tests\Enter_The_gungeon\Tracked_objects\Shotgun_back.png',grayscale = True, confidence=.8)
            print(f'I can see it at: {xb}x{yb}')
            self.click(xb,yb)
            self.click(xb,yb)
            self.click(xb,yb)
            self.click(xb,yb)
            self.click(xb,yb)

        except TypeError:
            print("No Shotgun back")

        

    def kill_ghost(self):
   
            #  ghost faced
        try:
            xgf,ygf = pyautogui.locateCenterOnScreen('Computerized_Vision_automation_tests\Enter_The_gungeon\Tracked_objects\Evil_ghost_face.png', confidence=.8)
            print(f'I can see it at: {xgf}x{ygf}')
            self.click(xgf,ygf)
            self.click(xgf,ygf)
            self.click(xgf,ygf)
            self.click(xgf,ygf)
            self.click(xgf,ygf)
        except TypeError:
            print("No Ghost Face")

            # ghost back
        try:
            xgb,ygb = pyautogui.locateCenterOnScreen('Computerized_Vision_automation_tests\Enter_The_gungeon\Tracked_objects\ghost_guy_back.png', confidence=.8)
            print(f'I can see it at: {xgb}x{ygb}')
            self.click(xgb,ygb)
            self.click(xgb,ygb)
            self.click(xgb,ygb)
            self.click(xgb,ygb)
            self.click(xgb,ygb)
        except TypeError:
            print("No Ghost Back")
        
       




    def kill_knight(self):
        # knight face                                                    
        try:
            xkf,ykf = pyautogui.locateCenterOnScreen('Computerized_Vision_automation_tests\Enter_The_gungeon\Tracked_objects\Evil_knight.png', confidence=.8)
            print(f'I can see it at: {xkf}x{ykf}')
            self.click(xkf,ykf)
            self.click(xkf,ykf)
            self.click(xkf,ykf)
            self.click(xkf,ykf)
            self.click(xkf,ykf)
        except TypeError:
            print("No Knight Face")

        
    def kill_slime(self):
        # slime face                                                 
        try:
            xlf,ylf = pyautogui.locateCenterOnScreen('Computerized_Vision_automation_tests\Enter_The_gungeon\Tracked_objects\Red_slime_gungeon.png', confidence=.8)
            print(f'I can see it at: {xlf}x{ylf}')
            self.click(xlf,ylf)
            self.click(xlf,ylf)
            self.click(xlf,ylf)
            self.click(xlf,ylf)
            self.click(xlf,ylf)
        except TypeError:
            print("No Knight Face")










    def dodge_bullets(self):

        # dodge red_bullet    
        if pyautogui.locateOnScreen('Computerized_Vision_automation_tests\Enter_The_gungeon\Tracked_objects\Bullet.pn                                                                                                                                                                                                                                                                                                                      g',region=(1192,592,400,400), confidence=.8) != None:
            keyboard.press("shift")
            time.sleep(.2)
            keyboard.release('shift')
            print("dodge red bullet")

        else:
            print("no red bullet")


    def dodge_chain(self):
        #dodge chain
        if pyautogui.locateOnScreen('Computerized_Vision_automation_tests\Enter_The_gungeon\Tracked_objects\Chain.png',region=(1192,592,400,400), confidence=.8) != None:
            keyboard.press("shift")
            time.sleep(.2)
            keyboard.release('shift')
            print("dodge chain")

        else:
            print("no chain")


    def dodge_fire(self):
        #dodge fire
        if pyautogui.locateOnScreen('Computerized_Vision_automation_tests\Enter_The_gungeon\Tracked_objects\Fire_dodge.png',region=(1192,592,400,400), confidence=.8) != None:
            keyboard.press("shift")
            time.sleep(.2)
            keyboard.release('shift')
            print("dodge fire")

        else:
            print("no fire")





g = Game()
g.main_loop()