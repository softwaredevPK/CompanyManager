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
        StartWindow.resize(800, 600)
        self.centralwidget = QWidget(StartWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.add_customer_B = QPushButton(self.centralwidget)
        self.add_customer_B.setObjectName(u"add_customer_B")

        self.verticalLayout.addWidget(self.add_customer_B)

        self.edit_customer_B = QPushButton(self.centralwidget)
        self.edit_customer_B.setObjectName(u"edit_customer_B")

        self.verticalLayout.addWidget(self.edit_customer_B)

        self.my_procust_B = QPushButton(self.centralwidget)
        self.my_procust_B.setObjectName(u"my_procust_B")

        self.verticalLayout.addWidget(self.my_procust_B)

        StartWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(StartWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 21))
        StartWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(StartWindow)
        self.statusbar.setObjectName(u"statusbar")
        StartWindow.setStatusBar(self.statusbar)

        self.retranslateUi(StartWindow)

        QMetaObject.connectSlotsByName(StartWindow)
    # setupUi

    def retranslateUi(self, StartWindow):
        StartWindow.setWindowTitle(QCoreApplication.translate("StartWindow", u"MainWindow", None))
        self.add_customer_B.setText(QCoreApplication.translate("StartWindow", u"Add Customer", None))
        self.edit_customer_B.setText(QCoreApplication.translate("StartWindow", u"Edit Customer", None))
        self.my_procust_B.setText(QCoreApplication.translate("StartWindow", u"My Products", None))
    # retranslateUi

