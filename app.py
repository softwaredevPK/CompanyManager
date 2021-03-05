from gui_windows.welcome_window import Ui_welcome_window
from gui_windows.AddContractorWidget import Ui_add_contractor_QWidget
from gui_windows.start_window import Ui_StartWindow
from PySide2 import QtCore, QtGui, QtWidgets
from orm import db_manager, Customer, Supplier
from functools import partial
from utilities import show_msg_box


class WelcomeWindow(QtWidgets.QMainWindow):
    """First window that appers after launch of tool(If Company is created)"""

    def __init__(self):
        super().__init__()
        self.ui = Ui_welcome_window()
        self.ui.setupUi(self)
        self._connect()
        self.start_window = StartWindow

    def _connect(self):
        self.ui.edit_B.clicked.connect(self.edit)
        self.ui.start_B.clicked.connect(self.start)

    def check_settings(self):
        """Method used to check if Company Account was created.
         If it return False, then window shouldn't use show method."""
        if not db_manager.is_supplier_created():  # before showing window check if acc is created
            if not self.add_company():  # if user would close window without creating acc do not open window
                return False
            else:
                return True
        else:
            return True

    def add_company(self):
        """Method used to create Company(user) Account"""
        add_company = AddCompany()
        show_msg_box('Please setup your company account')
        if not add_company.exec_():  # if user closes window - meaning resign from creating acc
            return False
        else:
            return True


    def start(self):
        """Method used to start a program"""
        self.start_window = self.start_window()
        self.close()
        self.start_window.show()

    def edit(self):
        """Method used to edit company setting(Record in DB)"""
        company = db_manager.get_company()
        edit_company = EditCompany(company)
        edit_company.exec_()


class StartWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_StartWindow()
        self.ui.setupUi(self)
        self._connect()

    def _connect(self):
        self.ui.add_customer_B.clicked.connect(self.add_customer)
        self.ui.edit_customer_B.clicked.connect(self.edit_customer)
        self.ui.my_procust_B.clicked.connect(self.my_products)

    def edit_customer(self):
        items = db_manager.get_customers_names()
        if len(items) == 0:
            msg_box = QtWidgets.QMessageBox(icon=QtWidgets.QMessageBox.Information, text="There are no customers in your DataBase.")
            msg_box.exec_()
        else:
            text, ok = QtWidgets.QInputDialog.getItem(self, 'Editor', 'Choose customer to edit', items, 0, False)
        if ok:  # not canceled
            db_manager.get_customer()

    def add_customer(self):
        add_cust = AddCustomer()
        add_cust.exec_()

    def my_products(self):
        ...


class AddCustomer(QtWidgets.QDialog):
    """
    Widget used to add new Customers to DB
    """

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
        # phone_no_validator = QtGui.QRegExpValidator("\d+", self.ui.tin_IW)
        self.ui.tin_IW.setValidator(QtGui.QRegExpValidator("[\d[a-zA-Z]+", self.ui.tin_IW))
        # tin_no_validator = QtGui.QRegExpValidator("\d+", self.ui.phone_number_IW)
        self.ui.phone_number_IW.setValidator(QtGui.QRegExpValidator("\d+", self.ui.phone_number_IW))

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
        """Method updates tin_count_IW with country_code"""
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
                                  phone_number=self.ui.phone_number_IW.text(),
                                  is_person=False)
            elif self.ui.person_B.isChecked():
                record = Customer(name=self.ui.first_name_IW.text() + self.ui.surname_IW.text(),
                                  full_name=self.ui.first_name_IW.text() + self.ui.second_name_IW.text() + self.ui.surname_IW.text(),
                                  address=self.ui.address_IW.text(),
                                  zip_code=self.ui.zipe_code_IW.text(),
                                  city=self.ui.town_IW.text(),
                                  email=self.ui.email_IW.text(),
                                  phone_number=self.ui.phone_number_IW.text(),
                                  is_person=True)
            check_res = db_manager.check_customer_constraints(record)
            if check_res:
                show_msg_box(check_res)
            else:
                db_manager.session.add(record)
                db_manager.session.commit()

            self.clear()   # at the end it should clear all field


class EditCustomer(AddCustomer):
    def __init__(self, customer: Customer):
        super().__init__()
        self.customer = customer
        self.ui.add_B.setText("Save")
        self.ui.add_B.clicked.connect(self.update)  # change of method connected to button
        self.write_values()

    def add(self):
        raise Exception("Method not in use")

    def write_values(self):
        """Write values of Customer to appropriate IW"""
        self.ui.long_name_IW.setText(self.customer.full_name)
        self.ui.short_name_IW.setText(self.customer.name)
        self.ui.country_IW.setCurrentText(self.customer.country)
        self.ui.tin_IW.setText(self.customer.tin_code)
        self.ui.address_IW.setText(self.customer.address)
        self.ui.town_IW.setText(self.customer.city)
        self.ui.zipe_code_IW.setText(self.customer.zip_code)
        self.ui.email_IW.setText(self.customer.email)
        self.ui.phone_number_IW.setText(self.customer.phone_number)

    def update(self):
        if self.req_fields_filled():
            if self.ui.company_B.isChecked():
                self.customer.is_person = False
                self.customer.full_name = self.ui.long_name_IW.text()
                self.customer.name = self.ui.short_name_IW.text()
                self.customer.country = self.ui.country_IW.currentText()
                self.customer.tin_code = self.ui.tin_IW.text()
            elif self.ui.person_B.isChecked():
                self.customer.is_person = True
                self.customer.full_name = self.ui.first_name_IW.text() + self.ui.second_name_IW.text() + self.ui.surname_IW.text()
                self.customer.name = self.ui.first_name_IW.text() + self.ui.surname_IW.text()
                self.customer.country = ''
                self.customer.tin_code = ''

            self.customer.address = self.ui.address_IW.text()
            self.customer.city = self.ui.town_IW.text()
            self.customer.zip_code = self.ui.zipe_code_IW.text()
            self.customer.email = self.ui.email_IW.text()
            self.customer.phone_number = self.ui.phone_number_IW.text()

            db_manager.session.commit()
            self.accept()


class AddCompany(AddCustomer):
    """
    Widget used to add new Company(Supplier) to DB
    """

    def set_connections(self):
        super().set_connections()
        self.ui.company_B.setVisible(False)
        self.ui.person_B.setVisible(False)

    def add(self):
        """Method for add button to being run when is clicked used only for supplier mode."""
        if self.req_fields_filled():
            record = Supplier(full_name=self.ui.long_name_IW.text(),
                              name=self.ui.short_name_IW.text(),
                              address=self.ui.address_IW.text(),
                              country=self.ui.country_IW.currentText(),
                              tin_code=self.ui.tin_IW.text(),
                              zip_code=self.ui.zipe_code_IW.text(),
                              city=self.ui.town_IW.text(),
                              email=self.ui.email_IW.text(),
                              phone_number=self.ui.phone_number_IW.text())
            db_manager.session.add(record)
            db_manager.session.commit()
            self.accept()


class EditCompany(AddCompany):
    def __init__(self, company: Supplier):
        super().__init__()
        self.company = company
        self.ui.add_B.setText("Save")
        self.ui.add_B.clicked.disconnect()
        self.ui.add_B.clicked.connect(self.update)  # change of method connected to button
        self.write_values()

    def add(self):
        raise Exception("Method not in use")

    def write_values(self):
        """Write values of Company to appropriate IW"""
        self.ui.long_name_IW.setText(self.company.full_name)
        self.ui.short_name_IW.setText(self.company.name)
        self.ui.country_IW.setCurrentText(self.company.country)
        self.ui.tin_IW.setText(self.company.tin_code)
        self.ui.address_IW.setText(self.company.address)
        self.ui.town_IW.setText(self.company.city)
        self.ui.zipe_code_IW.setText(self.company.zip_code)
        self.ui.email_IW.setText(self.company.email)
        self.ui.phone_number_IW.setText(str(self.company.phone_number))

    def update(self):
        if self.req_fields_filled():
            self.company.full_name = self.ui.long_name_IW.text()
            self.company.name = self.ui.short_name_IW.text()
            self.company.country = self.ui.country_IW.currentText()
            self.company.tin_code = self.ui.tin_IW.text()
            self.company.address = self.ui.address_IW.text()
            self.company.city = self.ui.town_IW.text()
            self.company.zip_code = self.ui.zipe_code_IW.text()
            self.company.email = self.ui.email_IW.text()
            self.company.phone_number = self.ui.phone_number_IW.text()
            db_manager.session.commit()
            self.accept()

