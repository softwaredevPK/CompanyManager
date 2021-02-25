from .gui_windows.welcome_window import Ui_welcome_window
from PySide2 import QtCore, QtGui, QtWidgets


class WelcomeWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_welcome_window()
        self.ui.setupUi()
        self._connect()

    def _connect(self):
        ...








