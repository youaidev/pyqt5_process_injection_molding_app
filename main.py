""" Mudules """
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys


# app
app = QApplication(sys.argv)

# window
window = QWidget()
window.setWindowTitle("Process Notes")
window.show()

# exit app
app.exec()
