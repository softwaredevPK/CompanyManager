# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'create_order_widget.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_create_order(object):
    def setupUi(self, create_order):
        if not create_order.objectName():
            create_order.setObjectName(u"create_order")
        create_order.resize(667, 382)
        self.verticalLayout = QVBoxLayout(create_order)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.delivery_date_IW = QDateEdit(create_order)
        self.delivery_date_IW.setObjectName(u"delivery_date_IW")

        self.gridLayout.addWidget(self.delivery_date_IW, 3, 3, 1, 1)

        self.quantity_DW = QLabel(create_order)
        self.quantity_DW.setObjectName(u"quantity_DW")

        self.gridLayout.addWidget(self.quantity_DW, 1, 1, 1, 1)

        self.order_date_IW = QDateEdit(create_order)
        self.order_date_IW.setObjectName(u"order_date_IW")

        self.gridLayout.addWidget(self.order_date_IW, 3, 2, 1, 1)

        self.product_DW = QLabel(create_order)
        self.product_DW.setObjectName(u"product_DW")

        self.gridLayout.addWidget(self.product_DW, 1, 0, 1, 1)

        self.quantity_IW = QLineEdit(create_order)
        self.quantity_IW.setObjectName(u"quantity_IW")

        self.gridLayout.addWidget(self.quantity_IW, 3, 1, 1, 1)

        self.delivery_date_DW = QLabel(create_order)
        self.delivery_date_DW.setObjectName(u"delivery_date_DW")

        self.gridLayout.addWidget(self.delivery_date_DW, 1, 3, 1, 1)

        self.product_IW = QComboBox(create_order)
        self.product_IW.setObjectName(u"product_IW")
        self.product_IW.setMinimumSize(QSize(150, 0))

        self.gridLayout.addWidget(self.product_IW, 3, 0, 1, 1)

        self.order_date_DW = QLabel(create_order)
        self.order_date_DW.setObjectName(u"order_date_DW")

        self.gridLayout.addWidget(self.order_date_DW, 1, 2, 1, 1)

        self.add_B = QPushButton(create_order)
        self.add_B.setObjectName(u"add_B")

        self.gridLayout.addWidget(self.add_B, 1, 4, 3, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.table_IV = QTableView(create_order)
        self.table_IV.setObjectName(u"table_IV")
        self.table_IV.setSelectionMode(QAbstractItemView.SingleSelection)
        self.table_IV.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.verticalLayout.addWidget(self.table_IV)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.remove_B = QPushButton(create_order)
        self.remove_B.setObjectName(u"remove_B")

        self.horizontalLayout.addWidget(self.remove_B)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.save_B = QPushButton(create_order)
        self.save_B.setObjectName(u"save_B")

        self.verticalLayout.addWidget(self.save_B)


        self.retranslateUi(create_order)

        QMetaObject.connectSlotsByName(create_order)
    # setupUi

    def retranslateUi(self, create_order):
        create_order.setWindowTitle(QCoreApplication.translate("create_order", u"Form", None))
        self.quantity_DW.setText(QCoreApplication.translate("create_order", u"Quantity", None))
        self.product_DW.setText(QCoreApplication.translate("create_order", u"Product", None))
        self.delivery_date_DW.setText(QCoreApplication.translate("create_order", u"Delivery date", None))
        self.order_date_DW.setText(QCoreApplication.translate("create_order", u"Order date", None))
        self.add_B.setText(QCoreApplication.translate("create_order", u"Add", None))
        self.remove_B.setText(QCoreApplication.translate("create_order", u"Remove", None))
        self.save_B.setText(QCoreApplication.translate("create_order", u"Save", None))
    # retranslateUi

