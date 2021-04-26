import os

from Codebase.WindowGUIController import WindowGUIControllerClass


class MainApp:
    def __init__(self):
        self._WinGUI=WindowGUIControllerClass()

    def showMainWindow(self):
        self._WinGUI.showMainWindow()


