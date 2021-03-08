# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'edit_product_widget.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_edit_product(object):
    def setupUi(self, edit_product):
        if not edit_product.objectName():
            edit_product.setObjectName(u"edit_product")
        edit_product.resize(265, 112)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(edit_product.sizePolicy().hasHeightForWidth())
        edit_product.setSizePolicy(sizePolicy)
        edit_product.setMinimumSize(QSize(0, 110))
        edit_product.setMaximumSize(QSize(16777215, 112))
        self.verticalLayout = QVBoxLayout(edit_product)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetMinAndMaxSize)
        self.title_DW = QLabel(edit_product)
        self.title_DW.setObjectName(u"title_DW")
        sizePolicy.setHeightForWidth(self.title_DW.sizePolicy().hasHeightForWidth())
        self.title_DW.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.title_DW)

        self.product_name_IW = QLineEdit(edit_product)
        self.product_name_IW.setObjectName(u"product_name_IW")

        self.verticalLayout.addWidget(self.product_name_IW)

        self.category_IW = QComboBox(edit_product)
        self.category_IW.setObjectName(u"category_IW")

        self.verticalLayout.addWidget(self.category_IW)

        self.ok_cancel_B = QDialogButtonBox(edit_product)
        self.ok_cancel_B.setObjectName(u"ok_cancel_B")
        self.ok_cancel_B.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.ok_cancel_B.setCenterButtons(False)

        self.verticalLayout.addWidget(self.ok_cancel_B)


        self.retranslateUi(edit_product)

        QMetaObject.connectSlotsByName(edit_product)
    # setupUi

    def retranslateUi(self, edit_product):
        edit_product.setWindowTitle(QCoreApplication.translate("edit_product", u"Form", None))
#if QT_CONFIG(accessibility)
        edit_product.setAccessibleDescription("")
#endif // QT_CONFIG(accessibility)
        self.title_DW.setText(QCoreApplication.translate("edit_product", u"Please change current product name and category.", None))
    # retranslateUi

