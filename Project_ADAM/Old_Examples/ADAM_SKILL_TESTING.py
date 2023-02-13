
# foundation for future ADAM integrations
# these parts will be a mix between ADAM_GUI and ADAM MAIN, 
# these sections will either replace the standard welcome text with displayed information, or could possibly open up more TKinter windows,
# it depends on what the user needs help with


import tkinter
from ADAM_SPEECH_ENGINE import ADAM_SPEECH_V1
from ADAM_SPEECH_RECOGNITION_V1 import Speech_recon

###### ASSIST IMPORTS
from ADAM_class_assist_MK1 import *
from ADAM_BASIC_PROGRAMMING_HELP import *
####
import pyperclip
import pickle
import time
import json


class ADAM_ACCESS_BUTTON:
    
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.microphone_frame = tkinter.Frame(self.main_window)
        self.main_window.geometry("200x100")
        self.main_window.title("ADAM Request Window")
        
        ads = ADAM_SKILLS()
        
        self.ask_ADAM = tkinter.Button(self.microphone_frame, text="Begin Search", command = lambda:ads.open_skills())


        
        self.ask_ADAM.pack()

        self.microphone_frame.pack()
        
        tkinter.mainloop()
    



     
class ADAM_SKILLS:
    se = ADAM_SPEECH_V1()
    sr = Speech_recon()
    ad = 'Hello and Welcome to Adam: ADVANCED DECISION ASSISTANCE MACHINE'
    se.speaking_engine(ad)        
    sr.start_voice_recognition()
    

        
    def __init__(self, speaking_text=sr.get_audio_text()):

        self.speaking_text = speaking_text




    def open_skills(self):  
        se = ADAM_SPEECH_V1()
        sr = Speech_recon()
        help = "What would you like assistance with?"
        se.speaking_engine(help)
        sr.start_voice_recognition()
        self.speech_text = sr.get_audio_text()
        

        if "class" in self.speaking_text:                
                    
            d = Class_Assist()
            d.class_assist_start()
            ct = 'Preparing Class assist module'
            se.speaking_engine(ct)
                

        
        if "programming" in self.speaking_text:
            #################################################################################################
            p = Basic_programing_Assist()
            p.basic_programming_help()

        if "adam" in self.speaking_text:
            pass

       



a = ADAM_ACCESS_BUTTON()











        
        
    
            
            

            


    



            
            
        
                
           
        

    


