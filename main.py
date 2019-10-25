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
from output_window import *

FORM_CLASS, _ = loadUiType(path.join(path.dirname(__file__), "main_window.ui"))
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
     text=text.split()
     self.close()
     self.new_window=OutputWindow(text)
     self.new_window.show()
         
             
         
    
     
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
