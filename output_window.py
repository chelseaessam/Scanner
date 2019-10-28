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
      count=0
      for word in text:
          
          if len(word)==1:# it will be either symbol or digit
              if word=="{":
                  Is_bracket=True
                  
              if Is_bracket==True and word!="}":
                  continue
              elif Is_bracket==True and word=="}":
                  Is_bracket=False
              elif word in symbols:
                  self.add_item("special symbol",word)
              elif word.isdigit():
                  self.add_item("number",word)
              elif word.isalpha():
                  self.add_item("identifier",word)
              
          elif word==":=":
              self.add_item("special symbol",word)
                  



                  
          else:# if word more than one
              
              if word in reserved:
                  self.add_item("reserved "+word.upper(),word)
              else:
                  mylist=[]
                  count=0
                  new_symbols={ "+" , "-" , "*" , "/" , "=" , "<" , ">" , "(" , ")" , ";" , ":=","{","}"}


                  for element in new_symbols:
                      while element in word:
                          if(word[0]==element):
                            mylist.append(element)
                          else:
                              
                           mylist.append(word[:word.find(element)])
                           mylist.append(element)

                          
                          if len(word[:word.find(element)])+len(element)!=len(word):
                           word=word[word.find(element)+len(element):]
                          else:
                              word=''

                  if word!='' :
                          mylist.append(word)
                          
                          
                  
                  for word in mylist:
                      
                      Is_number=False
                      Is_identifier=False
                      Is_operator=False

                      if word=="{":
                          Is_bracket=True

                      if Is_bracket==True and word!="}" :
                          continue
                      elif Is_bracket==True and word=="}":
                          Is_bracket=False
                      
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
##                 
                             for letter in word:
                                 if letter.isalpha():
                                     Is_identifier=True
                                     
                                 elif letter=="[":
                                     if word.find("]")!=-1:
                                         Is_operator=True
                                         Is_identifier=False
                                         self.add_item("operator",word[0:(word.find("["))])
                                         self.add_item("special symbols","[")
                                         self.add_item("identifier",word[(word.find("[")+1): word.find("]")])
                                         self.add_item("special symbols","]")
                                     else:
                                        Is_identifier=False
                                        break
                                    
                                
                                         
                             if Is_identifier==True and Is_operator==False:
                                 self.add_item("identifier",word)
                             elif Is_identifier== False and Is_operator==False:
                                self.show_msgBox("Syntax Error found in "+word)
                                break    
                                      
                            
                              


































          
##         Is_number=False
##         Is_identifier=False
##         Is_operator=False
##         
#######handling comments##################
##         if (Is_bracket==True) and( word!= "}" or word[len(word)-1]!="}"):
##             continue
##         if Is_bracket==True and (word=="}" or word[len(word)-1]=="}"):
##            Is_bracket=False
##            continue
##         if word[0]=="{" and word[len(word)-1]=="}":
##             continue 

##         

             
