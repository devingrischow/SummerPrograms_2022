import speech_recognition

class Speech_recon:
    

    def __init__(self):
        self.audio_storage = None
        
    def get_audio_text(self):
        return self.audio_storage

    def start_voice_recognition(self):
        try:
            sr = speech_recognition
            recognizer = sr.Recognizer()
            with sr.Microphone() as source:
                
                print("Listening:")
                audio = recognizer.listen(source)
                
                
                self.audio_storage = recognizer.recognize_google(audio)

        except sr.UnknownValueError:
            print("error occured")
            self.audio_storage = 'error'
            


# sample for how to retrive data 
# aboi = Speech_recon()


# print('begining speech engine')
# aboi.start_voice_recognition()
# skrt = aboi.get_audio_text()
# print(skrt)
