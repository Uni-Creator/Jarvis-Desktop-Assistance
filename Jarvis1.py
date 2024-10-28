import ctypes
import re
import time

startTime = time.perf_counter()

# build-in modules
import subprocess
import os
import sys
import random
import json
# import winshell
import datetime
import shutil
from threading import Thread
import threading
# import win32com.client as wincl

# installed modules
import pyttsx3
import speech_recognition as sr
import wikipedia
import wolframalpha
import webbrowser
import pyjokes
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import requests
import urllib
from urllib.request import urlopen
# import ctypes
# from bs4 import BeautifulSoup
from pynput.keyboard import Key, Controller
# from twilio.rest import Client
# import cv2
# import pywhatkit
## from geopy.geocoders import Nominatim
## import playsound
## import gtts
# import feedparser
# import operator


# my python files
from functions import coder, check_holiday, settings, progress
# import functions.progress
#from functions.rec_face import *
# from functions import check_holiday
# from functions import settings 
# from gui import *
# import functions.weather
from functions.match import match


print(time.perf_counter()-startTime)

# flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint)

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# engine.setProperty('voice',voices[0].id) # Default voice




def getThreadId(thread):

    if hasattr(thread,'_thread_id'):
        return thread._thread_id
    for id,thread1 in threading._active.items():
        if thread1 is thread:
            return id

def stopThread(thread):
    threadId = getThreadId(thread)
    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(threadId,\
        ctypes.py_object(SystemExit))

    if res > 1:
        ctypes.pythonapi.PyThreadState_SetAsyncExc(threadId,0)

class Jarvis():
    
    def __init__(self):
        super(Jarvis,self).__init__()

    def printf(self,text):
        print(text)
        return text

    def speak(self,audio):
        genList = ["Male","Female"]
        voice = genList.index(self.getAssData('Gender'))
        engine.setProperty('voice',voices[voice].id)
        engine.say(audio)
        engine.runAndWait()

    def pdf_read(self,file):
        # creating a pdf file object 
        with open(file, 'rb') as pdfFileObj:
            # creating a pdf reader object 
            pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 
            # printing number of pages in pdf file 
            pgnm = pdfReader.numPages
            text = ''
            for i in range(0,pgnm):
                # creating a page object 
                pageObj = pdfReader.getPage(i)
                # extracting text from page
                s = pageObj.extractText()
                text += s
            return text

    def checkUser(self,file='LoginData.uiop'):
        try:
            return coder.decoder(f'data/loginInfo/{file}').split('\n')
        except:
            return False
        
    def addGmail(self):
        if self.checkUser():
            data = self.checkUser()
            response = self.printf('A user already exists do you want to delete it')
            while True:
                yn1 = input('Delete existing user or not (y/n): ').lower()
                if yn1 == 'n':
                    return response
                elif yn1 == 'y':
                    break
                else:
                    os.system('cls')
        try:
            user = input('Enter your username: ')
            response = self.printf('Sir! To continue further I would like to know your some personal information')
            while True:
                yn2 = input('Would you like to continue or not (y/n): ').lower()
                if yn2 == 'n':
                        return False
                elif yn2 == 'y':
                    break
                else:
                    os.system('cls')
            
            while True:
                email = input('Sir please enter your gmail address: ')
                if '@gmail.com' in email:
                    break
                else:
                    os.system('cls')
            
            passw = input('Sir please enter your gmail address\'s password: ')
            
            userInfo = user + '\n' + email + '\n' + passw
            encodedInfo = coder.encoder(userInfo)
            with open('./data/loginInfo/LoginData.uiop','w') as file:
                file.write(encodedInfo)
                return True
            
        except:
            with open('./data/loginInfo/LoginData.uiop') as f:
                cont = f.read()
            if cont == '':
                with open('./data/loginInfo/LoginData.uiop','w') as f2:
                    f2.write(data)
            os.system('cls')
            return False

    def addUser(self):
        if self.checkUser:
            data = self.checkUser('LoginCredentials.uiop')
            response = self.printf('A user already exists do you want to delete it')
            while True:
                yn1 = input('Delete existing user or not (y/n): ').lower()
                if yn1 == 'n':
                    return False
                elif yn1 == 'y':
                    break
                else:
                    os.system('cls')
        try:
            user = input('Enter your username: ')
            passw = input('Enter your password: ')
            userInfo = user + '\n' + passw
            encodedInfo = coder.encoder(userInfo)
            with open('./data/loginInfo/LoginCredentials.uiop','w') as file:
                file.write(encodedInfo)
            self.getAssData({'Current user':f"{user}"},True)
            return True
            
        except:
            with open('./data/loginInfo/LoginCredentials.uiop') as f:
                cont = f.read()
            if cont == '':
                with open('./data/loginInfo/LoginCredentials.uiop','w') as f2:
                    f2.write(data)
            os.system('cls')
            return False

    def wishMe(self):
        # userId = checkUser('LoginCredentials.uiop')[0].replace('username: ','')
        hour = int(datetime.datetime.now().hour)
        # print(hour)
        if hour>= 0 and hour<12:
            response = self.printf("Good Morning Sir!")

        elif hour>= 12 and hour<18:
            response = self.printf("Good Afternoon Sir!")   

        else:
            response = self.printf("Good Evening Sir!")  
            
        if check_holiday.checker():
            response +=  '\n' + self.printf(check_holiday.checker())
        response += '\n' + self.printf('How may I help you today?')
        return response

    def usrname(self):
        uname = self.takeCommand()
        columns = shutil.get_terminal_size().columns

        response = self.printf("#####################".center(columns))
        response += self.printf("Welcome Mr.", uname.center(columns)) +'\n'
        response += self.printf("#####################".center(columns)) + '\n'

    def takeCommand(self):
    
        try:
            r = sr.Recognizer()
        
            with sr.Microphone() as source:
  

                r.adjust_for_ambient_noise(source,duration=3)
                r.pause_threshold=2
                r.energy_threshold=250
                r.dynamic_energy_threshold=250
                audio = r.listen(source)

            self.printf("Recognizing...")

            query = r.recognize_google(audio, language ='en-in')
            self.printf(query)

            if query == 'trial version':
                print('API not founded!')
                raise
            

    
        except KeyboardInterrupt:
            query = None

        except Exception as e:
            # time.sleep(10)
            print(e)
            query = None
            # response = self.printf(e)
            # query = input('Command: ')
        # query = input('Command: ')
        return query
    
    def sendEmail(self,to, content,subject=None,attachment=None):
        while True:
            user = self.checkUser()
            if user:
                userEmail = user[1]
                userPass = user[2]
                break
            else:
                self.addGmail()

        message = MIMEMultipart()
        message['From'] = userEmail
        message['To'] = to
        
        if subject != None:
            message['Subject'] = subject
        
        message.attach(MIMEText(content,'plain'))
        
        if attachment != None:
            for file in attachment:
                if file.endswith('.pdf'):
                    fileCont = self.pdf_read(file)
                else:
                    with open(file) as file:
                        fileCont = file.read()
                payload = MIMEBase('application','octate-stream')
                payload.set_payload((fileCont))
                encoders.encode_base64(payload)
                payload.add_header('Content-Decomposition',f'attachment;filename=Jarvis.py')
                message.attach(payload)
        
        text = message.as_string()
        
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.ehlo()

        # Enable low security in gmail
        # server.connect('smtp.gmail.com',587)
        server.login(userEmail, userPass)
        server.sendmail(userEmail, to, text)
        server.close()
        server.quit()

    def MatchFace(self):
        try:
            recTurn = 0
            decTurn = 0
            response = self.printf('[#] Detecting Face')
            while True:
                os.system('cls')
                detect = detectFace()
                if not detect:
                    decTurn += 1
                    # if decTurn == 5:
                    #         response = self.printf('Sir! I am enable to recognize your face try to login with your UserId and password ?')
                    #         log = Login()
                    #         return True
                    # os.system('cls')
                else:
                    response = self.printf('[#] Recognizing')
                    face = Recognize()
                    if not face:
                        recTurn += 1
                        if recTurn == 5:
                            response = self.printf('Sir! I am enable to recognize your face try to login with your id password ?')
                            self.Login()
                            return True
                        response = self.printf('[#] Failed!\n[#] Retrying!')
                        os.system('cls')
                    else:
                        self.wishMe()
                        return True
        except:
            pass

    def Login(self):
        try:
            clear = lambda: os.system('cls')
            clear()
        #    response = self.printf(checkUser('LoginCredentials.uiop'))
            if not self.checkUser('LoginCredentials.uiop'):
                self.addUser()
            userId = self.checkUser('LoginCredentials.uiop')[0].replace('username: ','')
            userPass = self.checkUser('LoginCredentials.uiop')[1].replace('password: ','')
            # response = self.printf(userId)
            # response = self.printf(userPass)
            turns = 0
            while True:
                Id = input('Enter your username: ')
                Pass = input('Enter your password: ')

                if Id == userId and Pass == userPass:
                    clear()
                    self.wishMe()
                    return True
                else:
                    turns += 1
                    response = self.printf('[#] Invalid Credentials!')
                    if turns == 5:
                        response = self.printf('Too many wrong attempts please try again after sometime.')
                        time.sleep(30)
                    elif turns == 6:
                        response = self.printf('Too many wrong attempts please try again after sometime.')
                        time.sleep(30)
                    elif turns == 7:
                        response = self.printf('Too many wrong attempts please try again after sometime.')
                        time.sleep(30)
                    elif turns == 8:
                        response = self.printf('Too many wrong attempts. Exiting')
                        # exit(app.exec_())
                        exit()
                clear()
        except KeyboardInterrupt:
            self.Login()
              
    def search_web(self,input): 
        try:
            if 'youtube' in input.lower(): 
                response = self.printf("Opening in youtube") 
                indx = input.lower().split().index('youtube') 
                query = input.split()[indx + 1:] 
                webbrowser.open("http://www.youtube.com/results?search_query=" + '+'.join(query)) 

            elif 'wikipedia' in input.lower(): 
                response = self.printf("Opening Wikipedia") 
                indx = input.lower().split().index('wikipedia') 
                query = input.split()[indx + 1:] 
                webbrowser.open("https://en.wikipedia.org/wiki/" + '_'.join(query)) 

            elif 'google' in input:
                    indx = input.lower().split().index('google') 
                    query = input.split()[indx + 1:] 
                    response = self.printf(f'Openning google')
                    webbrowser.open("https://www.google.com/")
            else: 
                response = self.printf(f'Searching {input}')
                # speak(f"Searching {input}")
                webbrowser.open("https://www.google.com/search?q=" + '+'.join(input.split())) 
            return response
        except:
            return False

    def open_application(self,input): 
        # function used to open application 
        # present inside the system. 

        apps = {}
        with open('functions/executables.txt') as f:
            for i in f.read().split('\n'):
                apps[i.split(' : ')[0].lower()] = i.split(' : ')[-1]
        
        input2 = input.lower().replace('microsoft','').replace('office','')
        # remList = []
        input2 = input2.split()
        indx = input2.index('open')

        appNameList = input2[indx + 1:]
        for space in range(appNameList.count(' ')):
            appNameList.remove(' ')
        # for i in appNameList:
        #     if i == '':
        #         remList.append(i)
        # print(appNameList)
        # for r in remList:
        #     appNameList.remove(r)

        # print(appNameList)

        if 'command' in appNameList or 'cmd' in appNameList:
            response = self.printf('Opening CMD')
            os.system('start cmd.exe')
            return response

        elif 'whatsapp' in appNameList:
            response = self.printf('Opening WhatsApp')
            try:
                os.startfile('%USERPROFILE%/Desktop/WhatsApp Desktop.lnk')
            except:
                response = self.printf(('You don\'t have WhatsApp installed. Opening WhatsApp WEB.'))
                webbrowser.open('https://web.whatsapp.com/')
            return response

        elif 'jarvis' in appNameList or 'alexa' in appNameList:
            response = self.printf(('I am already running Sir...'))
        else:
            name = list(apps.keys())
            # print(name)

            for i in appNameList:
                # print(i)
                for j in name:
                    # print(j)
                    app = j.split('.')[0]
                    if i in app.split(' '):
                        x = j.replace(".lnk","").replace('.exe','')
                        response = self.printf(f'Opening {x}')
                        os.startfile(apps[j])
                        return response

        # response = self.printf("Application not available")
        # speak("Application not available") 
        return self.search_web(input)

    def getAssData(self,data,write=False):
        filePath = "./data/files/myinfo/myinfo.uiop"
        if not write:
            assert type(data) == str
            rawAssData = coder.decoder(filePath)
            dataList = rawAssData.split('\n')
            # Comman format of file
            # Comman name: abc
            # Current user: abcd
            # Gender: Male
            # Name: Jarvis 2.0
            # Version: 2.0
            # Website: Null
            # Path: Null
            # Created By: Uni-Creator
            # GitHub: https://github.com/Uni-Creator/
            # @ Copyright 2021
            for info in dataList:
                if data in info:
                    return info.split(': ')[-1]
            return False
        else:
            assert type(data) == dict
            try:
                newData = []
                rawAssData = coder.decoder(filePath).split('\n')
                # response = self.printf(rawAssData)

                for a,b in enumerate(rawAssData):
                    newData.insert(a,b)
                    # response = self.printf(a,b)

                for key in data:
                    if key == 'Comman name':
                        newData.pop(1)
                        newData.insert(1,'Comman name: '+data[key])
                    if key == 'Gender':
                        newData.pop(0)
                        newData.insert(0,'Gender: '+data[key])
                    if key == 'User name':
                        newData.pop(2)
                        newData.insert(2,'User name: '+data[key])

                # response = self.printf(newData)
                finalData = '\n'.join(newData)
                # response = self.printf(finalData)
                encodedData = coder.encoder(finalData)
                with open(filePath,'w') as f:
                    f.write(encodedData)
                return True
            except FileNotFoundError:
                return False

    def checkCommand(self,input=None,response=False):
        global assname
        global power
        clear = lambda: os.system('cls')
        # This Function will clean any
        # command before execution of this python file
        # clear()
        assname = self.getAssData('Comman name')
        # wishMe = self.wishMe()
        # takeCommand = self.takeCommand()
        # getAssData = self.getAssData()

     # while True:
        query = self.takeCommand().lower() if input is None else input.lower()
        #  All the commands said by user will be 
        #  stored here in 'query' and will be
        #  converted to lower case for easily 
        #  recognition of command
        # power = Thread(target=settings.power)

        if match(["hi","hello"], query) and query[0] == "h":

            response = "Hi. How are you?"
            print(response)
            return [response,'Normal']

        elif match(['how are you'],query):

            response = "I am fine. Thanks for asking"
            print(response)
            return [response,'Normal']
        
        elif match(['good morning', 'good night','good evening'],query):
            greeting = query.split(' ')[query.split(' ').index('good') + 1]
            response = f"A warm,{greeting}\nHow are you Sir?"
            print(response)
            return [response,'Normal']
            # user = self.getAssData("Current User")

        elif re.search('speak',query):
            query = query.split(' ')[1:]
            response = ' '.join(query)
            print(response)
            return [response,'Normal']

        elif match(['fine', "good"] , query):
            response = "I am glad to know that your fine"
            print(response)
            return [response,"Normal"]

        elif match(["change user name to","update user name to"],query):
            query = query.replace("change user name to", "").replace('update user name to', "")
            
            if 'something' in query:
                response = 'Sir I think that something is not a good name. Please think of any other name.'
                succeeded = "Error"
            else:
                userName = query.title()
                self.getAssData({"User name":userName},True)
                response = f"User name successfully updated to {userName}"
                succeeded = "Success" 

            print(response)
            return [response,succeeded]

        elif "change name to " in query:


            query = query[query.index(" to ")+4:]

            if 'something' in query:
                response = 'Sir I think that something is not a good name. Please think of any other name.'
                succeeded = "Error"
            else:
                assname = query
                self.getAssData({"Comman name":assname},True)
                response = "Thanks for naming me"
                succeeded = "Success"
            print(response)
            return [response,succeeded]

        elif "change voice" in query:
            try:
                genList = ["Male","Female"]
                cVoice = genList.index(self.getAssData('Gender'))
                if cVoice == 0: voice,name = 1,"Alexa"
                else: voice,name = 0,"Jarvis"
                gender = genList[voice]
                self.getAssData({"Gender":gender,"Comman name":name},True)
                response = 'How do you like my new voice ?'
                succeeded = "Success"
            except:
                response = 'Sir, I am unable to change my voice'
                succeeded = "Error"

            print(response)
            return [response,succeeded]

        elif "update assistant" in query:
            response = "Downloading file please wait..."
            # main.jarvisTask(response,False)
            try:
                url = '# url after uploading file'
                r = requests.get(url, stream = True)
                
                with open("Updated_Jarvis.py", "wb") as file:
                    saved = False
                    total_length = int(r.headers.get('content-length'))
                    for ch in progress.bar(r.iter_content(chunk_size = 2391975),label='Downloading ',expected_size =(total_length / 1024) + 1):
                       if ch:
                           file.write(ch)
                           saved = True
                    if saved: subprocess.call('del Jarvis.py && ren Updated_Jarvis.py Jarvis.py && python Jarvis.py', shell=True)
                    else: raise
            except Exception as e:
                response = 'Unable to download file please try again'
                print(response)
                return [response,"Error"]

        elif "what's your name" in query or "what is your name" in query:
            response = f"My friends call me {assname}. Although I don't have any friends"
            print(response)
            return [response,"Normal"]

        elif match(['what do you want',"what do you desire",'what do you wish for'],query):
            if 'wish' in query:
                say = 'wish'
            elif 'desire' in query:
                say = 'desire'
            elif 'want' in query:
                say = 'want'
            response = f"I only {say} to serve you."
            print(response)
            return [response,"Normal"]

        elif "i am your friend" in query or "i want to be your friend" in query or "i want to become your friend" in query:
            response = f"Thanks a lot. I am glad to hear that"
            print(response)
            return [response,"Normal"]

        elif "who made you" in query or "who created you" in query:
            creator = self.getAssData("Created By")
            response = f"I have been created by {creator}."
            print(response)
            return [response,"Normal"]

        elif 'what year this is' in query:
            year = time.strftime('%Y')
            if year[1] =='1':
                abb = "'st"
            elif year[1] == '2':
                abb = "'nd"
            elif year[1] == '3':
                abb = "'rd"
            else: 
                abb = "'th"
            response = f"This {year[0]}{year[1]}{abb} century and the year is {year}"
            print(response)
            return [response,"Normal"]

        elif match(['time'],query):
            strTime = datetime.datetime.now().strftime("%H:%M:%S") 
            response = f"Sir, the time is {strTime}"
            print(response)
            return [response,"Normal"]

        elif match(['date'],query):
            date = datetime.datetime.now().strftime("%x")
            response = f"Sir, today\'s date is {date}"
            print(response)
            return [response,"Normal"]

        elif 'is love' in query:
            response = "Love is the 7th sense, that destroys all other senses"
            print(response)
            return [response,"Normal"]

        elif "who are you" in query or 'what are you' in query:
            creator = self.getAssData("Created By")
            response = f'I am an Artificial Intelligence, AI in short.\nCreated by {creator}'
            print(response)
            return [response,"Normal"]

        elif 'reason for you' in query:
            creator = self.getAssData("Created By")
            response = f"Thanks to {creator}. Further it's a secret"
            print(response)
            return [response,"Normal"]

        elif "why you came to world" in query:
            creator = self.getAssData("Created By")
            response = f"Thanks to {creator}. Further it's a secret"
            print(response)
            return [response,"Normal"]
        
        elif "how are you" in query:
            response = 'I am fine. Thanks for asking'
            print(response)
            return [response,"Normal"]
 
        elif 'open' in query:
            try:
                if 'type' in query:
                    keyboard = Controller()
                    searchList = query.split('and') 
                    app = searchList[0]
                else:
                    if query.replace('open',''):
                     app = query
                    else:
                     raise Exception
                print(app)
                AppOpened  = self.open_application(app)
                if not(AppOpened):
                    AppOpened = self.search_web(query)
                    if not(AppOpened):
                        raise Exception
                
                # main.jarvisTask(AppOpened,run=False,action="Success")
                time.sleep(1)

                if 'type' in query:
                    if 'chrome' in query or 'edge' in query or 'cmd' in query:
                        tasklist = ''
                        app = app.replace('open','').replace(' ','')
                        while not (app in tasklist):
                            tasklist = subprocess.run('tasklist',shell=True,text=True,capture_output=True).stdout
                        time.sleep(1)
                    else:
                        time.sleep(6)
                    keyboard.type(searchList[-1].replace('type ','').replace('search ',''))
                    keyboard.press(Key.enter)
                    keyboard.release(Key.enter)

                return [AppOpened,'']
                
            except Exception as e:
                response = f'Sorry Sir I am unable to open what you want'
                print(response)
                return [response,"Error"]

        elif 'close' in query:

            if 'jarvis' in query or 'alexa' in query:
                # main.jarvisTask('Thanks for giving me your time',False)
                time.sleep(2)
                # main.close()

            lis = query.split(' ')
            if len(lis) == 1: appToBeClosed = ''
            else:
                index = lis.index('close')
                appToBeClosed = query.split(' ')[index + 1]

            ExeNameDict = {}

            with open('functions/executables.txt') as f:
                for i in f.read().split('\n'):
                    # if not(i.endswith('.lnk')):
                    appAndPath = i.split(' : ')
                    ExeNameDict[appAndPath[0]] = appAndPath[-1]

            for app,path in ExeNameDict.items():

                if appToBeClosed.lower() in app.lower() + path.lower():
                    appExe = path.split('\\')[-1].split('.')[0].lower()

                    closedOrNot = subprocess.call(f'taskkill /f /im {appExe}.exe')
                    # print(closedOrNot)

                    if closedOrNot != 0: response,succeeded = f"Cannot close {appToBeClosed}","Error"
                    else: response,succeeded = f"{appToBeClosed} is closed successfully","Success"

                    break

            if not(response): response,succeeded = f"Cannot close {appToBeClosed}","Error"
            print(response)
            return [response,succeeded]  

        elif 'who am i to you' in query or 'what is our relationships' in query or 'who you are to me' in query:
            response = 'You are my one and only Sir and I am your assistant.\nI belong only to you.'
            print(response)
            return [response,"Normal"]
        
        elif "who i am" in query or "who am i" in query:
            response = "If you talk then definately you are human."
            print(response)
            return [response,"Normal"]

        elif 'what' in query or 'who' in query or 'why' in query or 'search' in query or 'how' in query:
            response = 'Searching...'
            succeeded = "Success"
            # main.jarvisTask(response,False)
            print(response)
            try:
                response = wikipedia.summary(query, sentences = 3)
            except:
                try:
                    # Use the same API key 
                    # that we have generated earlier
                    client = wolframalpha.Client("ELQLE3-6Q5QVQ8E7U")
                    res = client.query(query)
                    response = next(res.results).text
                except:
                    response = "No results found"
                    succeeded = "Error"
            print(response)
            return [response,succeeded]

        elif 'play music' in query or "play song" in query:
            try:
                raise
                # pywhatkit.playonyt('query')
            except:
                # music_dir = "D:\\Song"
                music_dir = "E:/"
                song_list = []

                # finding songs in e drive
                for root, dirs, files in os.walk(music_dir):
                    for i in files:
                        if i.endswith('.mp3')and os.path.getsize(i) > 2048:
                            p=root+'/'+i
                            song_list.append(p)

                # response = self.printf(song_list)
                randomSong = random.choice(song_list)
                # response = self.printf(randomSong)
                os.startfile(randomSong)
                # random = os.startfile(os.path.join(music_dir, songs[1]))

        elif 'send a mail' in query or 'send mail' in query or 'send email' in query:
            try:

                to = input('To whom: ')
                if not('@gmail.com' in to):
                    response = 'Invalid email address'
                    print(response)
                    return [response,"Error"]

                succeeded = "Success"

                try:
                    response = 'What should be the subject ? You can leave it blank for no subject.'
                    # main.jarvisTask(response,False)
                    print(response)

                    sub = input('Subject: ')
                    if sub.strip() == '':
                        sub = None
                except:
                    sub = None

                try:
                    response = 'Do you want any attachment ? You can leave it blank for no attachment. Or you can attach mutiple files by typing their paths separeted by ,'
                    # main.jarvisTask(response,False)
                    print(response)
                    attach = input('Attachment\'s path: ')
                    if attach.strip() == '':
                        attach = None
                    elif ',' in attach:
                        attach = attach.split(',')
                    else:
                        attach = [attach]

                except:
                    attach = None

                content = input('Content: ')
                self.sendEmail(to, content,subject=sub,attachment=attach)

            except Exception as e:

                response = "Sir I am not able to send this email"
                print(e)
                succeeded = "Error"

            print(response)
            return [response,succeeded]

        elif 'joke' in query:
            try:
                response = pyjokes.get_joke()
                succeeded = "Success"
            except:
                response = 'Sir! you are not connected to the internet. So I am unable to get some jokes'
                succeeded = "Error"
            print(response)
            return [response,succeeded]

        elif "calculate" in query:
            try:
                
                succeeded = "Success"
                # main.jarvisTask('Calculating..',False)
                print('Calculating..')
                app_id = "ELQLE3-6Q5QVQ8E7U"
                client = wolframalpha.Client(app_id)
                indx = query.split(' ').index('calculate') 
                query2 = query.split(' ')[indx + 1:] 
                res = client.query(' '.join(query2)) 
                answer = next(res.results).text

                response = "The answer is " + answer

            except:
                response = f'Sir! I am unable to {query}'
                succeeded = "Error"
            print(response)
            return [response,succeeded]

        elif 'power point presentation' in query or 'ppt' in query:
            response = f"opening Power Point presentation for {assname}"
            power = "./data/files/myinfo/Presentation/Jarvis.pptx"
            os.system(f'start {power}')
            print(response)
            return [response,"Normal"]
            # os.startfile(power)

        elif 'change background' in query:

            # main.jarvisTask('Do you want to specify a background image file path',False)
            yn = self.takeCommand().lower()
            if yn == 'yes': path = input('Enter the path: ')
            else: path = None
            settings.changeBackground(path)
            response = 'Background changed succesfully'
            print(response)
            return [response,"Normal"]

        # elif 'open bluestack' in query:
            # appli = r"C:\\ProgramData\\BlueStacks\\Client\\Bluestacks.exe"
            # os.startfile(appli)

        elif 'news' in query:
            try: 
                succeeded = "Success"
                # jsonObj = urlopen('''https://newsapi.org/v1/articles?source=bbc-news&sortBy=top&apiKey=4dbc17e007ab436fb66416009dfb59a8''')
                jsonObj = urlopen('''https://newsapi.org/v1/articles?source=the-times-of-india&sortBy=top&apiKey=4dbc17e007ab436fb66416009dfb59a8''')
                data = json.load(jsonObj)
                i = 1

                self.printf('''=============== TIMES OF INDIA ============'''+ '\n')
                response = ''
                for item in data['articles']:
                    news = str(i) + '. ' + item['title'] + '\n\n' + item['description'] + '\n\n'
                    response += news
                    i += 1

                date = datetime.datetime.now().strftime("%x %H:%M:%S")

                with open ('data/files/newsData.txt','a+') as f:
                    f.write(f"{date}\n{data['articles']}")
                
                
            except urllib.error.URLError as e:
                # print(e)
                response,succeeded = 'Sir! your are not connected to the internet',"Error"
            print(response)
            return [response,succeeded]

        elif 'empty recycle bin' in query:
            recycled = settings.recycled()
            if recycled:
                response = "Recycle Bin Recycled"
                succeeded = "Success"
            else:
                response = 'Unable to empty recycle bin'
                succeeded = "Error"
            print(response)
            return [response,succeeded]

        elif "where is" in query:
            query = query.replace("where is", "")
            location = query
            # main.jarvisTask("Locating " + location,False)
            print('Locating ' + location)
            webbrowser.open("https://www.google.nl/maps/place/" + location )

        elif "camera" in query or "take a photo" in query:
            cam = settings.camera()
            response = 'Press enter to click a photo'
            # main.jarvisTask(response,False)

            if not cam:
                response = 'Sir! I am unable to capture your photo please try again later'
                print(response)
                return [response,"Error"]
            else:
                return ["Photo saved successfully!", "Normal"]
            # stop()

        elif 'lock window' in query or 'lock device' in query:
                # main.jarvisTask(response,False)
                # response = ''
                power = Thread(target=settings.power,args=['lock'])
                power.start()
                print('Locking the device')
                return ["Locking the device","Normal"]

        elif 'shutdown system' in query:
                # main.jarvisTask(response,False)
                # response = ''
                power = Thread(target=settings.power,args=['shutdown'])
                power.start()
                response = "Shuting down system in 20 seconds. Close all apps"
                print(response)
                return [response,"Normal"]

        elif "restart" in query : #and( 'pc' in query or 'computer' in query or 'system' in query)
            # settings.power('restart')
            # main.jarvisTask(response,False)
            # response = ''
            power = Thread(target=settings.power,args=['restart'])
            power.start()
            response = 'Restarting in 20 seconds. Close all apps'
            print(response)
            return [response,"Normal"]

        elif "hibernate" in query:
            # main.jarvisTask(response,False)
            # response = ''
            power = Thread(target=settings.power,args=['hibernate'])
            power.start()
            response = "Hibernating"
            print(response)
            return [response,"Normal"]

        elif "log off" in query or "sign out" in query or 'log out' in query:
            # main.jarvisTask(response,False)
            # response = ''
            power = Thread(target=settings.power,args=['log out'])
            power.start()
            response = "Make sure all the application are closed before sign-out"
            print(response)
            return [response,"Normal"]

        elif 'cancel' in query:
            if power is not None and power.is_alive():
                stopThread(power)
                # power._set_tstate_lock(True)
                # power._stop()
                # power._delete()
                response = 'Process canceled successfully'
                print(response)
                return [response,"Normal"]

        elif "write a note" in query:
            response = "What should I write, Sir"
            # main.jarvisTask(response,False)
            print(response)
            note = self.takeCommand()
            with open('data/files/jarvis.txt', 'w') as file:
                strTime = time.strftime("%x %H:%M:%S")
                file.write(strTime + '\n' + note)

        elif "show note" in query:
            try:
                with open("data/files/jarvis.txt") as f:
                    response = f.read()
                    succeeded = "Success"
            except FileNotFoundError:
                response = "I am unable to open notes"
                succeeded = "Error"
            print(response)
            return [response,succeeded]

        # NPPR9-FWDCX-D2C8J-H872K-2YT43
        elif assname.lower() in query:
            version = self.getAssData('Name').split(' ')[-1]
            response = assname + ' ' + version + ' reporting Sir. How may I help you?'
            print(response)
            return [response,"Normal"]

        elif "weather" in query:
            try:
                send_url = 'http://ipinfo.io/json'
                r = requests.get(send_url)
                lotData = r.text
                lotData = json.loads(lotData)
                city = lotData['city']

                # Google Open weather website
                # to get API of Open weather 
                api_key = "5e23d5bf3f6d795eee4b02965e59c971"
                base_url = "http://api.openweathermap.org/data/2.5/weather?"
                complete_url = base_url + "appid=" + api_key + "&q=" + city
                response = requests.get(complete_url) 
                x = response.json() 
                print(x)

                if x["cod"] != "404": 
                    y = x["main"]
                    response = " Temperature (in kelvin unit) = " +str(y['temp'])+"\n atmospheric pressure (in hPa unit) ="+str(y['pressure']) +"\n humidity (in percentage) = " +str(y["humidity"]) +"\n description = " +str(x["weather"][0]["description"])
                else: 
                    response = f" Currently no data is avialable for {city}"
            except:
                response = 'Sir! you are not connected to internet'
            print(response)
            return [response,"Normal"]

        # elif "send message " in query:
                # # You need to create an account on Twilio to use this service
                # account_sid = 'Account Sid key'
                # auth_token = 'Auth token'
                # client = Client(account_sid, auth_token)

                # message = client.messages.create(
                # 					body = takeCommand(),
                # 					from_='Sender No',
                # 					to ='Receiver No'
                # 				)

                # response = self.printf(message.sid)

        elif "wikipedia" in query:
            response = wikipedia.summary(query.split('wikipedia')[-1], sentences = 3)
            print(response)
            return [response,"Normal"]

        elif 'brightness' in query:
            b = settings.brightness(query)
            response = f'Brightness {b} percent'
            print(response)
            return [response,"Normal"]
        
        elif 'record screen' in query or 'screen record' in query:
            T = None
            a = query.split(' ')
            if 'time' in query:
                T = int(a[a.index('time') - 1])
            if 'seconds' in query:
                T = int(a[a.index('seconds') - 1] )
                if 'minute' in query:
                    T += int(a[a.index('minute') - 1]) * 60
                    if 'hour' in query:
                        T += int(a[a.index('hour') - 1]) * 3600
            elif 'minute' in query:
                T = int(a[a.index('minute') - 1]) * 60
                if 'hour' in query:
                    T += int(a[a.index('hour') - 1]) * 3600
            elif 'hour' in query:
                T = int(a[a.index('hour') - 1]) *  3600
                
            msg = 'Starting recording. Press q to quit'
            # main.jarvisTask(msg,False)
            print(msg)
            r = settings.record_screen(T)
            if not r:
                response = 'Recording failed'
                succeeded = "Success"
            else:
                response = 'Recording succeeded'
                succeeded = "Error"
            print(response)
            return [response,succeeded]
        
        elif 'record mic' in query or 'record voice' in query:
            T = None
            a = query.split(' ')
            if 'seconds' in query:
                T = int(a[a.index('seconds') - 1] )
                if 'minute' in query:
                    T += int(a[a.index('minute') - 1]) * 60
                    if 'hour' in query:
                        T += int(a[a.index('hour') - 1]) * 3600
            elif 'minute' in query:
                T = int(a[a.index('minute') - 1]) * 60
                if 'hour' in query:
                    T += int(a[a.index('hour') - 1]) * 3600
            elif 'hour' in query:
                T = int(a[a.index('hour') - 1]) *  3600
            else:
                response = 'You must specify the duration to record'
                succeeded = 'Error'

            if T: 
                response = self.printf('Starting mic recording...')
                # main.jarvisTask(response,False)
                path = settings.mic(T)  
                response = 'Audio recorded\n'
                response += f'Recording saved to {path}'
                succeeded = 'Success'
            print(response)
            return [response,succeeded]
        
        elif 'volume' in query or 'mute' in query:
            response = settings.volume(query)
            return [response,""]

        elif 'screenshot' in query:
            if settings.takeScreenshot():
                response = 'Screenshot captured successfully'
                succeeded = "Success"
            else:
                response = 'Error capturing screenshot'
                succeeded = "Error"
            print(response)
            return [response,succeeded]

        elif 'reload' in query:
            assname = self.getAssData('Comman name')
            res = self.printf(f'Reloading {assname}')
            # main.jarvisTask(res,False)
            time.sleep(4)
            subprocess.call('taskkill /f /im python.exe > nul && python testChatUI.py',shell=True)

        # most asked question from google Assistant
        elif "will you be my gf" in query or "will you be my bf" in query or \
             'will you be my girlfriend' in query or "will you be my boyfriend" in query or \
                 "please go out with me" in query:
            # response = "I'm sorry, I only belong to my Sir"
            response = "I'm not sure about, may be you should give me some time"
            print(response)
            return [response,"Normal"]

        elif "i love you" in query:
            response = "It's hard to understand"
            print(response)
            return [response,"Normal"]

        elif 'will you marry me' in query:
            response = "I think it's to early for something like that, we should first get into relationship"
            print(response)
            return [response,"Normal"]
        
        elif 'i am your Sir' in query:
            response = 'I know that Sir.'
            print(response)
            return [response,"Normal"]

        # elif "" in query:
            # Command go here
            # For adding more commands
        
        else:
            response = "I didn't get that"
            print(response)
            return [response,"Error"]

    def run(self):
        # self.MatchFace()
        # self.Login()
        self.wishMe()
        # self.checkCommand()



# assname = startJarvis.getAssData('Comman name')
# gender = startJarvis.getAssData('Gender')
# userName = startJarvis.getAssData('User name')

if __name__ == '__main__':
    startJarvis = Jarvis()
    power = None
    keyboard = Controller()
    # app = QtWidgets.QApplication(sys.argv)
    # main = Main()
    # main.show()
    # exit(app.exec_())
    # MatchFace()
    # Login()
    # try:
    # jarvis = Jarvis()
    # print(assname)
    # jarvis.run()
    # except:
    #     pass
    # finally:
    #     print('\nBye')
