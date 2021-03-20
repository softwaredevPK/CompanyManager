# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'show_orders_widget.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_show_orders(object):
    def setupUi(self, show_orders):
        if not show_orders.objectName():
            show_orders.setObjectName(u"show_orders")
        show_orders.resize(400, 299)
        self.verticalLayout = QVBoxLayout(show_orders)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.orders_IV = QTableView(show_orders)
        self.orders_IV.setObjectName(u"orders_IV")
        self.orders_IV.setSelectionMode(QAbstractItemView.SingleSelection)
        self.orders_IV.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.orders_IV.setSortingEnabled(True)
        self.orders_IV.horizontalHeader().setProperty("showSortIndicator", True)

        self.verticalLayout.addWidget(self.orders_IV)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.edit_B = QPushButton(show_orders)
        self.edit_B.setObjectName(u"edit_B")

        self.horizontalLayout.addWidget(self.edit_B)

        self.details_B = QPushButton(show_orders)
        self.details_B.setObjectName(u"details_B")

        self.horizontalLayout.addWidget(self.details_B)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(show_orders)

        QMetaObject.connectSlotsByName(show_orders)
    # setupUi

    def retranslateUi(self, show_orders):
        show_orders.setWindowTitle(QCoreApplication.translate("show_orders", u"Form", None))
        self.edit_B.setText(QCoreApplication.translate("show_orders", u"Edit", None))
        self.details_B.setText(QCoreApplication.translate("show_orders", u"show details", None))
    # retranslateUi

