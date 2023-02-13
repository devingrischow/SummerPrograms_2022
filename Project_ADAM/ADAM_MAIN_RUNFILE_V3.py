
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
from ADAM_ADAM_MODULE_V1 import *
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
        self.ask_ADAM = tkinter.Button(self.microphone_frame, text="ADAM", command = lambda: ads.open_skills())


        
        self.ask_ADAM.pack()

        self.microphone_frame.pack()
        
        tkinter.mainloop()





     
class ADAM_SKILLS:
    se = ADAM_SPEECH_V1()
    
    ad = 'Hello and Welcome to Adam: ADVANCED DESIGN ASSISTANCE MACHINE'
    se.speaking_engine(ad)
    sr = Speech_recon()   
    
    

        
    def __init__(self, speaking_text= sr.get_audio_text()):

        self.speaking_text = speaking_text




    def open_skills(self):  
        se = ADAM_SPEECH_V1()
        sr = Speech_recon()
        help = "What would you like assistance with?"
        se.speaking_engine(help)
        sr.start_voice_recognition()
        self.speech_text = sr.get_audio_text()
        print("You said: " + self.speech_text)
        

        if "class" in self.speech_text:                
                    
            d = Class_Assist()
            d.class_assist_start()
            ct = 'Preparing Programming assist module'
            se.speaking_engine(ct)        
        elif "programming" in self.speech_text:
            #################################################################################################
            p = Basic_programing_Assist()
            p.basic_programming_help()
            ct = 'Preparing Programming assist module'
            se.speaking_engine(ct)

        elif "Adam" or "atom" in self.speech_text:
            ad = ADAM_ADAM_ASSIST()
            ad.adam_assist_start()
            ads = "Preparing ADAM module assistance module"
            se.speaking_engine(ads)

        else:
            ur = "sorry I cannot do that"
            se.speaking_engine(ur)

            

       














        
        
adb = ADAM_ACCESS_BUTTON()
adb()
   
            
            

            


    



            
            
        
                
           
        

    


