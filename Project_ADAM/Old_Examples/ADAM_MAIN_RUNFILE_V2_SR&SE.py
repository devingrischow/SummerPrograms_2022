
# foundation for future ADAM integrations
# these parts will be a mix between ADAM_GUI and ADAM MAIN, 
# these sections will either replace the standard welcome text with displayed information, or could possibly open up more TKinter windows,
# it depends on what the user needs help with

from telnetlib import SE
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





class Assist_Module_MK1:



    # def open_assistance_window(self):

    #     self.top_assitance = tkinter.Toplevel()

    #     self.test_frame = tkinter.Frame(self.top_assitance)


    #     # 500x100 size, first number +400 does left to right, second number(+300) does up and down
    #     self.top_assitance.geometry("500x100+400+300")


    #     self.assistance_label= tkinter.StringVar()

    #     self.assistance_label.set("What would you like assistance with?")

    #     self.label_assist_speak = tkinter.Label(self.test_frame, textvariable = self.assistance_label)  

    #     self.entry_box_assist = tkinter.Entry(self.test_frame)

    #     self.search = tkinter.Button(self.test_frame, text="Search", command = self.ADAM_ASSIST_V1)






    #     self.label_assist_speak.pack()
    #     self.entry_box_assist.pack()
        
    #     self.search.pack()
    #     self.test_frame.pack()

        



    def ADAM_ASSIST_V1(self):

    



        se = ADAM_SPEECH_V1()
        sr = Speech_recon()
        ad = 'Hello and Welcome to Adam: ADVANCED DECISION ASSISTANCE MACHINE'
        se.speaking_engine(ad)
        sr.start_voice_recognition()
        self.speech_text = sr.get_audio_text()
        self.ADAM_SKILLS()    





        
        
        # for every item in the test list, do an action
        
        ####PUT CLASS ASSIST HERE###



        
    def ADAM_SKILLS(self):

        if "class" in self.speech_text:                
                
            d = Class_Assist()
            d.class_assist_start()
            ct = 'Preparing Class assist module'
            se.speaking_engine(ct)
            sr.start_voice_recognition()
            

        
        if "programming" in self.speech_text:
            #################################################################################################
            p = Basic_programing_Assist()
            p.basic_programming_help()


        if "adam help" in self.speech_text:
            a = ADAM_Assist_V1()
            a.adam_assist_open()



ADAM = Assist_Module_MK1()
ADAM.ADAM_ASSIST_V1()



        













        
        
    
            
            

            


    



            
            
        
                
           
        

    


