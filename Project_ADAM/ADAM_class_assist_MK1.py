import tkinter
import pyperclip
import pickle
from ADAM_SPEECH_ENGINE import ADAM_SPEECH_V1
from ADAM_SPEECH_RECOGNITION_V1 import Speech_recon
import time
import json

class Class_Assist:
    
    
    def class_assist_start(self):
        # ADAM speech and sr must be located near the top. 
        se = ADAM_SPEECH_V1()
        

        
        
                
                    ####################################################################################################################################################################################
        self.class_assist_window_1 = tkinter.Tk() # creates another window for ADAM
        self.class_frame1 = tkinter.Frame(self.class_assist_window_1)
        self.button_frame_left = tkinter.Frame(self.class_assist_window_1)
        self.bottom_frame = tkinter.Frame(self.class_assist_window_1)

        self.class_assist_window_1.geometry('500x300+900+300')

        self.assistance_label1= tkinter.StringVar()

        self.assistance_label1.set("Help Modules")
        self.class_assist_window_1.title("Class Assist")
        self.label_assist_setting = tkinter.Label(self.class_frame1, textvariable = self.assistance_label1)  
        

        
        
        
        # load Data file into copy_paste storage, handles OS differences
        try:
            
            file_open= open('copy_paste_storage_CLASS_ASSIST.dat', 'r+b')
            self.copy_paste_storage = pickle.load(file_open)
            file_open.close()
            print("load window way")
        except FileNotFoundError:
            file_open= open('Project_ADAM/STORAGE/copy_paste_storage_CLASS_ASSIST.dat', 'r+b')
            self.copy_paste_storage = pickle.load(file_open)
            file_open.close()
            print('load mac way')
        except EOFError:
            print("excepted")
            self.copy_paste_storage = {}
        


        # gets self.
        try:
            self.c1 = self.copy_paste_storage['c1']
        except:
            print("Key Not Recognized")


        try:
            self.c2 = self.copy_paste_storage['c2']
        except:
            print("Key Not Recognized")
        
        try:
            self.c3 = self.copy_paste_storage['c3']
        except:
            print("Key Not Recognized")

        
        try:
            self.c4 = self.copy_paste_storage['c4']
        except:
            print("Key Not Recognized")

        # entire class demo with objects

        try:
            self.c5 = self.copy_paste_storage['c5']
        except:
            print("Key Not Recognized")


        ####
        
        self.self_help_button = tkinter.Button(self.button_frame_left,text="Copy: self", command= lambda: self.action_button(self.c1))
        self.getter_example_button = tkinter.Button(self.button_frame_left, text="Copy: get_attribute example", command= lambda: self.action_button(self.c2))
        self.setter_example_button = tkinter.Button(self.button_frame_left, text="Copy: set_attribute example", command= lambda:self.action_button(self.c3))
        self.demo_button = tkinter.Button(self.button_frame_left, text="Copy: Class Demo", command= lambda:self.action_button(self.c4))
        self.string_returning_demo = tkinter.Button(self.button_frame_left, text="Copy: String Printing function", command= lambda:self.action_button(self.c5))
        
        self.open_data_entry_window = tkinter.Button(self.bottom_frame, text='Open data window', command= lambda: self.data_window_classes())
        
        



        self.label_assist_setting.pack()
        self.self_help_button.pack()
        self.getter_example_button.pack()
        self.setter_example_button.pack()
        self.string_returning_demo.pack()
        self.open_data_entry_window.pack(side='bottom')
        self.demo_button.pack()
        self.class_frame1.pack()
        self.button_frame_left.pack(side='left')
        self.bottom_frame.pack(side='bottom')
        tkinter.mainloop()
        


        

        

                    ################################################################


    def action_button(self, text_placeholder):
        
        pyperclip.copy(text_placeholder)
        self.assistance_label1.set("Action has been Preformed")


    def data_window_classes(self):




        try:
            
            file_open= open('copy_paste_storage_CLASS_ASSIST.dat', 'r+b')
            self.copy_paste_storage = pickle.load(file_open)
            file_open.close()
            print("load Mac way")
        except FileNotFoundError:
            
                
            file_open= open('Project_ADAM/STORAGE/copy_paste_storage_CLASS_ASSIST.dat', 'r+b')
            self.copy_paste_storage = pickle.load(file_open)
            file_open.close()
            print('load windows way')
            
        except EOFError:
            print("excepted")
            self.copy_paste_storage = {}

    
    def ask_ADAM(self):
        sr = Speech_recon()
        sr.start_voice_recognition()
        speak_text = sr.get_audio_text()

        


        # try:
        #     input_file = open('Project_ADAM\STORAGE\copy_paste_storage_CLASS_ASSIST.dat', 'r+b')
        #     self.copy_paste_storage = pickle.load(input_file)
        #     input_file.close()
        # except(IOError, AttributeError, EOFError):
        #     self.copy_paste_storage = {}
        
            


        #  initialize the first dictionary and open it
        self.__data_class_window = tkinter.Toplevel() # creates another window for ADAM
        self.__data_frame = tkinter.Frame(self.__data_class_window)

        self.data_label = tkinter.Label(self.__data_frame, text='Enter data to be copied and pasted, Be careful as the data is stored in a DAT file, making data unreadible in file form')


        self.data_key_entry = tkinter.Entry(self.__data_frame)
        self.data_entry_box = tkinter.Text(self.__data_frame, width=80, height=25)
        self.convert_data_button = tkinter.Button(self.__data_frame, text="convert text to dictionary and append to dat file", command= lambda: self.append_data_to_file())

                
            
                

        self.data_label.pack()
        self.data_key_entry.pack()
        self.data_entry_box.pack()
        self.convert_data_button.pack()
                
        self.__data_frame.pack()
    

    def append_data_to_file(self):
        self.__data_key = self.data_key_entry.get()
        self.original_DATA_entry = self.data_entry_box.get("1.0", tkinter.END)
        
        try:
            call_name = self.__data_key
            code = self.original_DATA_entry
            self.copy_paste_storage[call_name] = code
            save_to_file = open('Project_ADAM\STORAGE\copy_paste_storage_CLASS_ASSIST.dat', "r+b")
            pickle.dump(self.copy_paste_storage, save_to_file)
            save_to_file.close()
        except FileNotFoundError:
            save_to_file = open('Project_ADAM\STORAGE\copy_paste_storage_CLASS_ASSIST.dat', "wb")
            pickle.dump(self.copy_paste_storage, save_to_file)
            save_to_file.close()

        print('action preformed')