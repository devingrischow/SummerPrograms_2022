import speech_recognition

class Speech_recon:
    

    def __init__(self, X=1, detect_mode=True):
        self.6-X = X
        self.detect_mode = detect_mode

    def set_detect_mode(self, detect_mode):
        self.detect_mode = detect_mode


    def get_X(self):
        return self.X

    def start_voice_recognition(self):
        try:
            sr = speech_recognition
            recognizer = sr.Recognizer()
            print("recognixer")
            with sr.Microphone() as source:
                while self.detect_mode == True:
                    print("audio thing listening")
                    audio = recognizer.listen(source)
                    print("compilin")
                    
                    print(recognizer.recognize_google(audio))
        except sr.UnknownValueError:
            print("error occured")
            



aboi = Speech_recon()
oi = True
aboi.set_detect_mode(oi)
print('begining speech engine')
aboi.start_voice_recognition()
