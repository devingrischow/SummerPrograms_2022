
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

se = ADAM_SPEECH_V1()
sr = Speech_recon()


class Assist_Module_MK1:



    def open_assistance_window(self):

        self.top_assitance = tkinter.Toplevel()

        self.test_frame = tkinter.Frame(self.top_assitance)


        # 500x100 size, first number +400 does left to right, second number(+300) does up and down
        self.top_assitance.geometry("500x100+400+300")


        self.assistance_label= tkinter.StringVar()

        self.assistance_label.set("What would you like assistance with?")

        self.label_assist_speak = tkinter.Label(self.test_frame, textvariable = self.assistance_label)  

        self.entry_box_assist = tkinter.Entry(self.test_frame)

        self.search = tkinter.Button(self.test_frame, text="Search", command = self.ADAM_ASSIST_V1)






        self.label_assist_speak.pack()
        self.entry_box_assist.pack()
        
        self.search.pack()
        self.test_frame.pack()

        



    def ADAM_ASSIST_V1(self):



        print("passed into")

        self.user_entry_assist = str(self.entry_box_assist.get())
        
        # for every item in the test list, do an action
        
        ####PUT CLASS ASSIST HERE###
        if "class" in self.user_entry_assist:
            d = Class_Assist()
            d.class_assist_start()
        

    
        if "programming" in self.user_entry_assist:
            #################################################################################################
            p = Basic_programing_Assist()
            p.class_assist_start1()


        # if "adam help" in self.user_entry_assist:
        #     a = ADAM_Assist_V1()
        #     a.adam_assist_open()



        













        
        
    
            
            

            


    



            
            
        
                
           
        

    


