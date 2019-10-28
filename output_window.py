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
        self.table_setup()
        self.scanner(text)
 def table_setup(self):
     self.tableWidget.setColumnCount(2)
     columnsLabels = ['Token Type', 'Token Value']
     self.tableWidget.setHorizontalHeaderLabels(columnsLabels)

 def add_item(self,token_type,token_value):
     num_rows=self.tableWidget.rowCount()
     self.tableWidget.insertRow(num_rows)
     self.tableWidget.setItem(num_rows, 0, QTableWidgetItem(token_type))
     self.tableWidget.setItem(num_rows, 1, QTableWidgetItem(token_value))

     
 def show_msgBox(self,msg):
        self.msgBox=QMessageBox()
        self.msgBox.setWindowTitle("Error!")
        self.msgBox.setIcon(QMessageBox.Warning)
        self.msgBox.setText(msg)
        self.msgBox.setStandardButtons(QMessageBox.Ok)
        self.msgBox.exec_()
        
 
 def scanner(self,text):
      Is_bracket=False
      for word in text:
         Is_number=False
         Is_identifier=False
         Is_operator=False
         
#####handling comments##################
         if (Is_bracket==True) and( word!= "}" or word[len(word)-1]!="}"):
             continue
         if Is_bracket==True and (word=="}" or word[len(word)-1]=="}"):
            Is_bracket=False
            continue
         if word[0]=="{" and word[len(word)-1]=="}":
             continue 
#####reserved words################
         
         elif word in reserved:
                 self.add_item("reserved",word)
######special symbols########################                 
                 
         elif word in symbols:
                 self.add_item("special symbols",word)
                 
                 
         elif word[0].isdigit():
             for letter in word:
                 if letter.isdigit():
                     Is_number=True
                 else:
                     Is_number=False
                     break
             if Is_number==True:
              self.add_item("number",word)
             else:
                self.show_msgBox("Syntax Error found in "+word)
                break

              
         elif word[0].isalpha():
             
             for letter in word:
                 if letter.isalpha():
                     Is_identifier=True
                     
                 elif letter=="[":
                     Is_operator=True
                     Is_identifier=False
                     self.add_item("operator",word[0:(word.find("["))])
                     self.add_item("identifier",word[(word.find("[")+1): word.find("]")])
                 else:
                    Is_identifier=False
                    break
                
                
             if Is_identifier==True and Is_operator==False:
                 self.add_item("identifier",word)
             elif Is_identifier== False and Is_operator==False:
                self.show_msgBox("Syntax Error found in "+word)
                break
            
         elif word =="{" or word[0]=="{":
                Is_bracket=True
                

             
