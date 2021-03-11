from gui_windows.welcome_window import Ui_welcome_window
from gui_windows.AddContractorWidget import Ui_add_contractor_QWidget
from gui_windows.start_window import Ui_StartWindow
from gui_windows.products_widget import Ui_product_widget
from gui_windows.edit_product_widget import Ui_edit_product
from gui_windows.price_tables_widget import Ui_price_table_widget
from PySide2 import QtCore, QtGui, QtWidgets
from orm import Customer, Supplier, Product, Category, PriceTable
from db_manager import db_manager
from functools import partial
from utilities import show_msg_box, MessageError
import PySide2
import re

# TODO IDEA: instead of self.ui.long_name_IW.text().strip(), maybe create properties which return it
# TODO Create properties for widgets
class SelectedRowMixin:

    @staticmethod
    def get_selected_row(selectable_widget):
        selected_indexes = {i.row() for i in selectable_widget.selectionModel().selectedIndexes()}
        if len(selected_indexes) == 1:
            return list(selected_indexes)[0]
        else:
            return None  # expected single selection mode


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
        self.ui.price_lists_B.clicked.connect(self.price_lists)

    def edit_customer(self):
        items = db_manager.get_customers_names()
        if len(items) == 0:
            msg_box = QtWidgets.QMessageBox(icon=QtWidgets.QMessageBox.Information, text="There are no customers in your DataBase.")
            msg_box.exec_()
            return
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

    def price_lists(self):
        price_table = PriceTableWidget()
        if price_table.runnable():
            price_table.exec_()


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
                if field.currentText().strip() == '--Select Country--':
                    self.change_border_to_red(field)
                    incorrect = True
            elif hasattr(field, 'text'):
                if field.text().strip() == '':
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
                record = Customer(full_name=self.ui.long_name_IW.text().strip(),
                                  name=self.ui.short_name_IW.text().strip(),
                                  address=self.ui.address_IW.text().strip(),
                                  country=self.ui.country_IW.currentText().strip(),
                                  tin_code=self.ui.tin_IW.text().strip(),
                                  zip_code=self.ui.zipe_code_IW.text().strip(),
                                  city=self.ui.town_IW.text().strip(),
                                  email=self.ui.email_IW.text().strip(),
                                  phone_number=self.ui.phone_number_IW.text().strip(),
                                  is_person=False)
            elif self.ui.person_B.isChecked():
                record = Customer(name=self.ui.first_name_IW.text().strip() + self.ui.surname_IW.text().strip(),
                                  full_name=self.ui.first_name_IW.text().strip() + self.ui.second_name_IW.text().strip() + self.ui.surname_IW.text().strip(),
                                  address=self.ui.address_IW.text().strip(),
                                  zip_code=self.ui.zipe_code_IW.text().strip(),
                                  city=self.ui.town_IW.text().strip(),
                                  email=self.ui.email_IW.text().strip(),
                                  phone_number=self.ui.phone_number_IW.text().strip(),
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
                full_name = self.ui.long_name_IW.text().strip()
                name = self.ui.short_name_IW.text().strip()
                country = self.ui.country_IW.currentText().strip()
                tin_code = self.ui.tin_IW.text().strip()
            elif self.ui.person_B.isChecked():
                is_person = True
                full_name = self.ui.first_name_IW.text().strip() + self.ui.second_name_IW.text().strip() + self.ui.surname_IW.text().strip()
                name = self.ui.first_name_IW.text().strip() + self.ui.surname_IW.text().strip()
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
                self.customer.address = self.ui.address_IW.text().strip()
                self.customer.city = self.ui.town_IW.text().strip()
                self.customer.zip_code = self.ui.zipe_code_IW.text().strip()
                self.customer.email = self.ui.email_IW.text().strip()
                self.customer.phone_number = self.ui.phone_number_IW.text().strip()
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
            record = Supplier(full_name=self.ui.long_name_IW.text().strip(),
                              name=self.ui.short_name_IW.text().strip(),
                              address=self.ui.address_IW.text().strip(),
                              country=self.ui.country_IW.currentText().strip(),
                              tin_code=self.ui.tin_IW.text().strip(),
                              zip_code=self.ui.zipe_code_IW.text().strip(),
                              city=self.ui.town_IW.text().strip(),
                              email=self.ui.email_IW.text().strip(),
                              phone_number=self.ui.phone_number_IW.text().strip())
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
            self.company.full_name = self.ui.long_name_IW.text().strip()
            self.company.name = self.ui.short_name_IW.text().strip()
            self.company.country = self.ui.country_IW.currentText().strip()
            self.company.tin_code = self.ui.tin_IW.text().strip()
            self.company.address = self.ui.address_IW.text().strip()
            self.company.city = self.ui.town_IW.text().strip()
            self.company.zip_code = self.ui.zipe_code_IW.text().strip()
            self.company.email = self.ui.email_IW.text().strip()
            self.company.phone_number = self.ui.phone_number_IW.text().strip()
            db_manager.session.commit()
            self.accept()


class ProductWidget(QtWidgets.QDialog, SelectedRowMixin):

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
        self.ui.change_status_B.clicked.connect(self.change_status)
        self.ui.add_new_category_B.clicked.connect(self.add_category)

        self.ui.category_IW.addItems(self.categories)

    @staticmethod
    def check_product_constraints(product):
        """Method checks if unique fields of customer are currently in use. """
        if db_manager.check_product_name_category_constraint(product.name, product.category):
            raise MessageError(f'Product {product.name} in category {product.category} already exists')

    def add(self):
        product = Product(name=self.ui.product_name_IW.text().strip(), category=self.ui.category_IW.currentText().strip())
        try:
            self.check_product_constraints(product)
        except MessageError as msg:
            show_msg_box(msg)
        else:
            db_manager.session.add(product)
            db_manager.session.commit()
            self.model.add_product(product)

    def edit_product(self):
        selected_row = self.get_selected_row(self.ui.Products_IV)
        if selected_row is None:
            return
        product = self.model.get_product(selected_row)
        edit_widget = EditProductWidget(product.name)
        if edit_widget.exec_():
            product.name = edit_widget.new_name()
            product.category = edit_widget.new_category()
            db_manager.session.commit()

    def change_status(self):
        selected_row = self.get_selected_row(self.ui.Products_IV)
        if selected_row is None:
            return
        product = self.model.get_product(selected_row)
        if product.active:
            product.active = False
        else:
            product.active = True
        db_manager.session.commit()
        self.ui.Products_IV.model().layoutChanged.emit()

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

    def headerData(self, section: int, orientation: PySide2.QtCore.Qt.Orientation, role: int=...):
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
        self.products.pop(index)
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
        return self.ui.product_name_IW.text().strip()

    def new_category(self):
        return self.ui.category_IW.currentText().strip()


class PriceTableWidget(QtWidgets.QDialog, SelectedRowMixin):

    class ValidatedItemDelegate(QtWidgets.QStyledItemDelegate):
        """https://stackoverflow.com/questions/13449971/pyside-pyqt4-how-to-set-a-validator-when-editing-a-cell-in-a-qtableview/13449972#13449972"""

        def createEditor(self, parent, option, index):
            if not index.isValid():
                return 0
            if index.column() == PriceTable.get_price_key():  # price column
                editor = QtWidgets.QLineEdit(parent)
                validator = QtGui.QRegExpValidator("([0-9]+[.])?[0-9]+", editor)
                editor.setValidator(validator)
                return editor
            return super().createEditor(parent, option, index)

    def __init__(self):
        super().__init__()
        self.ui = Ui_price_table_widget()
        self.ui.setupUi(self)
        self.customer_id = None
        self.model = PriceTableModel()
        self.products = db_manager.get_all_products()
        self._connect()

    def _connect(self):
        self.ui.table_IV.setModel(self.model)
        self.ui.add_B.clicked.connect(self.add)
        self.ui.change_status_B.clicked.connect(self.change_status)

        self.ui.product_IW.addItems(self.products)
        for i, product in enumerate(self.products):
            self.ui.product_IW.setItemText(i, product.name)

        # connect signal to refresh category of chosen product
        self.ui.product_IW.currentTextChanged.connect(self.update_category)

        # set current category
        product_index = self.ui.product_IW.currentIndex()
        if product_index == -1:  # missing products
            self.ui.category_IW.setText('')
        else:
            product = self.products[product_index]
            self.ui.category_IW.setText(product.category)

        # RegexValidator on column 1 with prices
        self.ui.price_IW.setValidator(QtGui.QRegExpValidator("([0-9]+[.])?[0-9]+", self.ui.price_IW))
        self.ui.table_IV.setItemDelegate(self.ValidatedItemDelegate())

    def runnable(self):
        self.set_customer_id()
        if self.customer_id is None:
            return False
        else:
            self.refresh_model()
            return True

    def set_customer_id(self):
        customers = db_manager.get_customers_names()
        if len(customers) == 0:
            show_msg_box("Missing customers")
            return
        customer_name, ok = QtWidgets.QInputDialog.getItem(self, 'Customer', 'Please choose customer to show price-list.', customers, 0, False)
        if ok:
            self.customer_id = db_manager.get_customer_id(customer_name=customer_name)
        return

    def refresh_model(self):
        self.model.download_price_table(self.customer_id)

    def update_category(self):
        product_index = self.ui.product_IW.currentIndex()
        product = self.products[product_index]
        self.ui.category_IW.setText(product.category)

    def add(self):
        product_index = self.ui.product_IW.currentIndex()
        if product_index == -1:  # missing products
            return
        product = self.products[product_index]
        if db_manager.product_in_price_table_exists(product.id, self.customer_id):
            return
        price = self.ui.price_IW.text().strip()
        price_table = PriceTable(product_id=product.id, customer_id=self.customer_id, price=0 if price == '' else float(price))
        db_manager.session.add(price_table)
        db_manager.session.commit()
        self.model.add_price_table(price_table)

    def change_status(self):
        selected_row = self.get_selected_row(self.ui.table_IV)
        if selected_row is None:
            return
        price_table = self.model.get_price_table(selected_row)
        if price_table.active:
            price_table.active = False
        else:
            price_table.active = True
        db_manager.session.commit()
        self.ui.table_IV.model().layoutChanged.emit()


class PriceTableModel(QtCore.QAbstractTableModel):

    def __init__(self):
        super().__init__()
        self.price_tables = []

    def rowCount(self, parent):
        return len(self.price_tables)

    def columnCount(self, parent):
        return len(PriceTable.cols())

    def data(self, index, role=QtCore.Qt.DisplayRole):
        if role == QtCore.Qt.DisplayRole:
            row = index.row()
            col = index.column()
            return self.price_tables[row][col]

    def headerData(self, section: int, orientation: PySide2.QtCore.Qt.Orientation, role: int = ...):
        if role == QtCore.Qt.DisplayRole:
            if orientation == QtCore.Qt.Horizontal:
                return PriceTable.cols()[section]
            elif orientation == QtCore.Qt.Vertical:
                return section

    def setData(self, index, value, role):
        if role == QtCore.Qt.EditRole:
            if index.column() == PriceTable.get_price_key():
                self.price_tables[index.row()][index.column()] = value

    def flags(self, index:PySide2.QtCore.QModelIndex) -> PySide2.QtCore.Qt.ItemFlags:
        if index.column() == PriceTable.get_price_key():
            return QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEditable
        else:
            return QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable

    # other methods

    def download_price_table(self, customer_id):
        self.price_tables = db_manager.get_price_table(customer_id)

    def add_price_table(self, price_table):
        self.layoutAboutToBeChanged.emit()
        self.price_tables.append(price_table)
        self.layoutChanged.emit()

    def get_price_table(self, index):
        return self.price_tables[index]

    def delete_price_table(self, index):
        self.layoutAboutToBeChanged.emit()
        self.price_tables.pop(index)
        self.layoutChanged.emit()