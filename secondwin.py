from PyQt5.QtCore import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout,QHBoxLayout,QGroupBox,QRadioButton,QListWidget,QLineEdit
class Experiment():
    def __init__(self, age,  test1, test2, test3):
        self.age = age
        self.t1 = test1
        self.t2 = test2
        self.t3 = test3 

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
        
      def next_click(self):
        self.hide
        self.exp = Experiment(int(self.line_age.text()), self.line_text1.text(), self.line_text2.text(),self.line_text3.text())
        self.fw = final_win(self.exp)
    
    def timer_test(self):
        global time
        time = QTime(0, 0, 15)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer1Event)
        self.timer.start(1500)

    def timer_sits(self):
        global time
        time = QTime(0, 0, 30)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer2Event)
        self.timer.start(1500)

    def timer_final(self):
        global time
        time = QTime(0, 1, 0)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer3Event)
        self.timer.start(1500)

    def timer1Event(self):
        global time
        time = time.addSecs(-1)
        self.text_timer.setText(time.toString("hh:mm:ss"))
        self.text_timer.setFont(QFont("Times", 36, QFont.Bold))
        self.text_timer.setStyleSheet("color: rgb(0,0,0)")
        if time.toString("hh:mm:ss" ) == "00:00:00":
            self.timer.stop()

    def timer2Event(self):
        global time
        time = time.addSecs(-1)
        self.text_timer.setText(time.toString("hh:mm:ss") [6:8])
        self.text_timer.setFont(QFont("Times", 36, QFont.Bold))
        self.text_timer.setStyleSheet("color: rgb(0,0,0)")
        if time.toString("hh:mm:ss" ) == "00:00:00":
            self.timer.stop()

    def timer3Event(self):
        global time
        time = time.addSecs(-1)
        self.text_timer.setText(time.toString("hh:mm:ss"))
        if int(time.toString("hh:mm:ss" ) [6:8]) >= 45:
            self.text_timer.setStyleSheet("color: rgb(0,255,0)")
        elif int(time.toString("hh:mm:ss" ) [6:8]) <= 15:
            self.text_timer.setStyleSheet("color: rgb(0,255,0)")
        else:
            self.text_timer.setStyleSheet("color: rgb(0,0,0)")
        self.text_timer.setFont(QFont("Times", 36, QFont.Bold))
        if time.toString("hh:mm:ss" ) == "00:00:00":
            self.timer.stop()

    def connects(self):
        self.button_next.clicked.connect(self.next_click)
        self.button_test1.clicked.connect(self.timer_test)
        self.button_test2.clicked.connect(self.timer_sits)
        self.button_test3.clicked.connect(self.timer_final)

    def connects(self):
        self.send_button.clicked.connect(self.next_click)


    def next_click(self):
        self.hide()
        self.fw = final_win()

app = QApplication([])
sw = second_win()
app.exec_()
        
