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

FORM_CLASS, _ = loadUiType(path.join(path.dirname(__file__), "C:\\Users\\Dell\\Desktop\\scanner2\\main_window.ui"))
reserved={"if","then","else","end","repeat","until","read","write"}
symbols = { "+" , "-" , "*" , "/" , "=" , "<" , ">" , "(" , ")" , ";" , ":="}
class MainWindow(QMainWindow,FORM_CLASS):
 def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.table_setup()
        self.buttons()
 def buttons(self):
     self.pushbutton_2.clicked.connect(self.get_text)
     self.pushButton.clicked.connect(self.clear_text)
 def clear_text(self):
     self.plainTextEdit.clear()
 def show_msgBox(self,msg):
    self.msgBox=QMessageBox()
    self.msgBox.setWindowTitle("Error!")
    self.msgBox.setIcon(QMessageBox.Warning)
    self.msgBox.setText(msg)
    self.msgBox.setStandardButtons(QMessageBox.Ok)
    self.msgBox.exec_()
 def show_alertBox(self,msg):
    self.msgBox=QMessageBox()
    self.msgBox.setWindowTitle("Alert!")
    self.msgBox.setIcon(QMessageBox.Warning)
    self.msgBox.setText(msg)
    self.msgBox.setStandardButtons(QMessageBox.Ok)
    self.msgBox.exec_()
     
 def table_setup(self):
     self.tableWidget.setColumnCount(2)
     columnsLabels = ['Token Type', 'Token Value']
     self.tableWidget.setHorizontalHeaderLabels(columnsLabels)

 def add_item(self,token_type,token_value):
     num_rows=self.tableWidget.rowCount()
     self.tableWidget.insertRow(num_rows)
     self.tableWidget.setItem(num_rows, 0, QTableWidgetItem(token_type))
     self.tableWidget.setItem(num_rows, 1, QTableWidgetItem(token_value))
     
     
 def get_text(self):
     text1=self.plainTextEdit.toPlainText()
     if not text1:
         self.show_msgBox("You must enter a code")
         
     else:
         while self.tableWidget.rowCount() > 0:
      
               self.tableWidget.removeRow(0)
       
         #text=text.split()
         self.scanner(text1)
         
             
         
 def scanner(self,text1):
      text=text1.split()
      bracket_list=[]
      bcount=-1
      
      to_break=False
      index=-1
      for word in text:
          index=index+1
          if bcount!=-1 and word!="}" and index==len(text)-1:
                  self.show_msgBox("Unbalanced curly brackets")
                  break
          if len(word)==1:# it will be either symbol or digit
              
              if bcount!=-1 and word!="}" and index==len(text)-1:
                  self.show_msgBox("Unbalanced curly brackets")
                  break
              elif word=="{":
                  bracket_list.append("{")
                  bcount=bcount+1
                  
              
              elif word=="}":
                  if bcount!=-1:#there was left bracket found
                      index=text1.find("}")
                      
                      if index+1< len(text1) and text1.find("}",index+1,len(text1))!=-1: # there is another right bracket
                         bracket_list.pop()
                         bcount=bcount-1
                      else:
                         bcount=-1 #empty the list
                  else:
                      self.show_msgBox("Syntax Error found in }")
                      break
              if bcount!=-1  :#and (text1.find("}")!=-1 )
                  continue
              elif word in symbols:
                  self.add_item("special symbol",word)
              elif word.isdigit():
                  self.add_item("number",word)
              elif word.isalpha():
                  self.add_item("identifier",word)
              
          elif word==":=" and bcount==-1:
              self.add_item("special symbol",word)
                  



                  
          else:# if word more than one
              
              if word in reserved and bcount==-1:
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
                          
                  count=-1
                  for word in mylist:
                      count=count+1
                      Is_number=False
                      Is_identifier=False
                      Is_operator=False

                      if bcount!=-1 and word!="}" and index==len(text)-1 and count==len(mylist)-1:
                       self.show_msgBox("Unbalanced curly brackets")
                       break
                      elif word=="{":
                          bracket_list.append("{")
                          bcount=bcount+1

                      
                        
                      elif word=="}":
                           if bcount!=-1:#there was left bracket found
                              index=text1.find("}")
                              if index+1<len(text1) and text1.find("}",index+1,len(text1))!=-1: # there is another right bracket
                                     bracket_list.pop()
                                     bcount=bcount-1
                              else:
                                bcount=-1 #empty the list
                           else:
                               self.show_msgBox("Syntax Error found in }")
                               to_break=True
                               break
                      elif bcount!=-1:#and (text1.find("}")!=-1 )
                          continue
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
                            
                  if to_break==True:
                        break
                
      if self.tableWidget.rowCount()==0:
          self.show_alertBox("There is no output")
          
    
     
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
