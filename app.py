from gui_windows.welcome_window import Ui_welcome_window
from gui_windows.AddContractorWidget import Ui_add_contractor_QWidget
from gui_windows.start_window import Ui_StartWindow
from gui_windows.products_widget import Ui_product_widget
from gui_windows.edit_product_widget import Ui_edit_product
from PySide2 import QtCore, QtGui, QtWidgets
from orm import Customer, Supplier, Product, Category
from db_manager import db_manager
from functools import partial
from utilities import show_msg_box, MessageError
import PySide2


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
            customer_name, ok = QtWidgets.QInputDialog.getItem(self, 'Editor', 'Choose customer to edit', items, 0, False)
        if ok:  # not canceled
            customer = db_manager.get_customer(customer_name)
            edit_cust = EditCustomer(customer)
            edit_cust.exec_()

    def add_customer(self):
        add_cust = AddCustomer()
        add_cust.exec_()

    def my_products(self):
        product_wg = ProductWidget()
        product_wg.exec_()


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

    @staticmethod
    def check_customer_constraints(customer):
        """Method checks if unique fields of customer are currently in use. """
        if db_manager.check_customer_names_constraint(customer.name):
            raise MessageError('Customer short name already is used')
        elif db_manager.check_customer_full_name_constraint(customer.full_name):
            raise MessageError('Customer long name already is used')
        elif db_manager.check_customer_country_tin_constraint(customer.country, customer.tin_code):
            raise MessageError('Customer country and tin_code already are used')

    def set_connections(self):
        self.ui.company_B.toggled.connect(self.to_company)
        self.ui.person_B.toggled.connect(self.to_person)
        self.ui.tin_IW.setValidator(QtGui.QRegExpValidator("[\d[a-zA-Z]+", self.ui.tin_IW))
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
            try:
                self.check_customer_constraints(record)
            except MessageError as msg:
                show_msg_box(msg)
            else:
                db_manager.session.add(record)
                db_manager.session.commit()
                self.clear()   # at the end it should clear all field


class EditCustomer(AddCustomer):

    def __init__(self, customer: Customer):
        super().__init__()
        self.customer = customer
        self.ui.add_B.setText("Save")
        self.write_values()
        self.start_country = customer.country
        self.start_tin = customer.tin_code
        self.start_name = customer.name
        self.start_full_name = customer.full_name

    def set_connections(self):
        super(EditCustomer, self).set_connections()
        self.ui.add_B.clicked.disconnect()
        self.ui.add_B.clicked.connect(self.update)  # change of method connected to button

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

    def check_customer_constraints(self, name, full_name, country, tin):
        """Method checks if unique fields of customer has changed, in such case checks if new values are free."""
        if self.start_name != name:
            if db_manager.check_customer_names_constraint(name):
                raise MessageError('Customer name already in used')
        elif self.start_full_name != full_name:
            if db_manager.check_customer_full_name_constraint(full_name):
                raise MessageError('Customer full_name already in used')
        elif self.start_tin != tin and self.start_country != country:
            if db_manager.check_customer_country_tin_constraint(country, tin):
                raise MessageError('Customer country and tin_code already are used')

    def update(self):
        if self.req_fields_filled():
            if self.ui.company_B.isChecked():
                is_person = False
                full_name = self.ui.long_name_IW.text()
                name = self.ui.short_name_IW.text()
                country = self.ui.country_IW.currentText()
                tin_code = self.ui.tin_IW.text()
            elif self.ui.person_B.isChecked():
                is_person = True
                full_name = self.ui.first_name_IW.text() + self.ui.second_name_IW.text() + self.ui.surname_IW.text()
                name = self.ui.first_name_IW.text() + self.ui.surname_IW.text()
                country = ''
                tin_code = ''
            try:
                self.check_customer_constraints(name, full_name, country, tin_code)
            except MessageError as msg:
                show_msg_box(msg)
            else:
                self.customer.full_name = full_name
                self.customer.name = name
                self.customer.country = country
                self.customer.tin_code = tin_code
                self.customer.is_person = is_person
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
        self.write_values()

    def set_connections(self):
        super(EditCompany, self).set_connections()
        self.ui.add_B.clicked.disconnect()
        self.ui.add_B.clicked.connect(self.update)  # change of method connected to button

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


class ProductWidget(QtWidgets.QDialog):

    def __init__(self):
        super().__init__()
        self.ui = Ui_product_widget()
        self.ui.setupUi(self)
        self.model = ProductModel()
        self.categories = db_manager.get_categories()
        self._connect()

    def _connect(self):
        self.ui.Products_IV.setModel(self.model)
        self.ui.add_B.clicked.connect(self.add)
        self.ui.edit_B.clicked.connect(self.edit_product)
        self.ui.delete_B.clicked.connect(self.delete_product)
        self.ui.add_new_category_B.clicked.connect(self.add_category)

        # setting sorting
        # proxy_model = QtCore.QSortFilterProxyModel()
        # proxy_model.setSourceModel(self.model)
        # self.ui.Products_IV.setModel(proxy_model)

        self.ui.category_IW.addItems(self.categories)

    def get_selected_row(self):
        selected_indexes = {i.row() for i in self.ui.Products_IV.selectionModel().selectedIndexes()}
        if len(selected_indexes) == 1:
            return list(selected_indexes)[0]
        else:
            return None  # expected single selection mode

    def add(self):
        product = Product(name=self.ui.product_name_IW.text(), category=self.ui.category_IW.currentText())
        db_manager.session.add(product)
        db_manager.session.commit()
        self.model.add_product(product)

    def edit_product(self):
        selected_row = self.get_selected_row()
        if selected_row is None:
            return
        product = self.model.get_product(selected_row)
        edit_widget = EditProductWidget(product.name)
        if edit_widget.exec_():
            product.name = edit_widget.new_name()
            product.category = edit_widget.new_category()
            db_manager.session.commit()

    def delete_product(self):
        selected_row = self.get_selected_row()
        if selected_row is None:
            return
        product = self.model.get_product(selected_row)
        db_manager.session.delete(product)
        db_manager.session.commit()
        self.model.delete_product(selected_row)

    def add_category(self):
        category_name, ok = QtWidgets.QInputDialog.getText(self, 'Category', 'Please add new category.')
        if not ok:
            return
        if not db_manager.category_exist(category_name):
            category = Category(name=category_name)
            db_manager.session.add(category)
            db_manager.session.commit()
            self.ui.category_IW.addItem(category_name)


class ProductModel(QtCore.QAbstractTableModel):

    def __init__(self):
        super().__init__()
        self.products = db_manager.get_all_products()

    def rowCount(self, parent):
        return len(self.products)

    def columnCount(self, parent):
        return len(Product.cols())

    def data(self, index, role=QtCore.Qt.DisplayRole):
        if role == QtCore.Qt.DisplayRole:
            row = index.row()
            col = index.column()
            return self.products[row][col]

    def headerData(self, section:int, orientation:PySide2.QtCore.Qt.Orientation, role:int=...):
        if role == QtCore.Qt.DisplayRole:
            if orientation == QtCore.Qt.Horizontal:
                return Product.cols()[section]
            elif orientation == QtCore.Qt.Vertical:
                return section

    # Below method edit list of objects stored in model, do not touch DB

    def add_product(self, product: Product):
        self.layoutAboutToBeChanged.emit()
        self.products.append(product)
        self.layoutChanged.emit()

    def get_product(self, index):
        return self.products[index]

    def delete_product(self, index):
        self.layoutAboutToBeChanged.emit()
        self.products = self.products[:index] + self.products[index + 1:]
        self.layoutChanged.emit()

    def sort(self, column:int, order:PySide2.QtCore.Qt.SortOrder=...):
        self.layoutAboutToBeChanged.emit()
        if order == PySide2.QtCore.Qt.SortOrder.AscendingOrder:
            self.products.sort(key=lambda x: x[column], reverse=False)
        else:
            self.products.sort(key=lambda x: x[column], reverse=True)
        self.layoutChanged.emit()


class EditProductWidget(QtWidgets.QDialog):
    def __init__(self, curr_name):
        super().__init__()
        self.ui = Ui_edit_product()
        self.ui.setupUi(self)
        self.ui.category_IW.addItems(db_manager.get_categories())
        self.ui.product_name_IW.setText(curr_name)
        self._connect()

    def _connect(self):
        self.ui.ok_cancel_B.button(QtWidgets.QDialogButtonBox.Ok).clicked.connect(self.accept)
        self.ui.ok_cancel_B.button(QtWidgets.QDialogButtonBox.Cancel).clicked.connect(self.reject)

    def new_name(self):
        return self.ui.product_name_IW.text()

    def new_category(self):
        return self.ui.category_IW.currentText()
