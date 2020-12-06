# This Python file uses the following encoding: utf-8

import sys

from PyQt5 import QtWidgets, QtGui, uic
from PyQt5.QtWidgets import QComboBox
from PyQt5.QtCore import QFile

from scraper import *
import webbrowser


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
        self.book_list = self.findChild(QtWidgets.QListWidget, "game_list")

        self.book_list.clicked.connect(self.book_clicked)
        self.searchbutton.clicked.connect(self.searchButtonEvent)

    def searchButtonEvent(self):
        
        text = self.searchbox.displayText()

        if text:
            self.searchbox.clear()
            self.book_list.addItem(text)
 
            books = getBooks(text)

            for items in books:
                for i in items:
                    self.book_list.addItem(i)

    def book_clicked(self):
        item = self.book_list.currentItem()
        webbrowser.open("https://www.amazon.com/s?k=" + item.text())

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    widget = Window()
    widget.show()
    sys.exit(app.exec_())