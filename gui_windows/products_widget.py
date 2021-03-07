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
        self.product_name_DW = QLabel(product_widget)
        self.product_name_DW.setObjectName(u"product_name_DW")

        self.gridLayout.addWidget(self.product_name_DW, 1, 0, 1, 1)

        self.product_name_IW = QLineEdit(product_widget)
        self.product_name_IW.setObjectName(u"product_name_IW")

        self.gridLayout.addWidget(self.product_name_IW, 2, 0, 1, 1)

        self.add_B = QPushButton(product_widget)
        self.add_B.setObjectName(u"add_B")

        self.gridLayout.addWidget(self.add_B, 1, 1, 2, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.Products_IV = QTableView(product_widget)
        self.Products_IV.setObjectName(u"Products_IV")

        self.verticalLayout.addWidget(self.Products_IV)


        self.retranslateUi(product_widget)

        QMetaObject.connectSlotsByName(product_widget)
    # setupUi

    def retranslateUi(self, product_widget):
        product_widget.setWindowTitle(QCoreApplication.translate("product_widget", u"Form", None))
        self.product_name_DW.setText(QCoreApplication.translate("product_widget", u"Product Name", None))
        self.add_B.setText(QCoreApplication.translate("product_widget", u"Add", None))
    # retranslateUi

