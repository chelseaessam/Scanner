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
      to_break=False
      index=-1
      for word in text:
          index=index+1
          if Is_bracket==True and "}" not in word and index==len(text)-1:
                  self.show_msgBox("Unbalanced curly brackets")
                  break
          if len(word)==1:# it will be either symbol or digit
              
              if word=="{" and index==len(text)-1:
                  self.show_msgBox("Unbalanced curly brackets")
                  break
              elif word=="{":
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
              
              if word in reserved and Is_bracket!=True:
                  self.add_item("reserved "+word.upper(),word)
              else:
                  mylist=[]
                  new_symbols={ "+" , "-" , "*" , "/" , "=" , "<" , ">" , "(" , ")" , ";" ,"{","}"}
                  count=0


                  for letter in word:
                      if letter in new_symbols:
                          
                           if letter=="=" and count-1>0 and mylist[count-1]==":=":
                              continue
                           else:

                               if(word[0]==letter):
                                   mylist.append(letter)
                                   word=word[slice(word.find(letter)+1,len(word),1)]
                                   count=count+1
                               else:
                                   
                                   mylist.append(word[slice(0,word.find(letter),1)])
                                   mylist.append(letter)
                                   count=count+2

                          
                                   if len(word[:word.find(letter)])+len(letter)!=len(word):
                                    word=word[slice(word.find(letter)+len(letter),len(word),1)]
                                   else:
                                      word=''
                      elif letter==":" and word.find(letter)!=len(word)-1 and word[word.find(letter)+1]=="=":
                          mylist.append(word[slice(0,word.find(letter),1)])
                          mylist.append(":=")
                          word=word[slice(word.find(letter)+2,len(word),1)]
                          count=count+2
                      
                          
                          

                  if word!='' :
                          mylist.append(word)
                          
                  count=0
                  for word in mylist:
                      Is_number=False
                      Is_identifier=False
                      Is_operator=False

                      if Is_bracket==True and word!="}" and index==len(text)-1 and count==len(mylist)-1:
                       self.show_msgBox("Unbalanced curly brackets")
                       break
                      elif word=="{":
                          Is_bracket=True

                      elif Is_bracket==True and word!="}" :
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
                                    to_break=True
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
                                to_break=True
                                break    
                            
                      count=count+1
                  if to_break==True:
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

             
