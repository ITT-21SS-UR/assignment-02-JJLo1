# your implementation here
import sys
from PyQt5 import uic, QtWidgets, QtCore



def input_logging_decorator(function):
    def wrapper(*args, **kwargs):
        print('New input via {}: {}'.format(function.__name__, args[1]))
        return function(*args, **kwargs)

    return wrapper


class IttCalculator(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi("calculator.ui", self)
        self.equationText = ""
        self.equationLabel = self.ui.EquationLabel
        self.resultText = ""
        self.resultLabel = self.ui.ResultLabel
        self.init_buttons()
        self.show()

    def add_to_expression(self, new_input):
        self.equationText += new_input
        self.equationLabel.setText(self.equationText)

    def execute_command(self, command):
        if command == "enter":
            self.resultText = self.calculate_result()
            self.resultLabel.setText(self.resultText)
        elif command == "clear":
            self.equationText = ""
            self.equationLabel.setText(self.equationText)
        elif command == "backspace":
            self.equationText = self.equationText[:-1]
            self.equationLabel.setText(self.equationText)

    def calculate_result(self):
        try:
            result = str(eval(self.equationText))
            return result
        except:
            return "Err"

    @input_logging_decorator
    def keyboard_input_command(self, new_input):
        self.execute_command(new_input)

    @input_logging_decorator
    def mouse_input_command(self, button):
        self.execute_command(button)

    @input_logging_decorator
    def keyboard_input_number_or_operator(self, new_input):
        self.add_to_expression(new_input)

    @input_logging_decorator
    def mouse_input_number_or_operator(self, button):
        self.add_to_expression(button)

    def init_buttons(self):
        self.ui.NumButton_1.clicked.connect(lambda x: self.mouse_input_number_or_operator("1"))
        self.ui.NumButton_2.clicked.connect(lambda x: self.mouse_input_number_or_operator("2"))
        self.ui.NumButton_3.clicked.connect(lambda x: self.mouse_input_number_or_operator("3"))
        self.ui.NumButton_4.clicked.connect(lambda x: self.mouse_input_number_or_operator("4"))
        self.ui.NumButton_5.clicked.connect(lambda x: self.mouse_input_number_or_operator("5"))
        self.ui.NumButton_6.clicked.connect(lambda x: self.mouse_input_number_or_operator("6"))
        self.ui.NumButton_7.clicked.connect(lambda x: self.mouse_input_number_or_operator("7"))
        self.ui.NumButton_8.clicked.connect(lambda x: self.mouse_input_number_or_operator("8"))
        self.ui.NumButton_9.clicked.connect(lambda x: self.mouse_input_number_or_operator("9"))
        self.ui.NumButton_0.clicked.connect(lambda x: self.mouse_input_number_or_operator("0"))
        self.ui.NumButton_DecPoint.clicked.connect(lambda x: self.mouse_input_number_or_operator("."))
        self.ui.NumButton_Divide.clicked.connect(lambda x: self.mouse_input_number_or_operator("/"))
        self.ui.NumButton_Multiply.clicked.connect(lambda x: self.mouse_input_number_or_operator("*"))
        self.ui.NumButton_Add.clicked.connect(lambda x: self.mouse_input_number_or_operator("+"))
        self.ui.NumButton_Subtract.clicked.connect(lambda x: self.mouse_input_number_or_operator("-"))
        self.ui.NumButton_Clear.clicked.connect(lambda x: self.mouse_input_command("clear"))
        self.ui.NumButton_Delete.clicked.connect(lambda x: self.mouse_input_command("backspace"))
        self.ui.NumButton_Enter.clicked.connect(lambda x: self.mouse_input_command("enter"))

    def keyPressEvent(self, event):
        allowed_numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
        allowed_operators = ["/", "*", "+", "-"]

        if event.text() in allowed_numbers:
            self.keyboard_input_number_or_operator(event.text())
        elif event.text() in allowed_operators:
            self.keyboard_input_number_or_operator(event.text())
        elif event.key() == QtCore.Qt.Key_Enter or event.key() == QtCore.Qt.Key_Return:
            self.keyboard_input_command("enter")
        elif event.key() == QtCore.Qt.Key_Backspace:
            self.keyboard_input_command("backspace")
        elif event.text() == "." or event.text() == ",":
            self.keyboard_input_number_or_operator(".")


def main():
    app = QtWidgets.QApplication(sys.argv)
    calculator = IttCalculator()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
