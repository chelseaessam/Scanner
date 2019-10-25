import sys
from itertools import chain
from os import path

from PyQt5 import QtCore
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType

FORM_CLASS, _ = loadUiType(path.join(path.dirname(__file__), "main_window.ui"))
numbers={'0','1','2','3','4','5','6','7','8','9'}
reserved={"if","then","else","end","repeat","until","read","write"}
symbols = { "+" , "-" , "*" , "/" , "=" , "<" , ">" , "(" , ")" , ";" , ":="}
class MainWindow(QMainWindow,FORM_CLASS):
 def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.buttons()
 def buttons(self):
     self.pushbutton_2.clicked.connect(self.get_text)
 def get_text(self):
     text=self.plainTextEdit.toPlainText()
     self.scanner(text)

 def scanner(self,text):
     
     text=text.split()
     
     
     for word in text:
         Is_number=False
         Is_identifier=False
         if word in reserved:
                 print(word+",reserved")
                 
         elif word in symbols:
                 print(word+",symbols")
                 
         elif word[0].isdigit():
             for letter in word:
                 if letter.isdigit():
                     Is_number=True
                 else:
                     Is_number=False
                     break
             if Is_number==True:
              print(word+",number")
         elif word[0].isalpha():
             for letter in word:
                 if letter.isalpha():
                     Is_identifier=True
                 else:
                     Is_identifier=False
                     print(word+", error")
                     break
             if Is_identifier==True:
                 print(word+" , identifier")
             
         elif word[0] == '{':
             
             
         
    
     
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
