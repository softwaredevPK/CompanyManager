# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'order_details_widget.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_order_details(object):
    def setupUi(self, order_details):
        if not order_details.objectName():
            order_details.setObjectName(u"order_details")
        order_details.resize(699, 413)
        self.verticalLayout = QVBoxLayout(order_details)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.table_IV = QTableView(order_details)
        self.table_IV.setObjectName(u"table_IV")
        self.table_IV.setSelectionMode(QAbstractItemView.NoSelection)
        self.table_IV.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.verticalLayout.addWidget(self.table_IV)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.edit_B = QPushButton(order_details)
        self.edit_B.setObjectName(u"edit_B")

        self.horizontalLayout.addWidget(self.edit_B)

        self.return_B = QPushButton(order_details)
        self.return_B.setObjectName(u"return_B")

        self.horizontalLayout.addWidget(self.return_B)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(order_details)

        QMetaObject.connectSlotsByName(order_details)
    # setupUi

    def retranslateUi(self, order_details):
        order_details.setWindowTitle(QCoreApplication.translate("order_details", u"Form", None))
        self.edit_B.setText(QCoreApplication.translate("order_details", u"Edit", None))
        self.return_B.setText(QCoreApplication.translate("order_details", u"Return", None))
    # retranslateUi

