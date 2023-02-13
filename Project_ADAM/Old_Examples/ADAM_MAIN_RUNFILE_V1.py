
import json
import tkinter
from ADAM_SPEECH_ENGINE import ADAM_SPEECH_V1

###Import Adam_Modules###'
from ADAM_ASSIST_HANDOFF import *

#########################

se = ADAM_SPEECH_V1()
             



class ADAM_GUI_V1:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.geometry("800x900")
        self.main_window.title("ADAM: ADVANCED DECISION ASSISTANCE MACHINE| BASIC GUI MK.1")
        


        



        self.text_speaking_frame = tkinter.Frame(self.main_window)
        
        # this frame will have a entry box allowing the user to interact with ADAM and call specific commands
        self.entry_frame = tkinter.Frame(self.main_window)

        self.ADAM_LABEL = tkinter.StringVar()

        self.ADAM_LABEL.set("Welcome To ADAM Basic")

        
        

        self.label_speak = tkinter.Label(self.text_speaking_frame, textvariable = self.ADAM_LABEL)      # self.text will hold the welcome text as well as be the text for ADAM to talk back to you from
        self.ADAM_text_variable = str("")
        self.__entry_box = tkinter.Entry(self.entry_frame)
        
        self.begin_search = tkinter.Button(self.entry_frame, text="Begin Search", command = self.set_entry_brain)


        self.label_speak.pack()
        self.__entry_box.pack()
        self.begin_search.pack()


        self.text_speaking_frame.pack()
        self.entry_frame.pack()
        tkinter.mainloop()

    def get_entry_text(self):
        return self.ADAM_LABEL 



#######SEARCHENGINE#######################################################################################################################################################################################       



    def set_entry_brain(self):

        print("passed into")

        self.user_entry = str(self.__entry_box.get())
        

        with open('Project_ADAM/ADAM_AI_STORAGE/ADAMSE_DECISION_V1.txt', 'r') as filehandle:
            ADAM_SEARCH_QUERIES_DECISION = json.load(filehandle)
        

        with open('Project_ADAM/ADAM_AI_STORAGE/ADAMSE_ASSISTANCE_V1.txt', 'r') as filehandle:
            ADAM_SEARCH_QUERIES_ASSISTANCE = json.load(filehandle)
        

        
        # for every item in the test list, do an action
        for d in ADAM_SEARCH_QUERIES_DECISION:
            if d in self.user_entry:
                print("DECIDING")
                self.top_decide = tkinter.Toplevel()

                self.test_frame2 = tkinter.Frame(self.top_decide)
                self.test_label2 = tkinter.Label(self.test_frame2, text="cheeseburgerz")
                self.test_label2.pack()
                self.test_frame2.pack()
                
                break
        for a in ADAM_SEARCH_QUERIES_ASSISTANCE:
            if a in self.user_entry:
                print("AIDING")
                Assist_window = Assist_Module_MK1()
                Assist_window.open_assistance_window()

                
                
                break
                
                
                
        

        


        
  
        
        

        

           









############################################################################################################################################################################################################################################################################################################################


start_ADAM = ADAM_GUI_V1()

