# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'start_window.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_StartWindow(object):
    def setupUi(self, StartWindow):
        if not StartWindow.objectName():
            StartWindow.setObjectName(u"StartWindow")
        StartWindow.resize(701, 492)
        self.centralwidget = QWidget(StartWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.company_name_DW = QLabel(self.centralwidget)
        self.company_name_DW.setObjectName(u"company_name_DW")
        self.company_name_DW.setMinimumSize(QSize(0, 100))
        self.company_name_DW.setMaximumSize(QSize(16777215, 200))
        font = QFont()
        font.setFamily(u"MS Sans Serif")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.company_name_DW.setFont(font)
        self.company_name_DW.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.company_name_DW)

        self.add_customer_B = QPushButton(self.centralwidget)
        self.add_customer_B.setObjectName(u"add_customer_B")

        self.verticalLayout.addWidget(self.add_customer_B)

        self.edit_customer_B = QPushButton(self.centralwidget)
        self.edit_customer_B.setObjectName(u"edit_customer_B")

        self.verticalLayout.addWidget(self.edit_customer_B)

        self.my_procust_B = QPushButton(self.centralwidget)
        self.my_procust_B.setObjectName(u"my_procust_B")

        self.verticalLayout.addWidget(self.my_procust_B)

        self.price_lists_B = QPushButton(self.centralwidget)
        self.price_lists_B.setObjectName(u"price_lists_B")

        self.verticalLayout.addWidget(self.price_lists_B)

        self.add_new_order_B = QPushButton(self.centralwidget)
        self.add_new_order_B.setObjectName(u"add_new_order_B")

        self.verticalLayout.addWidget(self.add_new_order_B)

        self.show_orders_B = QPushButton(self.centralwidget)
        self.show_orders_B.setObjectName(u"show_orders_B")

        self.verticalLayout.addWidget(self.show_orders_B)

        StartWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(StartWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 701, 21))
        StartWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(StartWindow)
        self.statusbar.setObjectName(u"statusbar")
        StartWindow.setStatusBar(self.statusbar)

        self.retranslateUi(StartWindow)

        QMetaObject.connectSlotsByName(StartWindow)
    # setupUi

    def retranslateUi(self, StartWindow):
        StartWindow.setWindowTitle(QCoreApplication.translate("StartWindow", u"MainWindow", None))
        self.company_name_DW.setText(QCoreApplication.translate("StartWindow", u"Company Name", None))
        self.add_customer_B.setText(QCoreApplication.translate("StartWindow", u"Add Customer", None))
        self.edit_customer_B.setText(QCoreApplication.translate("StartWindow", u"Edit Customer", None))
        self.my_procust_B.setText(QCoreApplication.translate("StartWindow", u"My Products", None))
        self.price_lists_B.setText(QCoreApplication.translate("StartWindow", u"Price-lists", None))
        self.add_new_order_B.setText(QCoreApplication.translate("StartWindow", u"Add new order", None))
        self.show_orders_B.setText(QCoreApplication.translate("StartWindow", u"Show orders", None))
    # retranslateUi

