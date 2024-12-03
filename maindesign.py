import sys

from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtWidgets import QApplication, QPushButton
from PyQt6 import QtCore, QtGui, QtWidgets


class Design(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def setupUi(self, Circles):
        self.resize(400, 300)
        self.btn = QPushButton(self)
        self.btn.setGeometry(150, 260, 100, 30)
        self.btn.setText("click^^")