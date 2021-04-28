import sys
from PyQt5 import uic, QtWidgets, QtCore


# decorator for logging all inputs
def input_logging_decorator(function):
    def wrapper(*args, **kwargs):
        print('New input via {}: {}'.format(function.__name__, args[1]))
        return function(*args, **kwargs)
    return wrapper


class IttCalculator(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.__ui = uic.loadUi("calculator.ui", self)
        self.__equation_text = ""
        self.__equation_label = self.__ui.EquationLabel
        self.__result_text = ""
        self.__result_label = self.__ui.ResultLabel
        self.__allowed_numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
        self.__allowed_operators = ["/", "*", "+", "-"]
        self.__init_buttons()
        self.show()

    # add a new input to our equation and equation-label
    def __add_to_equation(self, new_input):
        self.__equation_text += new_input
        self.__equation_label.setText(self.__equation_text)

    # execute an input command
    def __execute_command(self, command):
        if command == "enter":
            self.__result_text = self.__calculate_result()
            self.__result_label.setText(self.__result_text)
        elif command == "clear":
            self.__equation_text = ""
            self.__equation_label.setText(self.__equation_text)
        elif command == "backspace":
            self.__equation_text = self.__equation_text[:-1]
            self.__equation_label.setText(self.__equation_text)

    # calculates and returns the result of the equation by using the eval() function,
    # returns "Err" string if the equation cant be solved
    def __calculate_result(self):
        try:
            result = str(eval(self.__equation_text))
            return result
        except:
            return "Err"

    # sends a new keyboard "command" input (enter, clear or backspace) to the log (through the decorator)
    # and to the executes_command() function
    @input_logging_decorator
    def __keyboard_input_command(self, new_input):
        self.__execute_command(new_input)

    # sends a new mouse "command" input (enter, clear or backspace) to the log (through the decorator)
    # and to the execute_command() function
    @input_logging_decorator
    def __mouse_input_command(self, button):
        self.__execute_command(button)

    # sends a new keyboard "number or operator" input to the log (through the decorator)
    # and to the add_to_equation() function
    @input_logging_decorator
    def __keyboard_input_number_or_operator(self, new_input):
        self.__add_to_equation(new_input)

    # sends a new mouse "number or operator" input to the log (through the decorator)
    # and to the add_to_equation() function
    @input_logging_decorator
    def __mouse_input_number_or_operator(self, button):
        self.__add_to_equation(button)

    # initializes all UI buttons
    def __init_buttons(self):
        self.__ui.NumButton_1.clicked.connect(lambda x: self.__mouse_input_number_or_operator("1"))
        self.__ui.NumButton_2.clicked.connect(lambda x: self.__mouse_input_number_or_operator("2"))
        self.__ui.NumButton_3.clicked.connect(lambda x: self.__mouse_input_number_or_operator("3"))
        self.__ui.NumButton_4.clicked.connect(lambda x: self.__mouse_input_number_or_operator("4"))
        self.__ui.NumButton_5.clicked.connect(lambda x: self.__mouse_input_number_or_operator("5"))
        self.__ui.NumButton_6.clicked.connect(lambda x: self.__mouse_input_number_or_operator("6"))
        self.__ui.NumButton_7.clicked.connect(lambda x: self.__mouse_input_number_or_operator("7"))
        self.__ui.NumButton_8.clicked.connect(lambda x: self.__mouse_input_number_or_operator("8"))
        self.__ui.NumButton_9.clicked.connect(lambda x: self.__mouse_input_number_or_operator("9"))
        self.__ui.NumButton_0.clicked.connect(lambda x: self.__mouse_input_number_or_operator("0"))
        self.__ui.NumButton_DecPoint.clicked.connect(lambda x: self.__mouse_input_number_or_operator("."))
        self.__ui.NumButton_Divide.clicked.connect(lambda x: self.__mouse_input_number_or_operator("/"))
        self.__ui.NumButton_Multiply.clicked.connect(lambda x: self.__mouse_input_number_or_operator("*"))
        self.__ui.NumButton_Add.clicked.connect(lambda x: self.__mouse_input_number_or_operator("+"))
        self.__ui.NumButton_Subtract.clicked.connect(lambda x: self.__mouse_input_number_or_operator("-"))
        self.__ui.NumButton_Clear.clicked.connect(lambda x: self.__mouse_input_command("clear"))
        self.__ui.NumButton_Delete.clicked.connect(lambda x: self.__mouse_input_command("backspace"))
        self.__ui.NumButton_Enter.clicked.connect(lambda x: self.__mouse_input_command("enter"))

    # registers all relevant key press events
    def keyPressEvent(self, event):
        if event.text() in self.__allowed_numbers:
            self.__keyboard_input_number_or_operator(event.text())
        elif event.text() in self.__allowed_operators:
            self.__keyboard_input_number_or_operator(event.text())
        elif event.key() == QtCore.Qt.Key_Enter or event.key() == QtCore.Qt.Key_Return:
            self.__keyboard_input_command("enter")
        elif event.key() == QtCore.Qt.Key_Backspace:
            self.__keyboard_input_command("backspace")
        elif event.text() == "." or event.text() == ",":
            self.__keyboard_input_number_or_operator(".")


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    calculator = IttCalculator()
    sys.exit(app.exec_())
