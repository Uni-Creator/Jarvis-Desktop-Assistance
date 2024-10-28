#pip install notify2
#import notify2
#
#n = notify2.Notification("Summary",
#                         "Some body text",
#                         "SmallLogoCanary.png"   # Icon name
#                        )
#n.show()
#import pyautogui as pyg
#import time as t
#import sys
#import pyttsx3
#from PySide2.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QVBoxLayout, QLabel, QLineEdit, QDialog
#import os
#from PySide2.QtGui import QIcon
#import coder
#import Jarvis
#
#app = QApplication(sys.argv)
#
#class CallPy():
#    def call(self,path="E:\Abhay\Study\Programs\Python\Project\Clocks\clock.py"):
#        os.system(f'python {path}')
#
#class Window(QWidget):
#    def __init__(self):
#        super().__init__()
#
#        self.setWindowTitle("Jarvis")
#        self.setGeometry(800,500,300,220)
#
#        self.setIcon()
#        
#        self.create_button()
#
#        self.show()
#
#    def setIcon(self):
#        appIcon = QIcon("data/files/ico/icon.png")
#        self.setWindowIcon(appIcon)
#
#
#    def create_button(self):
#        vbox = QVBoxLayout()
#
#        btn1 = QPushButton("Open About Jarvis")
#        btn1.clicked.connect(self.show_about)
#
#        btn2 = QPushButton("Open Warning Jarvis")
#        btn2.clicked.connect(self.show_warning)
#
#        btn3 = QPushButton("Open Information Jarvis")
#        btn3.clicked.connect(self.show_info)
#
#        self.label = QLabel()
#        self.label1 = QLabel()
#
#        btn4 = QPushButton("Open Clock")
#        btn4.clicked.connect(self.show_question)
#        
#        btn5 = QPushButton("Exit")
#        btn5.clicked.connect(self.exit)
#        
#        btn = QPushButton('Start Listening..')
#        btn.clicked.connect(self.listen)
#
#        vbox.addWidget(self.label1)
##        vbox.addWidget(btn1)
##        vbox.addWidget(btn2)
##        vbox.addWidget(btn3)
##        vbox.addWidget(btn4)
#        vbox.addWidget(btn)
#        vbox.addWidget(btn5)
#        vbox.addWidget(self.label)
#
#        self.setLayout(vbox)
#        
#    def listen(self):
##        print('qwertyuiopasdfghjklzxcvbnm')
#        Jarvis.checkCommand()
#        
#    def exit(self):
#        app.quit()
##        exit()
#
#    def show_about(self):
#        QMessageBox.about(self, "Jarvis", "This is about application")
#
#    def show_warning(self):
#        QMessageBox.warning(self, "Warning", "This is Warning be alert anything can happen in this cruel world at any time. Don't believe anyone...")
#
#    def show_info(self):
#        QMessageBox.information(self, "Info", "This is Information")
#
#
#    def show_question(self):
#        reply = QMessageBox.question(self, "Jarvis", "Do you want to open Clock",
#                                     QMessageBox.Yes | QMessageBox.No)
#
#
#        if reply == QMessageBox.Yes:
##            self.label.setText("Opening clock")
#            clock = CallPy()
#            clock.call("E:\Abhay\Study\Programs\Python\Project\Clocks\clock.py")
#
#        elif reply == QMessageBox.No:
##            self.label.setText("I Dont Like Pyside2")
#            pass
#
#def get_cred():
#    credPath = 'data/loginInfo/LoginCredentials.uiop'
#    decoded = coder.decoder(credPath)
#    list1 = decoded.replace('username: ','').replace('password: ','').split('\n')
##    print(list1)
#    return list1
#
#class Form(QDialog):
#
#    def __init__(self, parent=None):
#        super(Form, self).__init__(parent)
#        
#        self.setWindowTitle("Jarvis")
#        self.setGeometry(800,500,300,200)
#
#        self.setIcon()
#
#        self.show()
#
#    def setIcon(self):
#        appIcon = QIcon("data/files/ico/icon.png")
#        self.setWindowIcon(appIcon)
#        
#        # Create widgets
#        self.label = QLabel()
#        self.user = QLabel()
#        self.username = QLineEdit("")
#        self.passl = QLabel()
#        self.passw = QLineEdit('')
#        self.button = QPushButton("Login")
#        self.exitbtn = QPushButton('Exit')
#        # Create layout and add widgets
#        layout = QVBoxLayout()
#        layout.addWidget(self.user)
#        layout.addWidget(self.username)
#        layout.addWidget(self.passl)
#        layout.addWidget(self.passw)
#        layout.addWidget(self.button)
#        layout.addWidget(self.exitbtn)
#        layout.addWidget(self.label)
#        # Set dialog layout
#        self.setLayout(layout)
#        # Add button signal to greetings slot
#        self.button.clicked.connect(self.greetings)
#        self.exitbtn.clicked.connect(self.exit)
#        self.user.setText("Username")
#        self.passl.setText('Password')
#        
#        
#    # Greets the user
#    def greetings(self):
#        user = self.username.text()
#        passw = self.passw.text()
#        with open('data/loginInfo/LoginCheck.uiop','w') as f:
#            coded = coder.encoder(f'{user}\n{passw}')
#            f.write(coded)
##        if user == get_cred()[0] and passw == get_cred()[1]:
#        if user == '' and passw == '':
#            print (f"Hi there {self.username.text()}")
##            clock = CallPy()
##            clock.call("E:\Abhay\Study\Programs\Python\Project\Jarvis\Jarvis.py")
#            app.quit()
#                
#        else:
#            self.label.setText('Wrong password or username !')
#            
#    def exit(self):
#        app.quit()
#
## Create and show the form
#form = Form()
#form.show()
## Run the main Qt loop
#app.exec_()
#
#checkInfo = coder.decoder('data/loginInfo/LoginCheck.uiop').split('\n')
#user = checkInfo[0]
#passw = checkInfo[1]
#
#
##if user == get_cred()[0] and passw == get_cred()[1]:
#if user == '' and passw == '':
#    window = Window()
#    app.exec_()
#
#app.quit()



from win10toast import ToastNotifier
toast = ToastNotifier()
toast.show_toast("Jarvis","Hai this notification is from Jarvis",duration=10,icon_path="data/files/ico/bell.ico")