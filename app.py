from gui_windows.welcome_window import Ui_welcome_window
from PySide2 import QtCore, QtGui, QtWidgets
from orm import db_manager

class WelcomeWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_welcome_window()
        self.ui.setupUi(self)
        self._connect()

    def _connect(self):
        self.ui.add_company_btn.clicked.connect(self.add_company)
        self.ui.start_btn(self.start)
        ...

    def add_company(self):
        self.refresh_companies_box()
        ...

    def start(self):
        ...

    def refresh_companies_box(self):
        self.ui.company_combo_box.clear()
        items = db_manager.get_companies_names()
        self.ui.company_combo_box.addItems(items)







