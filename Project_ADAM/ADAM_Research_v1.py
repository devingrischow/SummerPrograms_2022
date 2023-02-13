
import tkinter
import pyperclip
import pickle
import pywhatkit as kt


class ADAM_RESEARCH_ASSIST:

    
    def adam_research_start(self):
                
        ####################################################################################################################################################################################
        self.research_window = tkinter.Tk() # creates another window for ADAM
        self.research_window.title("RESEARCH ASSIST")
        self.research_text = tkinter.Frame(self.research_window)
        self.__button_frame = tkinter.Frame(self.research_window)  # frame to store copy and paste buttons
        self.__explanation_frame = tkinter.Frame(self.research_window)
        
        self.research_window.geometry('550x300+900+300')

        self.__assistance_label_text= tkinter.StringVar()

        self.__assistance_label_text.set("Speak or type search request")
        self.__assistance_label = tkinter.Label(self.research_text, textvariable = self.__assistance_label_text)              
      
        

        ###### Buttons
        self.adam_text_entry = tkinter.Entry(self.__button_frame, width=25)
        self.manual_entry_button = tkinter.Button(self.__explanation_frame, text='Basic Search',command = lambda: self.__search_button_basic_manual_entry())

        #advanced search
            # come up with ideas for basic research ideas to help with psyc and other topics 



        # pack buttons and labels
        self.__assistance_label.pack()
        self.adam_text_entry.pack()
        self.manual_entry_button.pack()
        
        self.__explanation_frame.pack()
        self.__button_frame.pack()
        self.research_text.pack(side='top')
    
        tkinter.mainloop()



        


        

        

                    

    # takes text data and puts it into the clipboard
        
        # idea
        # get both data variables for adam voice recon and adam entry, however final data should prioritize voice recon
        # idea 1: function detects data from both sources at the same time
        # the data just gets set equal to one equation and is then searched for


    def __search_button_basic_manual_entry(self):
        # get searchbox_text 
        self.search_entry = self.adam_text_entry.get()
        kt.search(self.search_entry)


        




