from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
        QApplication, QWidget, 
        QHBoxLayout, QVBoxLayout, 
        QGroupBox, QRadioButton,
        QPushButton, QLabel, QListWidget, QLineEdit)

from instr import *
from second_win import *

     
       
class MainWin(QWidget):
    def __init__(self):
        ''' вікно, в якому розташовується привітання '''
        super().__init__()

        self.initUI()
        self.set_appear()
        self.show()
    
    def on_click(self):
        self.hide()
        self.tw = TestWin()

    def initUI(self):
        ''' створює графічні елементи '''
        self.hello_text = QLabel(txt_hello)
        self.instruction = QLabel(txt_instruction)
        self.button = QPushButton(txt_next)
        
        self.layout = QVBoxLayout()

        self.layout.addWidget(self.hello_text)
        self.layout.addWidget(self.instruction)
        self.layout.addWidget(self.button)
        self.setLayout(self.layout)
        
        self.button.clicked.connect(self.on_click)
        
        
    

    def set_appear(self):
        ''' встановлює, як виглядатиме вікно (напис, розмір, місце) '''
        self.setWindowTitle(txt_title)
        
        self.setGeometry(win_x, win_y, win_width, win_height)
        
        # TODO вствановити розмір вікна в pyqt
        # TODO вствановити місце де вікно зявлятиметься в pyqt



app = QApplication([])
mw = MainWin()
app.exec_()
