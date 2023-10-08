from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
        QApplication, QWidget, 
        QHBoxLayout, QVBoxLayout, 
        QGroupBox, QRadioButton,
        QPushButton, QLabel, QListWidget, QLineEdit)

from instr import *
from final_win import *

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

    def initUI(self):
        ''' створює графічні елементи '''
        self.pib = QLabel(txt_name)
        self.rez_pib = QLineEdit(txt_hintname)
        self.age = QLabel(txt_age)
        self.rez_age = QLineEdit(txt_hintage)
        self.info1 = QLabel(txt_test1)
        self.bust1 = QPushButton(txt_starttest1)
        self.rez_1 = QLineEdit(txt_hinttest1)
        self.info2 = QLabel(txt_test2)
        self.bust2 = QPushButton(txt_starttest2)
        self.info3 = QLabel(txt_test3)
        self.bust3 = QPushButton(txt_starttest3)
        self.rez_2 = QLineEdit(txt_hinttest2)
        self.rez_3 = QLineEdit(txt_hinttest3)
        
        
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
        
        self.timer = QLabel(txt_timer)
        
        self.linev2 = QVBoxLayout()
        
        self.linev2.addWidget(self.timer)
        
        self.lineh = QHBoxLayout()
        
        self.fbu = QPushButton(txt_sendresults)
        
        self.lineh.addLayout(self.linev1)
        
        self.lineh.addLayout(self.linev2)
        
        
        self.setLayout(self.lineh)
        
app = QApplication([])
mw = TestWin()
app.exec_()
    

