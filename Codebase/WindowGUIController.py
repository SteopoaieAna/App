import sys
from PyQt5 import QtWidgets, uic

from Codebase.GUI.MainWindow import Ui_MainWindow
from Codebase.GUI_design.StyleSheet import MAIN_WINDOW_STYLESHEET

from Codebase.functions.Variables import PLOTTER_BACKGROUND


class WindowGUIControllerClass(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(WindowGUIControllerClass, self).__init__()
        self.setupUi(self)
        self.initPlotters()
        self.connect_main_buttons()


    def initPlotters(self):
        self.plot1.setBackground(PLOTTER_BACKGROUND)
        self.plot2.setBackground(PLOTTER_BACKGROUND)
        self.plot3.setBackground(PLOTTER_BACKGROUND)
        self.plot4.setBackground(PLOTTER_BACKGROUND)

        self.plot1.showGrid(x=True, y=True)
        self.plot2.showGrid(x=True, y=True)
        self.plot3.showGrid(x=True, y=True)
        self.plot4.showGrid(x=True, y=True)

    def connect_main_buttons(self):
        self.connectbutton_Plotting()
        self.connectbutton_Home()
        self.connectbutton_Results()

    def connectbutton_Home(self):
        self.button_Home.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))

    def connectbutton_Plotting(self):
        self.button_Plotting.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))

    def connectbutton_Results(self):
        self.button_Results.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(2))


    def showMainWindow(self):
        self.show()

    def gotoPlottingPage(self):
        self.stackedWidget.setCurrentIndex(2)

    def getText(self):
        text=self.comboBox.currentText()
        self.textEdit.setText(text)

    def retriveText(self):
        words=self.plainTextEdit_2.toPlainText()
        self.textEdit.setText(words)