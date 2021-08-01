__author__ = 'darer49'
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from firstPyQt5 import *

if __name__ == 'main':
    '''main function'''
    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
