# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'products_widget.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_product_widget(object):
    def setupUi(self, product_widget):
        if not product_widget.objectName():
            product_widget.setObjectName(u"product_widget")
        product_widget.resize(776, 496)
        self.verticalLayout = QVBoxLayout(product_widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.product_name_IW = QLineEdit(product_widget)
        self.product_name_IW.setObjectName(u"product_name_IW")

        self.gridLayout.addWidget(self.product_name_IW, 2, 0, 1, 1)

        self.product_name_DW = QLabel(product_widget)
        self.product_name_DW.setObjectName(u"product_name_DW")

        self.gridLayout.addWidget(self.product_name_DW, 1, 0, 1, 1)

        self.category_DW = QLabel(product_widget)
        self.category_DW.setObjectName(u"category_DW")

        self.gridLayout.addWidget(self.category_DW, 1, 1, 1, 1)

        self.add_new_category_B = QPushButton(product_widget)
        self.add_new_category_B.setObjectName(u"add_new_category_B")

        self.gridLayout.addWidget(self.add_new_category_B, 1, 2, 2, 1)

        self.category_IW = QComboBox(product_widget)
        self.category_IW.setObjectName(u"category_IW")
        self.category_IW.setMinimumSize(QSize(150, 0))

        self.gridLayout.addWidget(self.category_IW, 2, 1, 1, 1)

        self.add_B = QPushButton(product_widget)
        self.add_B.setObjectName(u"add_B")

        self.gridLayout.addWidget(self.add_B, 1, 4, 2, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 1, 3, 2, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.Products_IV = QTableView(product_widget)
        self.Products_IV.setObjectName(u"Products_IV")
        self.Products_IV.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.Products_IV.setSelectionMode(QAbstractItemView.SingleSelection)
        self.Products_IV.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.Products_IV.setSortingEnabled(True)
        self.Products_IV.horizontalHeader().setCascadingSectionResizes(True)
        self.Products_IV.verticalHeader().setVisible(True)
        self.Products_IV.verticalHeader().setHighlightSections(True)

        self.verticalLayout.addWidget(self.Products_IV)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.edit_B = QPushButton(product_widget)
        self.edit_B.setObjectName(u"edit_B")

        self.horizontalLayout.addWidget(self.edit_B)

        self.delete_B = QPushButton(product_widget)
        self.delete_B.setObjectName(u"delete_B")

        self.horizontalLayout.addWidget(self.delete_B)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(product_widget)

        QMetaObject.connectSlotsByName(product_widget)
    # setupUi

    def retranslateUi(self, product_widget):
        product_widget.setWindowTitle(QCoreApplication.translate("product_widget", u"Form", None))
        self.product_name_DW.setText(QCoreApplication.translate("product_widget", u"Product Name", None))
        self.category_DW.setText(QCoreApplication.translate("product_widget", u"Category", None))
        self.add_new_category_B.setText(QCoreApplication.translate("product_widget", u"Add new category", None))
        self.add_B.setText(QCoreApplication.translate("product_widget", u"Add", None))
        self.edit_B.setText(QCoreApplication.translate("product_widget", u"Edit", None))
        self.delete_B.setText(QCoreApplication.translate("product_widget", u"Delete", None))
    # retranslateUi

