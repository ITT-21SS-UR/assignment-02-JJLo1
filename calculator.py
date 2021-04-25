# your implementation here
import sys
from PyQt5 import uic, QtWidgets, QtCore, Qt


class IttCalculator(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.ui = uic.loadUi("calculator.ui", self)
        self.show()


def main():
    app = QtWidgets.QApplication(sys.argv)
    calculator = IttCalculator()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
