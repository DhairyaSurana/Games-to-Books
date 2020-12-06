# This Python file uses the following encoding: utf-8

import sys

from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QComboBox
from PyQt5.QtCore import QFile

from scraper import *


class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        uic.loadUi('form.ui', self) # Load the .ui file
        self.show() # Show the GUI

        # dropdown = self.findChild(QtWidgets.QComboBox, "games_dropdown")
        # dropdown.addItem("Witcher 3")
        # dropdown.addItem("Skyrim")
        # dropdown.addItem("Witcher 1")
        # dropdown.addItem("Witcher 2")

        self.searchbox = self.findChild(QtWidgets.QLineEdit, "searchbox")
        self.searchbutton = self.findChild(QtWidgets.QPushButton, "searchbutton")
        self.game_list = self.findChild(QtWidgets.QTextEdit, "game_list")
        self.game_list.setReadOnly(True)

        self.searchbutton.clicked.connect(self.searchButtonEvent)

    def searchButtonEvent(self):
        
        text = self.searchbox.displayText()

        if text:
            print(text)
            self.searchbox.clear()

        books = getBooks(text)

        for items in books:
            for i in items:
                self.game_list.append(i)




if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    widget = Window()
    widget.show()
    sys.exit(app.exec_())