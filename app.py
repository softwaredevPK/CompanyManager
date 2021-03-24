from gui_windows.welcome_window import Ui_welcome_window
from gui_windows.AddContractorWidget import Ui_add_contractor_QWidget
from gui_windows.start_window import Ui_StartWindow
from gui_windows.products_widget import Ui_product_widget
from gui_windows.edit_product_widget import Ui_edit_product
from gui_windows.price_tables_widget import Ui_price_table_widget
from gui_windows.show_orders_widget import Ui_show_orders
from gui_windows.order_details_widget import Ui_order_details
from gui_windows.create_order_widget import Ui_create_order
from PySide2 import QtCore, QtGui, QtWidgets
from orm import Customer, Supplier, Product, Category, PriceTable, CustomerOrder, OrderDetail, Order
from db_manager import db_manager
from functools import partial
from utilities import show_msg_box, MessageError, ExcelApplicationContextManager
import PySide2
import xlwings as xw


class MyAbstractModel(QtCore.QAbstractTableModel):
    """Parent class for other AbstractModels with similar implementation of basic methods"""
    model = None

    def __init__(self):
        super().__init__()
        self.list = []

    def rowCount(self, parent):
        return len(self.list)

    def columnCount(self, parent):
        return len(self.model.cols())

    def data(self, index, role=QtCore.Qt.DisplayRole):
        if role == QtCore.Qt.DisplayRole:
            row = index.row()
            col = index.column()
            return self.list[row][col]

    def headerData(self, section: int, orientation: PySide2.QtCore.Qt.Orientation, role: int=...):
        if role == QtCore.Qt.DisplayRole:
            if orientation == QtCore.Qt.Horizontal:
                return self.model.cols()[section]
            elif orientation == QtCore.Qt.Vertical:
                return section

    def sort(self, column:int, order:PySide2.QtCore.Qt.SortOrder=...):
        self.layoutAboutToBeChanged.emit()
        if order == PySide2.QtCore.Qt.SortOrder.AscendingOrder:
            self.list.sort(key=lambda x: x[column], reverse=False)
        else:
            self.list.sort(key=lambda x: x[column], reverse=True)
        self.layoutChanged.emit()

    def setData(self, index, value, role):
        if role == QtCore.Qt.EditRole:
            self.list[index.row()][index.column()] = value
            db_manager.session.commit()
            return True
        else:
            return False

    def flags(self, index: PySide2.QtCore.QModelIndex) -> PySide2.QtCore.Qt.ItemFlags:
        if index.column() in self.model.get_editable_keys():
            return QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEditable
        else:
            return QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable

    # Below method edit list of objects stored in model, do not touch DB

    def add_item(self, item):
        self.layoutAboutToBeChanged.emit()
        self.list.append(item)
        self.layoutChanged.emit()

    def get_item(self, index):
        return self.list[index]

    def delete_item(self, index):
        self.layoutAboutToBeChanged.emit()
        self.list.pop(index)
        self.layoutChanged.emit()


class SelectedRowMixin:

    @staticmethod
    def get_selected_row(selectable_widget):
        """
        Method to get selected row from TableViews which have single selection mode on Rows
        """
        selected_indexes = {i.row() for i in selectable_widget.selectionModel().selectedIndexes()}
        if len(selected_indexes) == 1:
            return list(selected_indexes)[0]
        else:
            return None


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

    def runnable(self):
        """Method used to check if Company Account was created.
         If it return False, then window shouldn't be shown."""
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
        self.ui.company_name_DW.setText(db_manager.get_supplier_full_name())
        self._connect()

    def _connect(self):
        self.ui.add_customer_B.clicked.connect(self.add_customer)
        self.ui.edit_customer_B.clicked.connect(self.edit_customer)
        self.ui.my_procust_B.clicked.connect(self.my_products)
        self.ui.price_lists_B.clicked.connect(self.price_lists)
        self.ui.show_orders_B.clicked.connect(self.show_orders)
        self.ui.add_new_order_B.clicked.connect(self.add_new_order)

    def customer_input_dialog(self):
        """Method used to ask user to choose Customer from list in input dialog.
        return: customer_name, True/False (False when cancelled)"""
        items = db_manager.get_customers_names()
        if len(items) == 0:
            msg_box = QtWidgets.QMessageBox(icon=QtWidgets.QMessageBox.Information,
                                            text="There are no customers in your DataBase.")
            msg_box.exec_()
            return None, None
        else:
            customer_name, ok = QtWidgets.QInputDialog.getItem(self, 'Editor', 'Choose customer to edit', items, 0,
                                                               False)
            return customer_name, ok

    def edit_customer(self):
        customer_name, ok = self.customer_input_dialog()
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

    def show_orders(self):
        orders = ShowOrdersWidget()
        orders.exec_()

    def add_new_order(self):
        customer_name, ok = self.customer_input_dialog()
        if ok:  # not canceled
            customer = db_manager.get_customer(customer_name)
            create = CreateOrderWidget(customer)
            if create.runnable():
                create.exec_()


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
        req = self.ui.data_person_CT.findChildren(QtWidgets.QLineEdit)
        req.remove(self.ui.second_name_IW) # second name is not required
        return req

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

    @property
    def long_name(self):
        return self.ui.long_name_IW.text().strip()

    @property
    def short_name(self):
        return self.ui.short_name_IW.text().strip()

    @property
    def address(self):
        return self.ui.address_IW.text().strip()

    @property
    def tin(self):
        return self.ui.tin_IW.text().strip()

    @property
    def country(self):
        return self.ui.country_IW.currentText().strip()

    @property
    def zip_code(self):
        return self.ui.zipe_code_IW.text().strip()

    @property
    def city(self):
        return self.ui.town_IW.text().strip()

    @property
    def email(self):
        return self.ui.email_IW.text().strip()

    @property
    def phone_no(self):
        return self.ui.phone_number_IW.text().strip()

    @property
    def first_name(self):
        return self.ui.first_name_IW.text().strip()

    @property
    def surname(self):
        return self.ui.surname_IW.text().strip()

    @property
    def second_name(self):
        return self.ui.second_name_IW.text().strip()

    def add(self):
        """Method for add button to being run when is clicked"""
        if self.req_fields_filled():
            if self.ui.company_B.isChecked():
                record = Customer(full_name=self.long_name,
                                  name=self.short_name,
                                  address=self.address,
                                  country=self.country,
                                  tin_code=self.tin,
                                  zip_code=self.zip_code,
                                  city=self.city,
                                  email=self.email,
                                  phone_number=self.phone_no,
                                  is_person=False)
            elif self.ui.person_B.isChecked():
                record = Customer(name=self.first_name + self.surname,
                                  full_name=self.first_name + self.second_name + self.surname,
                                  address=self.address,
                                  zip_code=self.zip_code,
                                  city=self.city,
                                  email=self.email,
                                  phone_number=self.phone_no,
                                  is_person=True)
            # Constraint check(if all unique requirements are passed)
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
                full_name = self.long_name
                name = self.short_name
                country = self.country
                tin_code = self.tin
            elif self.ui.person_B.isChecked():
                is_person = True
                full_name = self.first_name + self.second_name + self.surname
                name = self.first_name + self.surname
                country = ''
                tin_code = ''
            # Constraint check(if all unique requirements are passed)
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
                self.customer.address = self.address
                self.customer.city = self.city
                self.customer.zip_code = self.zip_code
                self.customer.email = self.email
                self.customer.phone_number = self.phone_no()
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
            record = Supplier(full_name=self.long_name,
                              name=self.short_name,
                              address=self.address,
                              country=self.country,
                              tin_code=self.tin,
                              zip_code=self.zip_code,
                              city=self.city,
                              email=self.email,
                              phone_number=self.phone_no)
            # no need of checking constraint, because this widget will be used only once to create user account(company)
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
        """Method updates data in DB"""
        if self.req_fields_filled():
            self.company.full_name = self.long_name
            self.company.name = self.short_name
            self.company.country = self.country
            self.company.tin_code = self.tin
            self.company.address = self.address
            self.company.city = self.country
            self.company.zip_code = self.zip_code
            self.company.email = self.email
            self.company.phone_number = self.phone_no
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

    @property
    def product_name(self):
        return self.ui.product_name_IW.text().strip()

    @property
    def category(self):
        return self.ui.category_IW.currentText().strip()

    def add(self):
        product = Product(name=self.product_name, category=self.category)
        # Constraint check(if all unique requirements are passed)
        try:
            self.check_product_constraints(product)
        except MessageError as msg:
            show_msg_box(msg)
        else:
            db_manager.session.add(product)
            db_manager.session.commit()
            self.model.add_item(product)
            self.ui.Products_IV.resizeColumnsToContents()

    def edit_product(self):
        selected_row = self.get_selected_row(self.ui.Products_IV)
        if selected_row is None:
            return
        product = self.model.get_item(selected_row)
        # edit is made by EditWidget
        edit_widget = EditProductWidget(product.name)
        if edit_widget.exec_():
            product.name = edit_widget.new_name
            product.category = edit_widget.new_category
            db_manager.session.commit()
            self.ui.Products_IV.resizeColumnsToContents()

    def change_status(self):
        """Function change status of given product on Product Table and in all related price-tables.
        If product is no available in general, we can't allow customers to buy it"""
        selected_row = self.get_selected_row(self.ui.Products_IV)
        if selected_row is None:
            return
        product = self.model.get_item(selected_row)
        if product.active:
            product.active = False
        else:
            product.active = True
        # status changes in all price-tales
        price_tables_product = db_manager.get_all_price_tables_for_product_id(product.id)
        for product in price_tables_product:
            if product.active:
                product.active = False
            else:
                product.active = True
        db_manager.session.commit()
        self.ui.Products_IV.model().layoutChanged.emit()

    def add_category(self):
        """Method used to create mew category for products"""
        category_name, ok = QtWidgets.QInputDialog.getText(self, 'Category', 'Please add new category.')
        if not ok:
            return
        if not db_manager.category_exist(category_name):
            category = Category(name=category_name)
            db_manager.session.add(category)
            db_manager.session.commit()
            self.ui.category_IW.addItem(category_name)
            self.ui.Products_IV.resizeColumnsToContents()


class ProductModel(MyAbstractModel):
    model = Product

    def __init__(self):
        super().__init__()
        self.list = db_manager.get_all_products()


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

    @property
    def new_name(self):
        return self.ui.product_name_IW.text().strip()

    @property
    def new_category(self):
        return self.ui.category_IW.currentText().strip()


class PriceTableWidget(QtWidgets.QDialog, SelectedRowMixin):

    # Used for RegexValidation purposes
    class ValidatedItemDelegate(QtWidgets.QStyledItemDelegate):
        """https://stackoverflow.com/questions/13449971/pyside-pyqt4-how-to-set-a-validator-when-editing-a-cell-in-a-qtableview/13449972#13449972"""

        def createEditor(self, parent, option, index):
            if not index.isValid():
                return 0
            if index.column() in PriceTable.get_editable_keys():  # price column
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
        """Method used to check if widget can be .exec"""
        self.set_customer_id()
        if self.customer_id is None:
            return False
        else:
            self.refresh_model()
            return True

    def set_customer_id(self):
        """
        Method try to set customer_ids in appropriate widget if possible.
        """
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
        self.ui.table_IV.resizeColumnsToContents()

    def update_category(self):
        product_index = self.ui.product_IW.currentIndex()
        product = self.products[product_index]
        self.ui.category_IW.setText(product.category)

    @property
    def price(self):
        return self.ui.price_IW.text().strip()

    def add(self):
        product_index = self.ui.product_IW.currentIndex()
        if product_index == -1:  # missing products
            return
        product = self.products[product_index]
        if db_manager.product_in_price_table_exists(product.id, self.customer_id):  # can't add multiple prices for 1 product
            return
        price = self.price
        price_table = PriceTable(product_id=product.id, customer_id=self.customer_id, price=0 if price == '' else float(price),
                                 active=product.active) # should have same status as product has actually
        db_manager.session.add(price_table)
        db_manager.session.commit()
        self.model.add_item(price_table)
        self.ui.table_IV.resizeColumnsToContents()

    def change_status(self):
        selected_row = self.get_selected_row(self.ui.table_IV)
        if selected_row is None:
            return
        price_table = self.model.get_item(selected_row)
        if price_table.active:
            price_table.active = False
        else:
            price_table.active = True
        db_manager.session.commit()
        self.ui.table_IV.model().layoutChanged.emit()
        self.ui.table_IV.resizeColumnsToContents()


class PriceTableModel(MyAbstractModel):
    model = PriceTable

    def __init__(self):
        super().__init__()
        self.list = []

    # other methods
    def download_price_table(self, customer_id):
        self.list = db_manager.get_price_table(customer_id)


class ShowOrdersWidget(QtWidgets.QDialog, SelectedRowMixin):

    def __init__(self):
        super().__init__()
        self.ui = Ui_show_orders()
        self.ui.setupUi(self)
        self.model = ShowOrdersModel()
        self._connect()

    def _connect(self):
        self.ui.orders_IV.setModel(self.model)
        self.ui.details_B.clicked.connect(self.details)
        self.ui.edit_B.clicked.connect(self.edit)

    def details(self):
        selected_row = self.get_selected_row(self.ui.orders_IV)
        if selected_row is None:
            return
        order_id = self.model.get_item(selected_row).id
        details = OrderDetailsWidget(order_id)
        self.close()
        details.exec_()

    def edit(self):
        selected_row = self.get_selected_row(self.ui.orders_IV)
        if selected_row is None:
            return
        order_id = self.model.get_item(selected_row).id
        customer = db_manager.get_customer_by_order_id(order_id)
        edit_widget = EditOrderWidget(customer, order_id)
        if edit_widget.runnable():
            self.accept()
            edit_widget.exec_()

    def to_excel(self):

        def set_borders(sheet_range, top=False, bottom=False, left=False, right=False, line_style=1, weight=2, theme_color=1, tint_n_shade=0):
            """function used to create borders on given range of sheet
            Below int values are vba values of properties:  https://docs.microsoft.com/en-us/office/vba/api/excel.borders"""
            borders = []
            if top:
                borders.append(8)
            if bottom:
                borders.append(9)
            if left:
                borders.append(7)
            if right:
                borders.append(10)
            for border in borders:

                sheet_range.api.Borders(border).LineStyle = line_style
                sheet_range.api.Borders(border).Weight = weight
                sheet_range.api.Borders(border).ThemeColor = theme_color
                sheet_range.api.Borders(border).TintAndShade = tint_n_shade
        # todo create button, add screen to readme
        # I decided to use xlwings to set print area and other properties that are unavailable in other libraries
        selected_row = self.get_selected_row(self.ui.orders_IV)
        if selected_row is None:
            return
        order = self.model.get_item(selected_row)
        supplier = db_manager.get_supplier()
        customer = db_manager.get_customer_by_order_id(order.id)
        order_details = db_manager.get_order_details(order.id)
        with ExcelApplicationContextManager(app=None, visible=False, kill_app=True, display_alerts=False,
                                            ask_to_update_links=False, enable_events=False, screen_updating=False) as _:
            wb = xw.Book()
            sheet = wb.sheets[0]
            sheet.range('A1').value = f'Order no. {order.id}'
            sheet.range('A2').value = f"Delivery date {order.delivery_date.strftime('%d/%m/%Y')}"
            sheet.range('E1').value = order.order_date.strftime('%d/%m/%Y')

            # Supplier data
            sheet.range('A4').value = "Supplier"
            sheet.range('A5').value = supplier.full_name
            sheet.range('A6').value = supplier.address
            sheet.range('A7').value = f'{supplier.zip_code} {supplier.city}'
            sheet.range('A8').value = supplier.country_tin
            sheet.range('A9').value = f'E-mail: {supplier.email}'
            sheet.range('A10').value = f'Phone: {supplier.phone_number}'

            # Customer data
            sheet.range('D4').value = 'Customer'
            sheet.range('D5').value = customer.full_name
            sheet.range('D6').value = customer.address
            sheet.range('D7').value = f'{customer.zip_code} {customer.city}'
            sheet.range('D8').value = customer.country_tin
            sheet.range('D9').value = f'E-mail: {customer.email}'
            sheet.range('D10').value = f'Phone: {customer.phone_number}'

            # Create header of table
            sheet.range('A12').value = ["No.", 'Product name', 'Quantity', 'Unit price', 'Total price']
            set_borders(sheet.range('A12:E12'), top=True, bottom=True, left=True, right=True)
            sheet.range('A12:E12').api.Interior.color = 10921638
            # write data to table
            total = 0
            for i, order_detail in enumerate(order_details):
                no = i + 1
                sheet.range(f'A{12 + no}').value = [order_detail.product.name, order_detail.quantity, order_detail.unit_price, order_detail.total_price]
                total += order_detail.total_price
            for col in 'ABCDE':
                set_borders(sheet.range(f'{col}13:{col}{12 + no}', top=True, bottom=True, left=True, right=True))

            sheet.range(f'D{12 + no + 2}').value = 'TOTAL'  # 2 rows below last row table
            sheet.range(f'E{12 + no + 2}').value = total
            set_borders(f'A{12 + no + 2}:E{12 + no + 2}', top=True, weight=-4138)
            sheet.range('A:E').api.EntireColumn.Autofit
            sheet.book.app.api.ActiveWindow.DisplayGridlines = False

            sheet.api.PageSetup.Zoom = False
            sheet.api.PageSetup.FitToPagesWide = 1
            sheet.api.PageSetup.FitToPageTall = 1
            # sheet.book.save()







class ShowOrdersModel(MyAbstractModel):
    model = CustomerOrder

    def __init__(self):
        super().__init__()
        self.list = db_manager.get_all_customers_orders()


class OrderDetailsWidget(QtWidgets.QDialog, SelectedRowMixin):
    def __init__(self, order_id):
        super().__init__()
        self.order_id = order_id
        self.ui = Ui_order_details()
        self.ui.setupUi(self)
        self.model = OrderDetailsModel(order_id)
        self._connect()

    def _connect(self):
        self.ui.table_IV.setModel(self.model)
        self.ui.edit_B.clicked.connect(self.edit)
        self.ui.return_B.clicked.connect(self.return_)

    def return_(self):
        orders = ShowOrdersWidget()
        self.close()
        orders.exec_()

    def edit(self):
        customer = db_manager.get_customer_by_order_id(self.order_id)
        edit_widget = EditOrderWidget(customer, self.order_id)
        if edit_widget.runnable():
            self.accept()
            edit_widget.exec_()


class OrderDetailsModel(MyAbstractModel):
    model = OrderDetail

    def __init__(self, order_id=None):
        super().__init__()
        if order_id is None:
            self.list = []
        else:
            self.list = db_manager.get_order_details(order_id)


class CreateOrderWidget(QtWidgets.QDialog, SelectedRowMixin):
    """
    Widget is based on flush, because of implementation of AbstractTableModel
    """

    def __init__(self, customer):
        super().__init__()
        self.customer = customer
        self.ui = Ui_create_order()
        self.ui.setupUi(self)
        self.model = OrderDetailsModel()
        self.order = None
        self.saved = False
        self.products = db_manager.get_customer_products(customer.id)
        self._connect()

    def closeEvent(self, arg__1:PySide2.QtGui.QCloseEvent):
        if self.saved:
            self.accept()
        else:
            db_manager.session.rollback()
            self.accept()

    def _connect(self):
        self.ui.product_IW.addItems(self.products)
        for i, product in enumerate(self.products):
            self.ui.product_IW.setItemText(i, product.product.name)

        self.ui.quantity_IW.setValidator(QtGui.QRegExpValidator("\d+", self.ui.quantity_IW))
        self.ui.order_date_IW.setDate(QtCore.QDate.currentDate())
        self.ui.delivery_date_IW.setDate(QtCore.QDate.currentDate())
        self.ui.table_IV.setModel(self.model)
        self.ui.save_B.clicked.connect(self.save)
        self.ui.add_B.clicked.connect(self.add)
        self.ui.remove_B.clicked.connect(self.remove)

    def runnable(self):
        """Method used to check if widget can be .exec"""
        if len(self.products) == 0:
            show_msg_box(f"Missing price-list for {self.customer.name}")
            return False
        else:
            return True

    @property
    def order_date(self):
        return self.ui.order_date_IW.date().toPython()

    @property
    def delivery_date(self):
        return self.ui.delivery_date_IW.date().toPython()

    @property
    def quantity(self):
        return self.ui.quantity_IW.text()

    @property
    def product(self):
        return self.products[self.ui.product_IW.currentIndex()]

    def add(self):
        if self.order is None:
            self.order = Order(customer_id=self.customer.id, order_date=self.order_date, delivery_date=self.delivery_date)
            db_manager.session.add(self.order)
            db_manager.session.flush()
        if db_manager.product_in_order_exist(self.order.id, self.product.product_id):  # such item has been added already
            return
        order_detail = OrderDetail(order_id=self.order.id, product_id=self.product.product_id, quantity=self.quantity, unit_price=self.product.price)
        db_manager.session.add(order_detail)
        db_manager.session.flush()
        self.model.add_item(order_detail)
        self.ui.table_IV.resizeColumnsToContents()

    def save(self):
        self.saved = True
        self.order = Order(customer_id=self.customer.id, order_date=self.order_date, delivery_date=self.delivery_date) # refresh if has changed
        db_manager.session.commit()  # all flushed items are commited
        # add to OrderDetail products order_id and commit them
        self.accept()

    def remove(self):
        selected_row = self.get_selected_row(self.ui.table_IV)
        if selected_row is None:
            return
        order_detail = self.model.list[selected_row]
        db_manager.session.delete(order_detail)
        db_manager.session.flush()
        self.model.delete_item(selected_row)
        self.ui.table_IV.resizeColumnsToContents()


class EditOrderWidget(CreateOrderWidget):
    def __init__(self, customer, order_id):
        QtWidgets.QDialog.__init__(self)
        self.customer = customer
        self.ui = Ui_create_order()
        self.ui.setupUi(self)
        self.order = db_manager.get_order_by_order_id(order_id)
        self.model = OrderDetailsModel(order_id)
        self.saved = False
        self.products = db_manager.get_customer_products(customer.id)
        self._connect()

    def _connect(self):
        super()._connect()
        self.ui.order_date_IW.setDate(self.order.order_date)
        self.ui.delivery_date_IW.setDate(self.order.delivery_date)

    def save(self):
        """Save method here, should change update Order + OrderDetails models"""
        self.saved = True
        self.order.order_date = self.order_date
        self.order.delivery_date = self.delivery_date
        db_manager.session.commit()  # all flushed items are commited
        # add to OrderDetail products order_id and commit them
        self.accept()

    def add(self):
        if db_manager.product_in_order_exist(self.order.id, self.product.product_id):  # check such item has been added already
            return
        order_detail = OrderDetail(order_id=self.order.id, product_id=self.product.product_id, quantity=self.quantity, unit_price=self.product.price)
        db_manager.session.add(order_detail)
        db_manager.session.flush()
        self.model.add_item(order_detail)
        self.ui.table_IV.resizeColumnsToContents()


# todo i have comma instead of dot in Price-Lists



# todo maybe something that generate Documents? For example: Generate pdf - create pdf for Order (maybe word->pdf or Excel -> PDF)