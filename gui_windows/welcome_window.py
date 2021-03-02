# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'welcome_window.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_welcome_window(object):
    def setupUi(self, welcome_window):
        if not welcome_window.objectName():
            welcome_window.setObjectName(u"welcome_window")
        welcome_window.resize(490, 349)
        self.centralwidget = QWidget(welcome_window)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.title_DW = QLabel(self.centralwidget)
        self.title_DW.setObjectName(u"title_DW")
        self.title_DW.setMinimumSize(QSize(0, 100))
        font = QFont()
        font.setFamily(u"MS Sans Serif")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.title_DW.setFont(font)
        self.title_DW.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.title_DW)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.edit_B = QPushButton(self.centralwidget)
        self.edit_B.setObjectName(u"edit_B")

        self.verticalLayout.addWidget(self.edit_B)

        self.start_B = QPushButton(self.centralwidget)
        self.start_B.setObjectName(u"start_B")

        self.verticalLayout.addWidget(self.start_B)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        welcome_window.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(welcome_window)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 490, 21))
        welcome_window.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(welcome_window)
        self.statusbar.setObjectName(u"statusbar")
        welcome_window.setStatusBar(self.statusbar)

        self.retranslateUi(welcome_window)

        QMetaObject.connectSlotsByName(welcome_window)
    # setupUi

    def retranslateUi(self, welcome_window):
        welcome_window.setWindowTitle(QCoreApplication.translate("welcome_window", u"Welcome Window", None))
        self.title_DW.setText(QCoreApplication.translate("welcome_window", u"Company Manager", None))
        self.edit_B.setText(QCoreApplication.translate("welcome_window", u"Edit company settingss", None))
        self.start_B.setText(QCoreApplication.translate("welcome_window", u"Start", None))
    # retranslateUi

