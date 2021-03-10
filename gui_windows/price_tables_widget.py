# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'price_tables_widget.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_price_table_widget(object):
    def setupUi(self, price_table_widget):
        if not price_table_widget.objectName():
            price_table_widget.setObjectName(u"price_table_widget")
        price_table_widget.resize(580, 363)
        self.verticalLayout = QVBoxLayout(price_table_widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 0, 3, 2, 1)

        self.product_DW = QLabel(price_table_widget)
        self.product_DW.setObjectName(u"product_DW")

        self.gridLayout.addWidget(self.product_DW, 0, 0, 1, 1)

        self.price_DW = QLabel(price_table_widget)
        self.price_DW.setObjectName(u"price_DW")

        self.gridLayout.addWidget(self.price_DW, 0, 2, 1, 1)

        self.add_B = QPushButton(price_table_widget)
        self.add_B.setObjectName(u"add_B")

        self.gridLayout.addWidget(self.add_B, 0, 4, 2, 1)

        self.product_IW = QComboBox(price_table_widget)
        self.product_IW.setObjectName(u"product_IW")
        self.product_IW.setMinimumSize(QSize(150, 0))

        self.gridLayout.addWidget(self.product_IW, 1, 0, 1, 1)

        self.price_IW = QLineEdit(price_table_widget)
        self.price_IW.setObjectName(u"price_IW")
        self.price_IW.setMaximumSize(QSize(120, 16777215))

        self.gridLayout.addWidget(self.price_IW, 1, 2, 1, 1)

        self.category_DW = QLabel(price_table_widget)
        self.category_DW.setObjectName(u"category_DW")

        self.gridLayout.addWidget(self.category_DW, 0, 1, 1, 1)

        self.category_IW = QLineEdit(price_table_widget)
        self.category_IW.setObjectName(u"category_IW")
        self.category_IW.setEnabled(True)
        self.category_IW.setReadOnly(True)

        self.gridLayout.addWidget(self.category_IW, 1, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.table_IV = QTableView(price_table_widget)
        self.table_IV.setObjectName(u"table_IV")
        self.table_IV.setSelectionMode(QAbstractItemView.SingleSelection)
        self.table_IV.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.verticalLayout.addWidget(self.table_IV)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.delete_B = QPushButton(price_table_widget)
        self.delete_B.setObjectName(u"delete_B")

        self.horizontalLayout.addWidget(self.delete_B)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(price_table_widget)

        QMetaObject.connectSlotsByName(price_table_widget)
    # setupUi

    def retranslateUi(self, price_table_widget):
        price_table_widget.setWindowTitle(QCoreApplication.translate("price_table_widget", u"Form", None))
        self.product_DW.setText(QCoreApplication.translate("price_table_widget", u"Product", None))
        self.price_DW.setText(QCoreApplication.translate("price_table_widget", u"Price", None))
        self.add_B.setText(QCoreApplication.translate("price_table_widget", u"Add", None))
        self.category_DW.setText(QCoreApplication.translate("price_table_widget", u"Category", None))
        self.delete_B.setText(QCoreApplication.translate("price_table_widget", u"Delete", None))
    # retranslateUi

