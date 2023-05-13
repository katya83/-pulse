from PyQt5.QtCore import QApplication, QWidget, QLabel, QPushButton, QBoxLayout,
class final_win(QWidget)
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
        self.text_one =QLabel
        self.text_two =QLabel

        self.line_y = QBoxLayout()

        self.line_y_addWidget(self.text_one)
        self.line_y_addWidget(self.text_two)

        self.setLayout(self.line_y)
       

app = QApplication([])
fw = final_win()
app.exec_()
        
