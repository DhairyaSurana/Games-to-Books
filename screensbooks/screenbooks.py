# This Python file uses the following encoding: utf-8
import sys
import os
import webbrowser



from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QComboBox
from PyQt5.QtCore import QFile


class bookreccomendations(QtWidgets.QMainWindow):
    def __init__(self):
        super(bookreccomendations, self).__init__()
        uic.loadUi("screenbooks.ui", self)
        self.show
        self.backbutton.clicked.connect(self.backButtonEvent)
        self.Lord.clicked.connect(self.Lordevent)
        self.Alice.clicked.connect(self.Alicevent)
        self.Withcher.clicked.connect(self.Witcherevent)
        # self.ListofBooks.clicked.connect(self.OpenLink)
        # self.ListofBooks.itemClicked.connect(self.OpenLink)
        # self.ListofBooks.cellClicked.connect(self.listwidgetclicked)
        # self.layout.ListofBooks.addWidget(self.listWidget)
        # self.layout.addWidget(self)       #.listWidget)
# I COULD NOT GET THE BELOW STUFF TO WORK AT ALL

    # def listwidgetclicked(self, item):
    #     print('!!! cick {0}'.format(item.text()))

    # def OpenLink(self):
    #     print("wow")
    #     if item.column() == 1:
    #         print("so close")
    #         webbrowser.open('www.google.com')
    def Lordevent(self):
        # print("let's do website")
        webbrowser.open('https://www.amazon.com/Hobbit-Lord-Rings-Fellowship-Towers/dp/0345538374/ref=sr_1_3?crid=28H8XJFQA451H&dchild=1&keywords=lord+of+the+rings+books&qid=1607281981&sprefix=lord%2Caps%2C195&sr=8-3')
    def Alicevent(self):
        webbrowser.open('https://www.amazon.com/Alices-Adventures-Wonderland-Lewis-Carroll/dp/B08JJKG6XV/ref=sr_1_1_sspa?crid=26OB50V6AFT5U&dchild=1&keywords=alice+in+wonderland+book&qid=1607282075&sprefix=alice+i%2Caps%2C208&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUFKSjdEOURPUldGU1EmZW5jcnlwdGVkSWQ9QTAyMzk2NzYyWFdLVU1HTlgzVDFVJmVuY3J5cHRlZEFkSWQ9QTA0MzU3NzlJRjI5RFM5V0pOTzcmd2lkZ2V0TmFtZT1zcF9hdGYmYWN0aW9uPWNsaWNrUmVkaXJlY3QmZG9Ob3RMb2dDbGljaz10cnVl')
    def Witcherevent(self):
        webbrowser.open('https://www.amazon.com/Witcher-Boxed-Set-Contempt-Baptism/dp/0316438979/ref=sr_1_3?crid=1OA098NOMCEF9&dchild=1&keywords=witcher+books&qid=1607282118&sprefix=wticher+boo%2Caps%2C173&sr=8-3')
    def backButtonEvent(self):
        print("backbuttonclick")
        # self.load_ui()
    

    # def load_ui(self):
    #     loader = QUiLoader()
    #     path = os.path.join(os.path.dirname(__file__), "form.ui")
    #     ui_file = QFile(path)
    #     ui_file.open(QFile.ReadOnly)
    #     loader.load(ui_file, self)
    #     ui_file.close()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    widget = bookreccomendations()
    widget.show()
    sys.exit(app.exec_())
