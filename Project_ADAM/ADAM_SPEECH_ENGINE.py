import pyttsx3



class ADAM_SPEECH_V1:
    def __init__(self, sentence=''):
        self.sentence = sentence

	
    def set_sentence(self, sentence):
        self.sentence = sentence


    def get_sentence(self):
        return self.sentence       


    def speaking_engine(self, sentence):
        self.sentence = sentence
        # init function to get an engine instance for the speech synthesis
        engine = pyttsx3.init()
        
        # say method on the engine that passing input text to be spoken
        engine.say(sentence)
        
        # run and wait method, it processes the voice commands.
        engine.runAndWait()

