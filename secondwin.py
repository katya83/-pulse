from PyQt5.QtCore import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout,QHBoxLayout,QGroupBox,QRadioButton,QListWidget,QLineEdit
class SecondWin(QWidget)
    def __init__(self):
        super(). __init__()
        self set_appear()
        self initUI()
        self connects()
        self.show()

    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width,win_height)
        self.move(win_x,win_y)

    def initUI(self):
        self.h_line = QHBoxLayout()
        self.r_line = QVBoxLayout()
        self.l_line = QVBoxLayout()
        self.h_line.addLayout(self.l_line)
        self.h_line.addLayout(self.r_line)
        self.setLayout(self.h_line)

        self.fio = QLabel()
        self.let = QLabel()

        self.instructions = QLabel()
        self.instructions1 = QLabel()
        self.instructions2 = QLabel()
        self.timer = QLabel()

        self.button1 = QPushButton()
        self.button2= QPushButton()
        self.button3= QPushButton()
        self.send_button = QPushButton(txt_sendresults)

        self.pole = QLineEdit()
        self.pole1 = QLineEdit()
        self.pole2 = QLineEdit()
        self.pole3 = QLineEdit()
        self.pole4 = QLineEdit()

        self.l_line.addWidget(self.fio)
        self.l_line.addWidget(self.pole)

        self.l_line.addWidget(self.let)
        self.l_line.addWidget(self.pole)

        self.l_line.addWidget(self.instructions)
        self.l_line.addWidget(self.button)

        self.r_line.addWidget(self.timer)

        self.l_line.addWidget(self.fio)

    def connects(self):
        self.send_button.clicked.connect(self.next_click)


    def next_click(self):
        self.hide()
        self.fw = final_win()

app = QApplication([])
sw = second_win()
app.exec_()
        
