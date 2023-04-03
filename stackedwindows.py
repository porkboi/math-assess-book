# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 10:44:36 2022

@author: chris
"""

import sys

# 1. Import QApplication and all the required widgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, 
    QGridLayout,
    QMainWindow,
    QPushButton,
    QHBoxLayout,
    QVBoxLayout,
    QWidget,
    QLabel,
    QTextEdit,
    QStackedWidget,
    QFormLayout,
    QLineEdit,
    QListWidget,
    )
from PyQt5.QtGui import QPixmap
#from functools import partial
from random import randrange
from PIL import Image
from questiongen import *
from imagegen import *

WINDOW_SIZE=400
BANNER_HEIGHT=35
BUTTON_SIZE=40

class Arith100Window(QWidget):
    '''
    New Window, float free
    '''
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Primary 1 / Arithmetic: 100")
        self.setFixedSize(WINDOW_SIZE, WINDOW_SIZE)
        self.generalLayout=QVBoxLayout()
        centralWidget = QWidget(self)
        centralWidget.setLayout(self.generalLayout)
        self._createBanner()
        self._createsimpleqn()
        self._createsimpleqn2()

    def _createBanner(self):
        self.banner = QLabel()
        self.banner.setText("<h3>Primary 1/ Arithmetic: 100 Questions<h3>")
        self.banner.setAlignment(Qt.AlignCenter)
        self.banner.setFixedHeight(BANNER_HEIGHT)
        self.generalLayout.addWidget(self.banner)

    def _createsimpleqn(self):
        self.createsimpleqn=QHBoxLayout()
        self._simpleqn()
        self._button0()
        self.generalLayout.addLayout(self.createsimpleqn)
    
    def _simpleqn(self):
        self.simpleqn = QTextEdit()
        self.simpleqn.setFixedSize(300,30)
        text = qn1a()
        text = str(text)
        self.simpleqn.setPlainText(text)
        self.simpleqn.setReadOnly(True)
        self.createsimpleqn.addWidget(self.simpleqn)
    
    def _button0(self):
        self.button0 = QPushButton("Re-generate")
        self.button0.clicked.connect(self.regenerate0)
        self.button0.setFixedSize(80, 30)
        self.createsimpleqn.addWidget(self.button0)
    
    def _createsimpleqn2(self):
        self.createsimpleqn2=QHBoxLayout()
        self._simpleqn2()
        self._button1()
        self.generalLayout.addLayout(self.createsimpleqn2)
    
    def _simpleqn2(self):
        self.simpleqn2 = QTextEdit()
        self.simpleqn2.setFixedSize(300,30)
        text = qn1b()
        text = str(text)
        self.simpleqn2.setPlainText(text)
        self.simpleqn2.setReadOnly(True)
        self.createsimpleqn2.addWidget(self.simpleqn2)
    
    def _button1(self):
        self.button1 = QPushButton("Re-generate")
        self.button1.clicked.connect(self.regenerate1)
        self.button1.setFixedSize(80, 30)
        self.createsimpleqn2.addWidget(self.button1)

    def regenerate0(self):
        self.simpleqn.setPlainText(" ")
        text = qn1a()
        text = str(text)
        self.simpleqn.setPlainText(text)
    
    def regenerate1(self):
        self.simpleqn2.setPlainText(" ")
        text = qn1b()
        text = str(text)
        self.simpleqn2.setPlainText(text)

class AddSubWindow(QWidget):
    '''
    New Window, float free
    '''
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Primary 1 / Addition and Subtraction")
        self.setFixedSize(WINDOW_SIZE, WINDOW_SIZE)
        self.generalLayout=QVBoxLayout()
        centralWidget = QWidget(self)
        centralWidget.setLayout(self.generalLayout)
        self._createBanner()
        self._createqn()

    def _createBanner(self):
        self.banner = QLabel()
        self.banner.setText("<h3>Primary 1 / Addition and Subtraction<h3>")
        self.banner.setAlignment(Qt.AlignCenter)
        self.banner.setFixedHeight(BANNER_HEIGHT)
        self.generalLayout.addWidget(self.banner)

    def _createqn(self):
        self.createqn=QHBoxLayout()
        self._createQuestion()
        self._createButtons()
        self.generalLayout.addLayout(self.createqn)
        
    def _createQuestion(self):
        self.question = QTextEdit()
        self.question.setFixedSize(300,50)
        text = qn2a()
        text = str(text)
        self.question.setPlainText(text)
        self.question.setReadOnly(True)
        self.createqn.addWidget(self.question)
        
    def _createButtons(self):
        self.button = QPushButton("Re-generate")
        self.button.clicked.connect(self.regenerate)
        self.button.setFixedSize(80, 30)
        self.createqn.addWidget(self.button)
        
    def regenerate(self):
        self.question.setPlainText(" ")
        text = qn2a()
        text = str(text)
        self.question.setPlainText(text)

class MulDivWindow(QWidget):
    '''
    New Window, float free
    '''
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Primary 1 / Multiplication and Division")
        self.setFixedSize(WINDOW_SIZE, WINDOW_SIZE)
        self.generalLayout=QVBoxLayout()
        centralWidget = QWidget(self)
        centralWidget.setLayout(self.generalLayout)
        self._createBanner()
        self._createqn3a()
        self._createqn3b()
        self.regenerate3a()

    def _createBanner(self):
        self.banner = QLabel()
        self.banner.setText("<h3>Primary 1/ Multiplication and Division<h3>")
        self.banner.setAlignment(Qt.AlignCenter)
        self.banner.setFixedHeight(BANNER_HEIGHT)
        self.generalLayout.addWidget(self.banner)

    def _createqn3a(self):
        self.createqn3a=QHBoxLayout()
        self._qn3a()
        self._button3a()
        self.generalLayout.addLayout(self.createqn3a)
    
    def _qn3a(self):
        self.qn3a = QTextEdit()
        self.qn3a.setFixedSize(300,40)
        text = qn3a()
        text = str(text)
        self.qn3a.setPlainText(text)
        self.qn3a.setReadOnly(True)
        self.createqn3a.addWidget(self.qn3a)
    
    def _button3a(self):
        self.button3a = QPushButton("Re-generate")
        self.button3a.clicked.connect(self.regenerate3a)
        self.button3a.setFixedSize(80, 30)
        self.createqn3a.addWidget(self.button3a)

    def regenerate3a(self):
        self.qn3a.setPlainText(" ")
        text = qn3a()
        text = str(text)
        self.qn3a.setPlainText(text)
    
    def _createqn3b(self):
        self.createqn3b=QHBoxLayout()
        self._qn3b()
        self._button3b()
        self.generalLayout.addLayout(self.createqn3b)
    
    def _qn3b(self):
        self.qn3b = QTextEdit()
        self.qn3b.setFixedSize(300,40)
        text = qn3b()
        text = str(text)
        self.qn3b.setPlainText(text)
        self.qn3b.setReadOnly(True)
        self.createqn3b.addWidget(self.qn3b)
    
    def _button3b(self):
        self.button3b = QPushButton("Re-generate")
        self.button3b.clicked.connect(self.regenerate3b)
        self.button3b.setFixedSize(80, 30)
        self.createqn3b.addWidget(self.button3b)

    def regenerate3b(self):
        self.qn3b.setPlainText(" ")
        text = qn3b()
        text = str(text)
        self.qn3b.setPlainText(text)

class MoneyWindow(QWidget):
    '''
    New Window, float free
    '''
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Primary 1 / Money")
        self.setFixedSize(WINDOW_SIZE, WINDOW_SIZE)
        self.generalLayout=QVBoxLayout()
        centralWidget = QWidget(self)
        centralWidget.setLayout(self.generalLayout)
        self.moneybanner()
        self._createqn4a()
    
    def moneybanner(self):
        self.banner = QLabel()
        self.banner.setText("<h3>Primary 1/ Money<h3>")
        self.banner.setAlignment(Qt.AlignCenter)
        self.banner.setFixedHeight(BANNER_HEIGHT)
        self.generalLayout.addWidget(self.banner)
    
    def _createqn4a(self):
        self.createqn4a=QHBoxLayout()
        self._createquestionpartofqn4a()
        self._button4a()
        self.generalLayout.addLayout(self.createqn4a)
    
    def _createquestionpartofqn4a(self):
        self.createquestionpartofqn4a=QVBoxLayout()
        self._qn4a()
        self._qn4aimages()
        self.createqn4a.addLayout(self.createquestionpartofqn4a)
        
    def _qn4a(self):
        self.qn4a=QTextEdit()
        self.qn4a.setFixedSize(300,25)
        onedollarint, fiftycentint, twentycentint, tencentint, text = qn4a()
        self.onedollarint = onedollarint
        self.fiftycentint = fiftycentint
        self.twentycentint = twentycentint
        self.tencentint = tencentint
        
        self.qn4a.setPlainText(text)
        self.qn4a.setReadOnly(True)
        self.createquestionpartofqn4a.addWidget(self.qn4a)
    
    def _qn4aimages(self):
        self.qn4aimages = QLabel()
        self.qn4aimages.setFixedSize(300,300)
        onedollar_image = Image.open('src/onedollar.jpg')
        fiftycent_image = Image.open('src/fiftycent.jpg')
        twentycent_image = Image.open('src/twentycent.jpg')
        tencent_image = Image.open('src/tencent.jpg')
        onedollarmosiac = coinmosiac(onedollar_image, self.onedollarint)
        fiftycentmosiac = coinmosiac(fiftycent_image, self.fiftycentint)
        twentycentmosiac = coinmosiac(twentycent_image, self.twentycentint)
        tencentmosiac = coinmosiac(tencent_image, self.tencentint)
        bigmosiac = big_mosiac(onedollarmosiac, fiftycentmosiac, twentycentmosiac, tencentmosiac)
        im = bigmosiac.save('src/tempmosiac.jpg')
        
        pixmap = QPixmap('src/tempmosiac.jpg')
        self.qn4aimages.setPixmap(pixmap)
        self.qn4aimages.setScaledContents(True)
        self.createquestionpartofqn4a.addWidget(self.qn4aimages)
    
    def _button4a(self):
        self.button4a = QPushButton("Re-generate")
        self.button4a.clicked.connect(self.regenerate4a)
        self.button4a.setFixedSize(80, 30)
        self.createqn4a.addWidget(self.button4a)

    def regenerate4a(self):
        self.qn4a.setPlainText(" ")
        onedollarint, fiftycentint, twentycentint, tencentint, text = qn4a()
        self.onedollarint = onedollarint
        self.fiftycentint = fiftycentint
        self.twentycentint = twentycentint
        self.tencentint = tencentint
        text = str(text)
        self.qn4a.setPlainText(text)
        
        onedollar_image = Image.open('src/onedollar.jpg')
        fiftycent_image = Image.open('src/fiftycent.jpg')
        twentycent_image = Image.open('src/twentycent.jpg')
        tencent_image = Image.open('src/tencent.jpg')
        onedollarmosiac = coinmosiac(onedollar_image, self.onedollarint)
        fiftycentmosiac = coinmosiac(fiftycent_image, self.fiftycentint)
        twentycentmosiac = coinmosiac(twentycent_image, self.twentycentint)
        tencentmosiac = coinmosiac(tencent_image, self.tencentint)
        bigmosiac = big_mosiac(onedollarmosiac, fiftycentmosiac, twentycentmosiac, tencentmosiac)
        im = bigmosiac.save('src/tempmosiac.jpg')
        
        pixmap = QPixmap('src/tempmosiac.jpg')
        self.qn4aimages.setPixmap(pixmap)
        self.qn4aimages.setScaledContents(True)
        
class MathQnBankWindow(QWidget):

   def __init__(self):
      super().__init__()
      self.setWindowTitle("Math Question Generator")
      self.setFixedSize(700, WINDOW_SIZE)

      #banner
      self.banner = QLabel()
      self.banner.setText("<h1>Math Question Generator<h1>")
      self.banner.setAlignment(Qt.AlignCenter)
      self.banner.setFixedHeight(BANNER_HEIGHT)
      #list
      self.leftlist = QListWidget ()
      self.leftlist.insertItem (0, 'Primary 1')
      self.leftlist.insertItem (1, 'Primary 2')
      self.leftlist.insertItem (2, 'Primary 3')
      self.leftlist.insertItem (3, 'Primary 4')
      self.leftlist.insertItem (4, 'Primary 5')
      self.leftlist.insertItem (5, 'Primary 6')
		
#     self.noteswindow = QWidget()
      self.primary1window = QWidget()
      self.primary2window = QWidget()
#     self.primary3window = QWidget()
#     self.primary4window = QWidget()
#     self.primary5window = QWidget()
#     self.primary6window = QWidget()
#     self.iflwindow = QWidget()

#     self.notesUI()
      self.primary1UI()
      self.primary2UI()
#     self.primary3UI()
#     self.primary4UI()
#     self.primary5UI()
#     self.primary6UI()
#     self.iflUI()
		
      self.stack = QStackedWidget (self)
#     self.stack.addWidget (self.notes)
      self.stack.addWidget (self.primary1window)
      self.stack.addWidget (self.primary2window)
#     self.stack.addWidget (self.primary3window)
#     self.stack.addWidget (self.primary4window)
#     self.stack.addWidget (self.primary5window)
#     self.stack.addWidget (self.primary6window)
#     self.stack.addWidget (self.iflwindow)
		
      hbox=QHBoxLayout()
      hbox.addWidget(self.leftlist)
      hbox.addWidget(self.stack)
      
      vbox=QVBoxLayout(self)
      vbox.addWidget(self.banner)
      vbox.addLayout(hbox)
      
      self.setLayout(vbox)
      self.leftlist.currentRowChanged.connect(self.display)
      self.setGeometry(50, 50, 10,10)
      self.show()

   def Arith100(self, checked):
      self.w = Arith100Window()
      self.w.show()
    
   def AddSub(self, checked):
       self.w = AddSubWindow()
       self.w.show()
       
   def MulDiv(self, checked):
       self.w = MulDivWindow()
       self.w.show()
  
   def Money(self,checked):
       self.w = MoneyWindow()
       self.w.show()

   def primary1UI(self):
      layout = QVBoxLayout()
      #banner
      self.bannerpri1 = QLabel()
      self.bannerpri1.setText("<h2>Primary 1 Math Syllabus<h2>")
      self.bannerpri1.setAlignment(Qt.AlignCenter)
      self.bannerpri1.setFixedHeight(BANNER_HEIGHT)
      
      #buttons
      buttonsLayout = QGridLayout()
      
      btn1a = QPushButton("Numbers to 100")
      btn1a.setFixedSize(150, BUTTON_SIZE)
      buttonsLayout.addWidget(btn1a,0,0)
      btn1a.clicked.connect(self.Arith100)
      
      btn1b = QPushButton("Addition and Subtraction")
      btn1b.setFixedSize(150, BUTTON_SIZE)
      buttonsLayout.addWidget(btn1b, 0, 1)
      btn1b.clicked.connect(self.AddSub)
      
      btn1c = QPushButton("Multiplication and Division")
      btn1c.setFixedSize(150, BUTTON_SIZE)
      buttonsLayout.addWidget(btn1c, 0, 2)
      btn1c.clicked.connect(self.MulDiv)
      
      btn1d = QPushButton("Money")
      btn1d.setFixedSize(150, BUTTON_SIZE)
      buttonsLayout.addWidget(btn1d, 1, 0)
      btn1d.clicked.connect(self.Money)
      
      btn1e = QPushButton("Length")
      btn1e.setFixedSize(150,BUTTON_SIZE)
      buttonsLayout.addWidget(btn1e, 1, 1)
 
      btn1f = QPushButton("Time")
      btn1f.setFixedSize(150,BUTTON_SIZE)
      buttonsLayout.addWidget(btn1f, 1, 2)
      
      btn1g = QPushButton("2D Shapes")
      btn1g.setFixedSize(150,BUTTON_SIZE)
      buttonsLayout.addWidget(btn1g, 2, 0)
      
      btn1h = QPushButton("Length")
      btn1h.setFixedSize(150,BUTTON_SIZE)
      buttonsLayout.addWidget(btn1h, 2, 1)
      
      btn1i = QPushButton("Exam Revision")
      btn1i.setFixedSize(150,BUTTON_SIZE)
      buttonsLayout.addWidget(btn1i, 2, 2)
   
      layout.addWidget(self.bannerpri1)
      layout.addLayout(buttonsLayout)
      self.primary1window.setLayout(layout)
    		
   def primary2UI(self):
      layout = QVBoxLayout()
      #banner
      self.bannerpri2 = QLabel()
      self.bannerpri2.setText("<h2>Primary 2 Math Syllabus<h2>")
      self.bannerpri2.setAlignment(Qt.AlignCenter)
      self.bannerpri2.setFixedHeight(BANNER_HEIGHT)
      
      #buttons
      buttonsLayout = QGridLayout()
      
      btn2a = QPushButton("Numbers to 1000")
      btn2a.setFixedSize(150, BUTTON_SIZE)
      buttonsLayout.addWidget(btn2a,0,0)
#      btn1a.clicked.connect(self.Arith100)
      
      btn2b = QPushButton("Addition and Subtraction")
      btn2b.setFixedSize(150, BUTTON_SIZE)
      buttonsLayout.addWidget(btn2b, 0, 1)
      
      btn2c = QPushButton("Multiplication and Division")
      btn2c.setFixedSize(150, BUTTON_SIZE)
      buttonsLayout.addWidget(btn2c, 0, 2)
      
      btn2d = QPushButton("Money")
      btn2d.setFixedSize(150, BUTTON_SIZE)
      buttonsLayout.addWidget(btn2d, 1, 0)
      
      btn2e = QPushButton("Length, Mass, Volume")
      btn2e.setFixedSize(150,BUTTON_SIZE)
      buttonsLayout.addWidget(btn2e, 1, 1)
 
      btn2f = QPushButton("Fractions")
      btn2f.setFixedSize(150,BUTTON_SIZE)
      buttonsLayout.addWidget(btn2f, 1, 2)
      
      btn2g = QPushButton("2D Shapes")
      btn2g.setFixedSize(150,BUTTON_SIZE)
      buttonsLayout.addWidget(btn2g, 2, 0)
      
      btn2h = QPushButton("3D Shapes")
      btn2h.setFixedSize(150,BUTTON_SIZE)
      buttonsLayout.addWidget(btn2h, 2, 1)
      
      btn2i = QPushButton("Time")
      btn2i.setFixedSize(150,BUTTON_SIZE)
      buttonsLayout.addWidget(btn2i, 2, 2)

      btn2j = QPushButton("Picture Graphs")
      btn2j.setFixedSize(150,BUTTON_SIZE)
      buttonsLayout.addWidget(btn2j, 3, 0)

      btn2k = QPushButton("Exam Revision")
      btn2k.setFixedSize(150,BUTTON_SIZE)
      buttonsLayout.addWidget(btn2k, 3, 1)      
   
      layout.addWidget(self.bannerpri2)
      layout.addLayout(buttonsLayout)
      self.primary2window.setLayout(layout)      
   
   def display(self,i):
       self.stack.setCurrentIndex(i)
		
def main():
    mathqnbankApp = QApplication([])
    mathqnbank = MathQnBankWindow()
    mathqnbank.show()
    sys.exit(mathqnbankApp.exec())
	
if __name__ == '__main__':
   main()