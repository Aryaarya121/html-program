import speech_recognition as sr
import pyttsx3
def say(text):
   engine=pyttsx3.init()
   voice=engine.getProperty('voices')
   engine.setProperty('voice',voice[0].id)
   engine.say(text)
   engine.runAndWait()

def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source,duration=1)
        print("Listening........")
        r.pause_threshold=1
        audio = r.listen(source)
        try:
            print("Recognizing........")
            text = r.recognize_google(audio,language='en-in')
            print(f"User Said : {text}\n")
        except Exception as e :
            print(e)
            print("can not recognize your voice")
            return "None"
        return text    

    
while True:
   text=takecommand()
   say(text)    
