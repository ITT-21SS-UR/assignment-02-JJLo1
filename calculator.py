# your implementation here
import sys
from PyQt5 import uic, QtWidgets, QtCore


def input_logging_decorator(function):
    def wrapper(*args, **kwargs):
        print('New input via {}: {}'.format(function.__name__, args[1]))
        return function

    return wrapper


class IttCalculator(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi("calculator.ui", self)
        self.new_input = None
        self.init_buttons()
        self.show()


    def add_input(self, new_input):
        self.new_input = new_input

    @input_logging_decorator
    def keyboard_input(self, new_input):
        self.add_input(new_input)

    @input_logging_decorator
    def mouse_input(self, button):
        if button == "1":
            self.add_input(self, 1)

    def init_buttons(self):
        self.ui.NumButton_1.clicked.connect(lambda x: self.mouse_input("1"))
        self.ui.NumButton_2.clicked.connect(lambda x: self.mouse_input("2"))
        self.ui.NumButton_3.clicked.connect(lambda x: self.mouse_input("3"))
        self.ui.NumButton_4.clicked.connect(lambda x: self.mouse_input("4"))
        self.ui.NumButton_5.clicked.connect(lambda x: self.mouse_input("5"))
        self.ui.NumButton_6.clicked.connect(lambda x: self.mouse_input("6"))
        self.ui.NumButton_7.clicked.connect(lambda x: self.mouse_input("7"))
        self.ui.NumButton_8.clicked.connect(lambda x: self.mouse_input("8"))
        self.ui.NumButton_9.clicked.connect(lambda x: self.mouse_input("9"))
        self.ui.NumButton_0.clicked.connect(lambda x: self.mouse_input("0"))
        self.ui.NumButton_DecPoint.clicked.connect(lambda x: self.mouse_input("."))
        self.ui.NumButton_Clear.clicked.connect(lambda x: self.mouse_input("clear"))
        self.ui.NumButton_Delete.clicked.connect(lambda x: self.mouse_input("backspace"))
        self.ui.NumButton_Enter.clicked.connect(lambda x: self.mouse_input("enter"))
        self.ui.NumButton_Divide.clicked.connect(lambda x: self.mouse_input("/"))
        self.ui.NumButton_Multiply.clicked.connect(lambda x: self.mouse_input("*"))
        self.ui.NumButton_Add.clicked.connect(lambda x: self.mouse_input("+"))
        self.ui.NumButton_Subtract.clicked.connect(lambda x: self.mouse_input("-"))

    def keyPressEvent(self, event):
        if event.text() == "1":
            self.keyboard_input("1")
        elif event.text() == "2":
            self.keyboard_input("2")
        elif event.text() == "3":
            self.keyboard_input("3")
        elif event.text() == "4":
            self.keyboard_input("4")
        elif event.text() == "5":
            self.keyboard_input("5")
        elif event.text() == "6":
            self.keyboard_input("6")
        elif event.text() == "7":
            self.keyboard_input("7")
        elif event.text() == "8":
            self.keyboard_input("8")
        elif event.text() == "9":
            self.keyboard_input("9")
        elif event.text() == "0":
            self.keyboard_input("0")
        elif event.text() == "/":
            self.keyboard_input("/")
        elif event.text() == "*":
            self.keyboard_input("*")
        elif event.text() == "+":
            self.keyboard_input("+")
        elif event.text() == "-":
            self.keyboard_input("-")
        elif event.key() == QtCore.Qt.Key_Enter or event.key() == QtCore.Qt.Key_Return:
            self.keyboard_input("enter")
        elif event.key() == QtCore.Qt.Key_Backspace:
            self.keyboard_input("backspace")
        elif event.text() == "." or event.text() == ",":
            self.keyboard_input(".")




def main():
    app = QtWidgets.QApplication(sys.argv)
    calculator = IttCalculator()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
