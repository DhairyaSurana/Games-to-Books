# This Python file uses the following encoding: utf-8

import sys

from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QComboBox
from PyQt5.QtCore import QFile


class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        uic.loadUi('form.ui', self) # Load the .ui file
        self.show() # Show the GUI
        print('test')

        dropdown = self.findChild(QtWidgets.QComboBox, "games_dropdown")
        dropdown.addItem("Witcher 3")
        dropdown.addItem("Skyrim")
        dropdown.addItem("Witcher 1")
        dropdown.addItem("Witcher 2")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    widget = Window()
    widget.show()
    sys.exit(app.exec_())