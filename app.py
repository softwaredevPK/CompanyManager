from gui_windows.welcome_window import Ui_welcome_window
from gui_windows.AddContractorWidget import Ui_add_contractor_QWidget
from PySide2 import QtCore, QtGui, QtWidgets
from orm import db_manager, Customer
from functools import partial

# TODO possibility to add Company only if DB is empty! Wanna to show button to add it only for empty db
class WelcomeWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_welcome_window()
        self.ui.setupUi(self)
        self.add_contractor = AddCustomer()
        self._connect()

    def _connect(self):
        self.ui.add_company_B.clicked.connect(self.add_company)
        self.ui.start_B.clicked.connect(self.start)

    def add_company(self):
        self.add_contractor.exec_()
        self.refresh_companies_box()

    def start(self):
        ...

    def refresh_companies_box(self):
        self.ui.company_IW.clear()
        items = db_manager.get_companies_names()
        self.ui.company_IW.addItems(items)


class AddCustomer(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_add_contractor_QWidget()
        self.ui.setupUi(self)

        # Default window should be opened for Company
        self.ui.data_person_CT.setVisible(False)
        self.ui.company_B.setChecked(True)

        self.set_connections()

    @property
    def req_fields(self):
        return [self.ui.country_IW] + self.ui.data_company_CT.findChildren(QtWidgets.QLineEdit) + self.ui.data_person_CT.findChildren(QtWidgets.QLineEdit)

    @property
    def company_req_fields(self):
        return [self.ui.country_IW] + self.ui.data_company_CT.findChildren(QtWidgets.QLineEdit)

    @property
    def person_req_fields(self):
        return self.ui.data_person_CT.findChildren(QtWidgets.QLineEdit)

    @property
    def all_qlineedits(self):
        return self.ui.data_company_CT.findChildren(QtWidgets.QLineEdit) + self.ui.data_person_CT.findChildren(QtWidgets.QLineEdit) + self.ui.additional_data_CT.findChildren(QtWidgets.QLineEdit)

    @staticmethod
    def change_border_to_red(*args):
        """
        :param args: It req Qobject, but during connections some extra args might be passed
        """
        for arg in args:
            if hasattr(arg, 'setStyleSheet'):
                arg.setStyleSheet("border: 1px solid red")

    @staticmethod
    def change_border_to_black(*args):
        """
        :param args: It req Qobject, but during connections some extra args might be passed
        """
        for arg in args:
            if hasattr(arg, 'setStyleSheet'):
                arg.setStyleSheet("border: 1px solid black")

    def set_connections(self):
        self.ui.company_B.toggled.connect(self.to_company)
        self.ui.person_B.toggled.connect(self.to_person)

        self.ui.country_IW.addItems(db_manager.get_countries_names())
        self.ui.country_IW.setPlaceholderText('--Select Country--')
        self.ui.country_IW.setCurrentIndex(-1)
        self.ui.country_IW.currentTextChanged.connect(self.fill_country_tin)

        self.ui.clear_B.clicked.connect(self.clear)
        self.ui.add_B.clicked.connect(self.add)

        # changing borders to black each time when user changes text for req_fields(can't use property bc need to
        for field in self.req_fields:

            if hasattr(field, 'currentTextChanged'):
                field.currentTextChanged.connect(partial(self.change_border_to_black, field))
            elif hasattr(field, 'textChanged'):
                field.textChanged.connect(partial(self.change_border_to_black, field))

    def fill_country_tin(self, country):
        """Method for clear button to being run when is clicked"""
        if country == '':   # when setting back to default
            code = ''
        else:
            code = db_manager.get_country_code(country)
        self.ui.tin_country_IW.setText(code)

    def req_fields_filled(self):
        """Method checks if all necessary fields are filled, and change its border to red if sth is missing
        :return True if all checks are positive, otherwise return False
        """
        incorrect = False
        if self.ui.company_B.isChecked():
            fields_to_check = self.company_req_fields
        elif self.ui.person_B.isChecked():
            fields_to_check = self.person_req_fields

        for field in fields_to_check:
            if hasattr(field, 'currentText'):
                if field.currentText() == '--Select Country--':
                    self.change_border_to_red(field)
                    incorrect = True
            elif hasattr(field, 'text'):
                if field.text() == '':
                    self.change_border_to_red(field)
                    incorrect = True

        if incorrect:
            return False
        else:
            return True

    def to_person(self):
        """Method for person button to being run when is toggled"""
        self.ui.data_person_CT.setVisible(True)
        self.ui.data_company_CT.setVisible(False)

    def to_company(self):
        """Method for company button to being run when is toggled"""
        self.ui.data_person_CT.setVisible(False)
        self.ui.data_company_CT.setVisible(True)

    def clear(self):
        """Method for clear button to being run when is clicked"""
        for line_edit in self.all_qlineedits:
            line_edit.setText('')
        self.ui.country_IW.setCurrentIndex(-1)

    def add(self):
        """Method for add button to being run when is clicked"""
        if self.req_fields_filled():
            if self.ui.company_B.isChecked():
                record = Customer(full_name=self.ui.long_name_IW.text(),
                                  name=self.ui.short_name_IW.text(),
                                  address=self.ui.address_IW.text(),
                                  country=self.ui.country_IW.currentText(),
                                  tin_code=self.ui.tin_IW.text(),
                                  zip_code=self.ui.zipe_code_IW.text(),
                                  city=self.ui.town_IW.text(),
                                  email=self.ui.email_IW.text(),
                                  phone_number=self.ui.phone_number_IW.text())
            elif self.ui.person_B.isChecked():
                record = Customer(name=self.ui.first_name_IW.text() + self.ui.surname_IW.text(),
                                  full_name=self.ui.first_name_IW.text() + self.ui.second_name_IW.text() + self.ui.surname_IW.text(),
                                  address=self.ui.address_IW.text(),
                                  zip_code=self.ui.zipe_code_IW.text(),
                                  city=self.ui.town_IW.text(),
                                  email=self.ui.email_IW.text(),
                                  phone_number=self.ui.phone_number_IW.text())
            db_manager.session.add(record)
            db_manager.session.commit()
            # todo create contextmanager to deal with roll_back and commit
            self.clear()   # at the end it should clear all field




