
import tkinter
import pyperclip
import pickle
from sys import platform



class ADAM_ADAM_ASSIST:

    
    def adam_assist_start(self):
                
                    ####################################################################################################################################################################################
        self.ADAM_window = tkinter.Tk() # creates another window for ADAM
        self.ADAM_window.title("ADAM ASSIST")
        self.ADAM_frame_text = tkinter.Frame(self.ADAM_window)
        self.__button_frame = tkinter.Frame(self.ADAM_window)  # frame to store copy and paste buttons
        self.__explanation_frame = tkinter.Frame(self.ADAM_window)
        
        self.__data_entry_frame = tkinter.Frame(self.ADAM_window)   # stores the data entry frame to enter data

        self.ADAM_window.geometry('550x300+900+300')

        self.__assistance_label_text= tkinter.StringVar()

        self.__assistance_label_text.set("Help Modules")
        self.__assistance_label = tkinter.Label(self.ADAM_frame_text, textvariable = self.__assistance_label_text)  
        ####

       
        
        
        # load Data file dictionary into private copy_paste storage, loads it two different ways, incase opening it on a mac or other operating system
        if platform == "darwin":

            try:
                
                __file_open= open(r'Project_ADAM/STORAGE/copy_paste_storage_CLASS_ASSIST.dat', 'rb')
                self.__copy_paste_storage = pickle.load(__file_open)
                __file_open.close()
            except EOFError:

                print("excepted")
                self.__copy_paste_storage = {}
        elif platform == "Windows":
            
            try:
                
                __file_open= open(r'Project_ADAM/STORAGE/copy_paste_storage_CLASS_ASSIST.dat', 'rb')
                self.__copy_paste_storage = pickle.load(__file_open)
                __file_open.close()
            except EOFError:

                print("excepted")
                self.__copy_paste_storage = {}
        
            
            

        
        # Loads button keys

        try:
            self.ad1 = self.__copy_paste_storage['ad1']
        except:
            print("Copy Key Not Recognized")


        try:
            self.ade1 = self.__copy_paste_storage['ade1']
        except:
            print("Explanation Key Not Recognized")


        try:
            self.ad2 = self.__copy_paste_storage['ad2']
        except:
            print("Key Not Recognized")

        try:
            self.ade2 = self.__copy_paste_storage['abe2']
        except:
            print("Explanation Key Not Recognized")
        
        try:
            self.ad3 = self.__copy_paste_storage['ad3']
        except:
            print("Key Not Recognized")

        try:
            self.ade3 = self.__copy_paste_storage['ade3']
        except:
            print("Explanation Key Not Recognized")

        
        

        

        ###### Buttons
        self.create_new_prg_skill = tkinter.Button(self.__button_frame,text="Copy: New Skill Window", command= lambda: self.__action_button(self.ad1))
        self.create_new_prg_skill_example = tkinter.Button(self.__explanation_frame,text="See Skill Creation Example", command= lambda: self.__explanation_window_open(self.ade1))

        
        self.speaking_engine = tkinter.Button(self.__button_frame, text="Copy: Speech Syntyhesis Example", command= lambda: self.__action_button(self.ad2))
        self.speaking_engine_example = tkinter.Button(self.__explanation_frame, text="See Speech Synthesis Example", command= lambda: self.__explanation_window_open(self.ade2))


        self.speech_recognition = tkinter.Button(self.__button_frame, text="Copy: Speech Recognition Example", command= lambda: self.__action_button(self.ad3))
        self.speech_recognition_example = tkinter.Button(self.__explanation_frame, text="See Speech Recognition Example", command= lambda: self.__explanation_window_open(self.ade3))
        
        
        self.__open_data_input_entry_window = tkinter.Button(self.__data_entry_frame, text="Open data entry window", command=lambda: self.__data_window_classes())
    


        # pack buttons and labels
        self.__assistance_label.pack()

        self.create_new_prg_skill.pack()
        self.create_new_prg_skill_example.pack()

        self.speaking_engine.pack()
        self.speaking_engine_example.pack()

        self.speech_recognition.pack()
        self.speech_recognition_example.pack()
        
        self.__open_data_input_entry_window.pack(side='bottom')
        
        self.ADAM_frame_text.pack(side='top')
        self.__button_frame.pack(side='left')
        self.__explanation_frame.pack(side='right')
        self.__data_entry_frame.pack(side='bottom')
        tkinter.mainloop()
        


        

        

                    

    # takes text data and puts it into the clipboard
    def __action_button(self, text_placeholder):
        
        pyperclip.copy(text_placeholder)    # stores the copy and pasted data into the clipboard
        self.__assistance_label_text.set("Action has been Preformed")


    # opens a new toplevel window to store new copy and paste data
    def __data_window_classes(self):

        try:
            __input_file = open('Project_ADAM\STORAGE\copy_paste_ADAM.dat', 'r+b')
            self.__copy_paste_storage = pickle.load(__input_file)
            __input_file.close()
        except(IOError, AttributeError, EOFError):
            self.__copy_paste_storage = {}
        
            


        #  initialize the first dictionary and open it
        self.__data_class_window = tkinter.Toplevel() # creates another window for ADAM
        self.__data_frame = tkinter.Frame(self.__data_class_window)
        self.__data_class_window.title("DATA INPUT")

        self.__data_label = tkinter.Label(self.__data_frame, text='Enter data to be copied and pasted, Be careful as the data is stored in a DAT file, making data unreadible in file form')


        self.__data_key_entry = tkinter.Entry(self.__data_frame)
        self.__data_entry_box = tkinter.Text(self.__data_frame, width=80, height=25)
        self.__convert_data_button = tkinter.Button(self.__data_frame, text="convert text to dictionary and append to dat file", command= lambda: self.__append_data_to_file())

                
            
                
        # pack data window
        self.__data_label.pack()
        self.__data_key_entry.pack()
        self.__data_entry_box.pack()
        self.__convert_data_button.pack()
                
        self.__data_frame.pack()
    


    def __explanation_window_open(self, data):
        
        # fix adam explanation screen and cross platform OS data storing 
        self.__explanation_window = tkinter.Toplevel() # creates another window for ADAM
        self.__expo_frame = tkinter.Frame(self.__explanation_window)
        self.__explanation_window.title("ADAM Explanation Window")
        self.__expo_label = tkinter.Label(self.__expo_frame, text='Heres A Basic Explanation:')     # simple placeholder text that fits with all explanations



       
        self.__explanation_box = tkinter.Text(self.__expo_frame, width=80, height=35)
        
        
        self.__explanation_box.pack()
        self.__expo_label.pack()
        self.__explanation_box.insert('end', data)
        self.__explanation_box.config(state='disabled')
        
        self.__expo_frame.pack()
        

        # data is the explanation message sent into the function as text


    
        



        