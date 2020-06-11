import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import uic
import lolAutoPicker
import threading
import os, re
import pyperclip

# from PyQt5.QtWebEngineWidgets import *

form_class = uic.loadUiType("lolAutoPickerUI.ui")[0]

class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

        self.start_button.clicked.connect(self.findStart)
        self.stop_button.clicked.connect(self.findStop)

        self.radio_resolution1024X576.clicked.connect(self.changeResolution)
        self.radio_resolution1280X720.clicked.connect(self.changeResolution)
        self.radio_resolution1600X900.clicked.connect(self.changeResolution)
        self.radio_resolution1920X1080.clicked.connect(self.changeResolution)

        self.varStop = False
        self.current_thread=None
        self.lap = lolAutoPicker.lolAutoPick()
        # self.chat_edit.textChanged.connect(self.copyChat)

    def findStart(self):
        if self.current_thread:
            return
        self.current_thread = threading.Thread(target=myWindow.find)
        self.current_thread.start()
        
    def findStop(self):
        self.current_thread=None
        self.varStop=True
        self.status_label.setText("Click Start")

    def find(self):
        print('find start')
        before_copied=""
        accepted = False
        while not self.varStop:
            self.status_label.setText("Auto picking")

            if self.lap.acceptGame():
<<<<<<< HEAD
                accepted=True

            if accepted and self.lap.firstChat(self.chat_edit.text()):
                self.lap.selectChampion(self.champion_box.currentText())
                self.lap.selectSpell(self.spell_box1.currentText(), self.spell_box2.currentText())
                accepted=False
            else:
                pyperclip.copy(before_copied)
        self.varStop = False
=======
                pyperclip.copy(self.chat_edit.text())
                print("accepted game")
                if self.lap.check_pick_champ_location():
                    self.lap.firstChat()
                    print('chat complete')
                    self.lap.selectChampion(self.champion_box.currentText())
                    self.lap.selectSpell(self.spell_box1.currentText(), self.spell_box2.currentText())
                    self.status_label.setText("Select Done if you want restart click start button")
                    break
                
        self.varStop=False
>>>>>>> master

    def changeResolution(self):
        if self.radio_resolution1024X576.isChecked():
            self.lap.currentResoulution = str(1024)
        elif self.radio_resolution1280X720.isChecked():
            self.lap.currentResoulution = str(1280)
        elif self.radio_resolution1600X900.isChecked():
            self.lap.currentResoulution = str(1600)
        elif self.radio_resolution1920X1080.isChecked():
            self.lap.currentResoulution = str(1920)

    def setting(self):
        #전에 설정한 사이즈를 불러온다
        if self.lap.currentResoulution == str(1024):
            self.radio_resolution1024X576.setChecked(True)
        elif self.lap.currentResoulution == str(1280):
            self.radio_resolution1280X720.setChecked(True)
        elif self.lap.currentResoulution == str(1600):
            self.radio_resolution1600X900.setChecked(True)
        elif self.lap.currentResoulution == str(1920):
            self.radio_resolution1920X1080.setChecked(True)
            
        if not self.lap.checkChampionDownload():
            for champ in self.lap.champion_list:
                self.status_label.setText("Champion Image Downloading : " + champ)
                self.lap.championImageDownload(champ)
            self.lap.championCrop()
            self.status_label.setText('Image download done!')


        #box에 챔피언목록 추가
        for champ in self.lap.champion_list:
            self.champion_box.addItem(champ)
        rl = re.compile('choiced*')

        #box에 스펠목록 추가
        for spell in os.listdir('img/spell/1920'):
            if not rl.match(spell):
                self.spell_box1.addItem(spell[:-4])
                self.spell_box2.addItem(spell[:-4])

            
if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    threading.Thread(target=myWindow.setting).start()
    sys.exit(app.exec_())