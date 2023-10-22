from PyQt5.QtCore import Qt, QTimer, QTime
from PyQt5.QtWidgets import (
        QApplication, QWidget, 
        QHBoxLayout, QVBoxLayout, 
        QGroupBox, QRadioButton,
        QPushButton, QLabel, QListWidget, QLineEdit)
from PyQt5.QtGui import QFont

from instr import *
from final_win import *

class Experiment():
   def __init__(self, age, test1, test2, test3):
       self.age = int(age)
       self.t1 = int(test1)
       self.t2 = int(test2)
       self.t3 = int(test3)


class TestWin(QWidget):
    def __init__(self):
        ''' вікно, в якому проводиться опитування '''
        super().__init__()

        self.initUI()
        self.set_appear()
        self.show()
    
    def set_appear(self):
        ''' встановлює, як виглядатиме вікно (напис, розмір, місце) '''
        self.setWindowTitle(txt_title)
        self.setGeometry(win_x, win_y, win_width, win_height)
      
      
    def second(self):
        global time
        time = time.addSecs(-1)
        self.timert.setText(time.toString("hh:mm:ss"))
        if time.toString("hh:mm:ss") == "00:00:00":
            self.timer.stop()
            self.rez_1.setDisabled(False)
    
    def second12(self):
        global time
        time = time.addSecs(-1)
        self.timert.setText(time.toString("hh:mm:ss"))
        if time.toString("hh:mm:ss") == "00:00:00":
            self.timer.stop()
        
    def second1(self):
        global time
        time = time.addSecs(-1)
        self.timert.setText(time.toString("hh:mm:ss"))
        if time.toString("hh:mm:ss") == "00:00:45":
            self.timert.setStyleSheet("color: rgb(0,230,0)")
            self.rez_2.setDisabled(False)
        if time.toString("hh:mm:ss") == "00:00:15":
            self.timert.setStyleSheet("color: rgb(0,0,0)")
        if time.toString("hh:mm:ss") == "00:00:00":
            self.timer.stop()  
            self.rez_3.setDisabled(False)  
        
    def start_clicker(self):
        global time
        time = QTime(0,0,15)
        
        self.timer = QTimer()    
        self.timer.timeout.connect(self.second)
        self.timer.start(1000)
        
        
    def start_clicker1(self):
        global time
        time = QTime(0,0,45)
        
        self.timer = QTimer()    
        self.timer.timeout.connect(self.second12)
        self.timer.start(1000)
        
    def start_clicker2(self):
        global time
        time = QTime(0,1,0)
        
        self.timer = QTimer()    
        self.timer.timeout.connect(self.second1)
        self.timer.start(1000)
        
        

    def on_click(self):
        self.hide()
        
        self.exp = Experiment(
            self.rez_age.text(),
            self.rez_1.text(),
            self.rez_2.text(),
            self.rez_3.text()
        )
        self.fw = FinalWin(self.exp)

    def initUI(self):
        ''' створює графічні елементи '''
        self.pib = QLabel(txt_name)
        self.rez_pib = QLineEdit(txt_hintname)
        self.age = QLabel(txt_age)
        self.rez_age = QLineEdit(txt_hintage)
        self.info1 = QLabel(txt_test1)
        self.bust1 = QPushButton(txt_starttest1)
        self.rez_1 = QLineEdit(txt_hinttest1)
        self.rez_1.setDisabled(True)
        self.info2 = QLabel(txt_test2)
        self.bust2 = QPushButton(txt_starttest2)
        self.info3 = QLabel(txt_test3)
        self.bust3 = QPushButton(txt_starttest3)
        self.rez_2 = QLineEdit(txt_hinttest2)
        self.rez_2.setDisabled(True)
        self.rez_3 = QLineEdit(txt_hinttest3)
        self.rez_3.setDisabled(True)
        self.fbu = QPushButton(txt_sendresults)
        
        self.linev1 = QVBoxLayout()
        
        self.linev1.addWidget(self.pib)
        self.linev1.addWidget(self.rez_pib)
        self.linev1.addWidget(self.age)
        self.linev1.addWidget(self.rez_age)
        self.linev1.addWidget(self.info1)
        self.linev1.addWidget(self.bust1)
        self.linev1.addWidget(self.rez_1)
        self.linev1.addWidget(self.info2)
        self.linev1.addWidget(self.bust2)
        self.linev1.addWidget(self.info3)
        self.linev1.addWidget(self.bust3)
        self.linev1.addWidget(self.rez_2)
        self.linev1.addWidget(self.rez_3)
        self.linev1.addWidget(self.fbu, alignment= Qt.AlignCenter)
        
        self.timert = QLabel(txt_timer)
        self.timert.setFont(QFont("Times", 36, QFont.Bold))
        self.timert.setStyleSheet("color: rgb(0,0,0)")
        
        self.linev2 = QVBoxLayout()
        
        self.linev2.addWidget(self.timert)
        
        self.lineh = QHBoxLayout()
        
        
        
        self.lineh.addLayout(self.linev1)
        
        self.lineh.addLayout(self.linev2)
        
        
        self.setLayout(self.lineh)
        
        self.fbu.clicked.connect(self.on_click)
        self.bust1.clicked.connect(self.start_clicker)
        self.bust2.clicked.connect(self.start_clicker1)
        self.bust3.clicked.connect(self.start_clicker2)
        

    

