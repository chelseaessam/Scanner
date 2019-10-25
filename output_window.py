import sys
from itertools import chain
from os import path

from PyQt5 import QtCore
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from main import *

FORM_CLASS, _ = loadUiType(path.join(path.dirname(__file__), "output_window.ui"))
class OutputWindow(QMainWindow,FORM_CLASS):
 def __init__(self,text, parent=None):
        
        super(OutputWindow, self).__init__(parent)
        QMainWindow.__init__(self)
        self.text=text
        self.setupUi(self)
        self.scanner(text)
        self.buttons()
 def buttons(self):
     self.pushButton.clicked.connect(self.goback)
 def goback(self):
     self.close()
     self.main_window=MainWindow()
     self.main_window.show()
 def scanner(self,text):
      for word in text:
         Is_number=False
         Is_identifier=False
         if word in reserved:
                 self.mylist.addItem(word+",reserved")
                 
         elif word in symbols:
                 self.mylist.addItem(word+",symbols")
                 
         elif word[0].isdigit():
             for letter in word:
                 if letter.isdigit():
                     Is_number=True
                 else:
                     Is_number=False
                     break
             if Is_number==True:
              self.mylist.addItem(word+",number")
         elif word[0].isalpha():
             for letter in word:
                 if letter.isalpha():
                     Is_identifier=True
                 else:
                     Is_identifier=False
                     self.mylist.addItem(word+", error")
                     break
             if Is_identifier==True:
                 self.mylist.addItem(word+" , identifier")
