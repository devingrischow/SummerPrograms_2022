
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
from ADAM_Research_v1 import *
####
import pyperclip
import pickle
import json




class ADAM_ACCESS_BUTTON:
    se = ADAM_SPEECH_V1()
    
    ad = 'Hello and Welcome to Adam: ADVANCED DESIGN ASSISTANCE MACHINE'
    se.speaking_engine(ad)
    
    def __init__(self):
        self.main_window = tkinter.Tk()
         
        
        self.microphone_frame = tkinter.Frame(self.main_window)  # turns into search button frame
        self.mcEntryframe = tkinter.Frame(self.main_window)
        
        self.main_window.geometry("250x150")
        self.main_window.title("ADAM Request Window")
        
        self.mcEntry = tkinter.Entry(self.mcEntryframe)
        
        self.ask_ADAM = tkinter.Button(self.microphone_frame, text="Search", command = lambda: self.mac_open_skills())


        self.mcEntry.pack()
        self.ask_ADAM.pack()
        

        self.mcEntryframe.pack()
        self.microphone_frame.pack()
        
        
        tkinter.mainloop()



    def mac_open_skills(self):  
        self.lowercased = self.mcEntry.get().lower()
        self.mcentry_text = self.lowercased
        print("--------" + self.mcentry_text + "-----------")
        se = ADAM_SPEECH_V1()

        if "class" in self.mcentry_text:                
                    
            d = Class_Assist()
            d.class_assist_start()
            ct = 'Preparing Programming assist module'
            se.speaking_engine(ct)        
        elif "programming" in self.mcentry_text:
            p = Basic_programing_Assist()
            p.basic_programming_help()
            pm = 'Preparing Programming assist module'
            se.speaking_engine(pm)

        elif "adam" or "atom" in self.mcentry_text:
            ad = ADAM_ADAM_ASSIST()
            ad.adam_assist_start()
            ads = "Preparing ADAM module assistance module"
            se.speaking_engine(ads)

        elif "research" in self.mcentry_text:
            r = ADAM_RESEARCH_ASSIST()
            r.adam_research_start()
            ra = "Preparing ADAM Research Module"       #ra the a means text, so research announcer
            se.speaking_engine(ra)

        else:
            ur = "sorry I cannot do that"
            se.speaking_engine(ur)





m = ADAM_ACCESS_BUTTON()
m


