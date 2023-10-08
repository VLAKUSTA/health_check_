from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
        QApplication, QWidget, 
        QHBoxLayout, QVBoxLayout, QGridLayout, 
        QGroupBox, QRadioButton,
        QPushButton, QLabel, QListWidget, QLineEdit)
        
from instr import *

class FinalWin(QWidget):
    ''' вікно, в якому проводиться опитування '''
    def __init__(self):
        
        super().__init__()

        self.initUI()
        self.set_appear()
        self.show()
    
    def initUI(self):
       ''' створює графічні елементи '''
       self.index_text = QLabel(txt_index)
       self.result_text = QLabel(txt_finalwin)

       self.layout = QVBoxLayout()
       
       self.layout.addWidget(self.index_text)
       self.layout.addWidget(self.result_text)
       self.setLayout(self.layout)
       

    def set_appear(self):
        ''' встановлює, як виглядатиме вікно (напис, розмір, місце) '''
        self.setWindowTitle(txt_title)
        self.setGeometry(win_x, win_y, win_width, win_height)
        
        # TODO вствановити розмір вікна в pyqt
        # TODO вствановити місце де вікно зявлятиметься в pyqt





