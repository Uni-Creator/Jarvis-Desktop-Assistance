from PyQt5 import QtWidgets, QtGui
# from PyQt5.QtGui import QMovie
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUiType
import ctypes,os,sys

img = []
imgPath = 'D:/AbhaySingh/Programs/Python/Project/Jarvis/data/files/BGW'
for root, dirs, files in os.walk(imgPath):
    for i in files:
        img.append(root + '/' + i)

FROM_MAIN,_ = loadUiType(os.path.join(os.path.dirname(__file__),"./data/GUI/wallpaper.ui"))
class Main(QMainWindow,FROM_MAIN):

    def __init__(self):
        super(Main,self).__init__()
        self.setupUi(self)
        self.imageIndex = 0
        self.image =''
        self.changeBackground()
        self.previous.clicked.connect(self.previousImage)
        self.next.clicked.connect(self.nextImage)
        self.okcancel.accepted.connect(self.setImage)
        self.okcancel.rejected.connect(self.exit)

    def previousImage(self):
        if self.imageIndex > 0:
            self.imageIndex -= 1
            self.changeBackground()

    def nextImage(self):
        if self.imageIndex < len(img)-1:
            self.imageIndex += 1
            self.changeBackground()


    def changeBackground(self):
        from os import walk
        # namedWindow("Wallpaper", WINDOW_NORMAL)
        # resizeWindow("Wallpaper", 480, 10)
        self.image = img[self.imageIndex]
        pic = QtGui.QPixmap(self.image)
        self.background.setPixmap(pic)
        # self.background.setPixmap(f"background-image: url({})")

    def setImage(self):
        if self.image:
            pass
        self.exit()
            # ctypes.windll.user32.SystemParametersInfoW(20, 0, self.image,0)

    def exit(self):
        exit(app.exec_())

def run():
    global app
    app = QtWidgets.QApplication(sys.argv)
    main = Main()
    main.show()
    exit(app.exec_())