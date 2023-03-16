import os

from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *


class GuiTest(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()
        self.widget = QLabel("Working!")
        self.layout.addWidget(self.widget)
        self.setLayout(self.layout)


if __name__ == "__main__":
    app = QApplication([])
    gui = GuiTest()
    gui.show()
    app.exec_()
