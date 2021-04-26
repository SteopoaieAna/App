
from PyQt5 import QtWidgets, QtGui
import sys
from PyQt5.QtWidgets import QApplication,QDialog
from PyQt5.uic import loadUi

from Codebase.GUI.MainWindow import Ui_MainWindow
from Codebase.MainApp.MainAppController import MainApp
from Codebase.WindowGUIController import WindowGUIControllerClass

''''''''''''''''

def controlish(self):
 controller=Controller(self)
'''''''''''''''''

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window=MainApp()
    window.showMainWindow()
    app.exec()