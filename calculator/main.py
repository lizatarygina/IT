from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QLabel, QPushButton
import sys

calc = 0
pr = 0
a = ''


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.btnr = QPushButton(self)
        self.btns = QPushButton(self)
        self.btny = QPushButton(self)
        self.btnd = QPushButton(self)
        self.btn0 = QPushButton(self)
        self.btn9 = QPushButton(self)
        self.btn8 = QPushButton(self)
        self.btn7 = QPushButton(self)
        self.btn6 = QPushButton(self)
        self.btn5 = QPushButton(self)
        self.btn4 = QPushButton(self)
        self.btn3 = QPushButton(self)
        self.btn2 = QPushButton(self)
        self.btn1 = QPushButton(self)
        self.btn = QPushButton(self)
        self.lbl = QLabel(self)
        self.le = QLineEdit(self)
        self.set_ui()

    def set_ui(self):
        self.setGeometry(200, 200, 210, 250)
        self.setWindowTitle('Window')
        self.le.setGeometry(30, 70, 120, 30)

        self.btn.setGeometry(150, 70, 30, 150)
        self.btn.setText('=')
        self.btn.clicked.connect(self.equal_click_event)

        self.btn1.setGeometry(30, 100, 30, 30)
        self.btn1.setText('1')
        self.btn1.clicked.connect(self.click_event_1)

        self.btn2.setGeometry(60, 100, 30, 30)
        self.btn2.setText('2')
        self.btn2.clicked.connect(self.click_event_2)

        self.btn3.setGeometry(90, 100, 30, 30)
        self.btn3.setText('3')
        self.btn3.clicked.connect(self.click_event_3)

        self.btn4.setGeometry(30, 130, 30, 30)
        self.btn4.setText('4')
        self.btn4.clicked.connect(self.click_event_4)

        self.btn5.setGeometry(60, 130, 30, 30)
        self.btn5.setText('5')
        self.btn5.clicked.connect(self.click_event_5)

        self.btn6.setGeometry(90, 130, 30, 30)
        self.btn6.setText('6')
        self.btn6.clicked.connect(self.click_event_6)

        self.btn7.setGeometry(30, 160, 30, 30)
        self.btn7.setText('7')
        self.btn7.clicked.connect(self.click_event_7)

        self.btn8.setGeometry(60, 160, 30, 30)
        self.btn8.setText('8')
        self.btn8.clicked.connect(self.click_event_8)

        self.btn9.setGeometry(90, 160, 30, 30)
        self.btn9.setText('9')
        self.btn9.clicked.connect(self.click_event_9)

        self.btn0.setGeometry(60, 190, 30, 30)
        self.btn0.setText('0')
        self.btn0.clicked.connect(self.click_event_0)

        self.btns.setGeometry(120, 100, 30, 60)
        self.btns.setText('+')
        self.btns.clicked.connect(self.click_event_s)

        self.btnr.setGeometry(120, 160, 30, 60)
        self.btnr.setText('-')
        self.btnr.clicked.connect(self.click_event_r)

        self.btny.setGeometry(30, 190, 30, 30)
        self.btny.setText('*')
        self.btny.clicked.connect(self.click_event_y)

        self.btnd.setGeometry(90, 190, 30, 30)
        self.btnd.setText('/')
        self.btnd.clicked.connect(self.click_event_d)

        self.show()

    def click_event_1(self):
        global a
        self.le.setText(self.le.text() + '1')
        a = a + '1'

    def click_event_2(self):
        global a
        self.le.setText(self.le.text() + '2')
        a = a + '2'

    def click_event_3(self):
        global a
        self.le.setText(self.le.text() + '3')
        a = a + '3'

    def click_event_4(self):
        global a
        self.le.setText(self.le.text() + '4')
        a = a + '4'

    def click_event_5(self):
        global a
        self.le.setText(self.le.text() + '5')
        a = a + '5'

    def click_event_6(self):
        global a
        self.le.setText(self.le.text() + '6')
        a = a + '6'

    def click_event_7(self):
        global a
        self.le.setText(self.le.text() + '7')
        a = a + '7'

    def click_event_8(self):
        global a
        self.le.setText(self.le.text() + '8')
        a = a + '8'

    def click_event_9(self):
        global a
        self.le.setText(self.le.text() + '9')
        a = a + '9'

    def click_event_0(self):
        global a
        self.le.setText(self.le.text() + '0')
        a = a + '0'

    def click_event_s(self):
        global calc, pr, a
        if pr == 0:
            calc += int(a)
        elif pr == 1:
            calc += int(a)
        elif pr == 2:
            calc -= int(a)
        elif pr == 3:
            calc *= int(a)
        elif pr == 4:
            calc //= int(a)
        self.le.setText(self.le.text() + '+')
        pr = 1
        a = ''

    def click_event_r(self):
        global calc, pr, a
        if pr == 0:
            calc += int(a)
        elif pr == 1:
            calc += int(a)
        elif pr == 2:
            calc -= int(a)
        elif pr == 3:
            calc *= int(a)
        elif pr == 4:
            calc //= int(a)
        self.le.setText(self.le.text() + '-')
        pr = 2
        a = ''

    def click_event_y(self):
        global calc, pr, a
        if pr == 0:
            calc += int(a)
        elif pr == 1:
            calc += int(a)
        elif pr == 2:
            calc -= int(a)
        elif pr == 3:
            calc *= int(a)
        elif pr == 4:
            calc //= int(a)
        self.le.setText(self.le.text() + '*')
        pr = 3
        a = ''

    def click_event_d(self):
        global calc, pr, a
        if pr == 0:
            calc += int(a)
        elif pr == 1:
            calc += int(a)
        elif pr == 2:
            calc -= int(a)
        elif pr == 3:
            calc *= int(a)
        elif pr == 4:
            calc //= int(a)
        self.le.setText(self.le.text() + '/')
        pr = 4
        a = ''

    def equal_click_event(self):
        global calc, pr, a
        if pr == 0:
            calc += int(a)
        elif pr == 1:
            calc += int(a)
        elif pr == 2:
            calc -= int(a)
        elif pr == 3:
            calc *= int(a)
        elif pr == 4:
            calc //= int(a)
        self.le.setText(str(calc))


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = Window()
    sys.exit(app.exec_())
