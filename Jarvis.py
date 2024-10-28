import datetime
import time
import webbrowser
import sys
import os
import threading
import speech_recognition as sr
from difflib import SequenceMatcher
import pyttsx3
from functions import coder, settings, progress
import ctypes


class Jarvis:
    
    def __init__(self, mode="Microphone", speaker=True):
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
        self.engine = pyttsx3.init()
        self.power = None
        self.mode = mode
        self.speaker = speaker
        self.user_name = "Abhay"
        self.commands = {
            "hi, hello, sus": self.greet,
            "what's the time, time right now": self.tell_time,
            "how are you": self.how_are_you,
            "news": self.get_news,
            "empty recycle bin": self.empty_recycle_bin,
            "restore recycle bin": self.restore_recycle_bin,
            "where is": self.where_is,
            "open camera, click photo": self.open_camera,
            "open":"",
            "sleep, lock window": self.lock_window,
            "shutdown": self.shutdown,
            "restart": self.restart,
            "hibernate": self.hibernate,
            "log sign off": self.log_out,
            "cancel": self.cancel,
            "exit, close": self.exit
        }

    def listen(self):
        
        if self.mode == "Input":
            return input("Enter command: ").lower()
        
        with self.microphone as source:
            self.recognizer.adjust_for_ambient_noise(source)
            print("Listening...")
            audio = self.recognizer.listen(source)
        try:
            query = self.recognizer.recognize_google(audio)
            print(f"User said: {query}")
            return query.lower()
        
        except sr.UnknownValueError:
            self.speak("Sorry, I did not understand that.")
            return ""
        except sr.RequestError:
            self.speak("Sorry, my speech service is down.")
            return ""
        
    def speak(self, text):
        print(text)
        
        if self.speaker:
            self.engine.say(text)
            self.engine.runAndWait()

    def process_query(self, query):
        """
        Process user query and return response
        """
        # Process the query and return response
        try:
            # Your query processing logic here
            response = self.generate_response(query)
            return response
        except Exception as e:
            return f"Sorry, I encountered an error: {str(e)}"
    
    def generate_response(self, query):
        # Your existing response generation logic
        for cmd, action in self.commands.items():
            if self.similar(query, cmd.split(',')) > 0.5:
                return action()
        return "Sorry, I didn't understand what you meant."
    
    def similar(self, query, commands):
        
        matchRatioLis = []
        for command in commands:
            matchRatioLis.append(SequenceMatcher(None, query, command).ratio())

            
        return max(matchRatioLis)
    
    def greet(self):
        message = f"Hi {self.user_name} how may I assist you today?"
        self.speak(message)
        return message

    def tell_time(self):
        now = datetime.datetime.now().strftime("%H:%M:%S")
        message = f"The current time is {now}"
        self.speak(message)
        return message

    def how_are_you(self):
        message = "I am fine, thank you. How can I assist you today?"
        self.speak(message)
        return message

    def get_news(self):
        message = "Fetching the latest news for you."
        self.speak(message)
        webbrowser.open("https://news.google.com/")
        return message

    def empty_recycle_bin(self):
        message = "Emptying the recycle bin."
        self.speak(message)
        settings.recycled("empty")
        return message

    def restore_recycle_bin(self):
        message = "Restoring the recycle bin."
        self.speak(message)
        settings.recycled("restore")
        return message

    def where_is(self):
        message = "Please specify the location."
        self.speak(message)
        location = self.listen()
        webbrowser.open(f"https://www.google.com/maps/place/{location}")
        return f"Opening maps for location: {location}"

    def open_camera(self):
        message = "Opening camera."
        self.speak(message)
        settings.camera()
        return message

    def lock_window(self):
        message = "Locking the window."
        self.speak(message)
        self.power = threading.Thread(target=settings.power,args=['lock'], daemon=True)
        self.power.start()
        return message

    def shutdown(self):
        message = "Shutting down the system in 20 seconds.\nPlease close any opened applications."
        self.speak(message)
        self.power = threading.Thread(target=settings.power,args=['shutdown'], daemon=True)
        self.power.start()
        return message

    def restart(self):
        message = "Restarting the system in 20 seconds.\nPlease close any opened applications."
        self.speak(message)
        self.power = threading.Thread(target=settings.power,args=['restart'], daemon=True)
        self.power.start()
        return message

    def hibernate(self):
        message = "Hibernating the system in 20 seconds."
        self.speak(message)
        self.power = threading.Thread(target=settings.power,args=['hibernate'], daemon=True)
        self.power.start()
        return message

    def log_out(self):
        message = "Signing off the system in 10 seconds.\nPlease close any opened applications."
        self.speak(message)
        self.power = threading.Thread(target=settings.power,args=['log out'], daemon=True)
        self.power.start()
        return message

    def cancel(self):
        if self.power is not None and self.power.is_alive():
            self.stopThread(self.power)
            return "Cancelled the pending operation."
        return "No operation to cancel."

    def exit(self):
        message = "Exiting program..."
        self.speak(message)
        time.sleep(1)
        sys.exit(0)
        return message

    def getThreadId(self, thread):

        if hasattr(thread,'_thread_id'):
            return thread._thread_id
        for id,thread1 in threading._active.items():
            if thread1 is thread:
                return id

    def stopThread(self, thread):
        threadId = self.getThreadId(thread)
        res = ctypes.pythonapi.PyThreadState_SetAsyncExc(threadId,\
            ctypes.py_object(SystemExit))

        if res > 1:
            ctypes.pythonapi.PyThreadState_SetAsyncExc(threadId,0)


def main():
    jarvis = Jarvis(mode="Input", speaker=None)
    try:
        while True:
            query = jarvis.listen()
            if query:
                jarvis.process_query(query)
    except KeyboardInterrupt:
        print("Exiting program...")
        sys.exit(0)


if __name__ == "__main__":
    main()
