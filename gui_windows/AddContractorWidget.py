# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AddContractorWidget.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_add_contractor_QWidget(object):
    def setupUi(self, add_contractor_QWidget):
        if not add_contractor_QWidget.objectName():
            add_contractor_QWidget.setObjectName(u"add_contractor_QWidget")
        add_contractor_QWidget.resize(780, 290)
        add_contractor_QWidget.setMinimumSize(QSize(780, 290))
        add_contractor_QWidget.setMaximumSize(QSize(780, 290))
        self.gridLayout = QGridLayout(add_contractor_QWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.scrollArea = QScrollArea(add_contractor_QWidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setMinimumSize(QSize(755, 210))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 745, 269))
        self.gridLayout_2 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalSpacer = QSpacerItem(1, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 0, 1, 1, 1)

        self.additional_data_CT = QGroupBox(self.scrollAreaWidgetContents)
        self.additional_data_CT.setObjectName(u"additional_data_CT")
        self.additional_data_CT.setFlat(True)
        self.gridLayout_4 = QGridLayout(self.additional_data_CT)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.phone_number_IW = QLineEdit(self.additional_data_CT)
        self.phone_number_IW.setObjectName(u"phone_number_IW")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.phone_number_IW.sizePolicy().hasHeightForWidth())
        self.phone_number_IW.setSizePolicy(sizePolicy)
        self.phone_number_IW.setMinimumSize(QSize(250, 20))

        self.gridLayout_4.addWidget(self.phone_number_IW, 5, 2, 1, 1)

        self.town_IW = QLineEdit(self.additional_data_CT)
        self.town_IW.setObjectName(u"town_IW")
        sizePolicy.setHeightForWidth(self.town_IW.sizePolicy().hasHeightForWidth())
        self.town_IW.setSizePolicy(sizePolicy)
        self.town_IW.setMinimumSize(QSize(250, 20))

        self.gridLayout_4.addWidget(self.town_IW, 2, 2, 1, 1)

        self.phone_number_DW = QLabel(self.additional_data_CT)
        self.phone_number_DW.setObjectName(u"phone_number_DW")
        self.phone_number_DW.setMinimumSize(QSize(0, 20))

        self.gridLayout_4.addWidget(self.phone_number_DW, 5, 0, 1, 1)

        self.email_DW = QLabel(self.additional_data_CT)
        self.email_DW.setObjectName(u"email_DW")
        self.email_DW.setMinimumSize(QSize(0, 20))

        self.gridLayout_4.addWidget(self.email_DW, 4, 0, 1, 1)

        self.email_IW = QLineEdit(self.additional_data_CT)
        self.email_IW.setObjectName(u"email_IW")
        sizePolicy.setHeightForWidth(self.email_IW.sizePolicy().hasHeightForWidth())
        self.email_IW.setSizePolicy(sizePolicy)
        self.email_IW.setMinimumSize(QSize(250, 20))

        self.gridLayout_4.addWidget(self.email_IW, 4, 2, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer, 6, 1, 1, 2)

        self.town_DW = QLabel(self.additional_data_CT)
        self.town_DW.setObjectName(u"town_DW")
        self.town_DW.setMinimumSize(QSize(0, 20))

        self.gridLayout_4.addWidget(self.town_DW, 2, 0, 1, 1)

        self.zip_code_DW = QLabel(self.additional_data_CT)
        self.zip_code_DW.setObjectName(u"zip_code_DW")
        self.zip_code_DW.setMinimumSize(QSize(0, 20))

        self.gridLayout_4.addWidget(self.zip_code_DW, 3, 0, 1, 1)

        self.zipe_code_IW = QLineEdit(self.additional_data_CT)
        self.zipe_code_IW.setObjectName(u"zipe_code_IW")
        sizePolicy.setHeightForWidth(self.zipe_code_IW.sizePolicy().hasHeightForWidth())
        self.zipe_code_IW.setSizePolicy(sizePolicy)
        self.zipe_code_IW.setMinimumSize(QSize(250, 20))

        self.gridLayout_4.addWidget(self.zipe_code_IW, 3, 2, 1, 1)

        self.address_DW = QLabel(self.additional_data_CT)
        self.address_DW.setObjectName(u"address_DW")
        self.address_DW.setMinimumSize(QSize(0, 20))

        self.gridLayout_4.addWidget(self.address_DW, 1, 0, 1, 1)

        self.address_IW = QLineEdit(self.additional_data_CT)
        self.address_IW.setObjectName(u"address_IW")
        sizePolicy.setHeightForWidth(self.address_IW.sizePolicy().hasHeightForWidth())
        self.address_IW.setSizePolicy(sizePolicy)
        self.address_IW.setMinimumSize(QSize(250, 20))

        self.gridLayout_4.addWidget(self.address_IW, 1, 2, 1, 1)


        self.gridLayout_2.addWidget(self.additional_data_CT, 0, 2, 1, 1)

        self.data_CT = QGroupBox(self.scrollAreaWidgetContents)
        self.data_CT.setObjectName(u"data_CT")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.data_CT.sizePolicy().hasHeightForWidth())
        self.data_CT.setSizePolicy(sizePolicy1)
        self.data_CT.setMinimumSize(QSize(356, 0))
        self.data_CT.setFlat(True)
        self.gridLayout_3 = QGridLayout(self.data_CT)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.data_company_CT = QFrame(self.data_CT)
        self.data_company_CT.setObjectName(u"data_company_CT")
        self.data_company_CT.setFrameShape(QFrame.StyledPanel)
        self.data_company_CT.setFrameShadow(QFrame.Raised)
        self.formLayout_2 = QFormLayout(self.data_company_CT)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.long_name_DW = QLabel(self.data_company_CT)
        self.long_name_DW.setObjectName(u"long_name_DW")
        self.long_name_DW.setMinimumSize(QSize(0, 20))

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.long_name_DW)

        self.long_name_IW = QLineEdit(self.data_company_CT)
        self.long_name_IW.setObjectName(u"long_name_IW")
        self.long_name_IW.setMinimumSize(QSize(0, 20))

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.long_name_IW)

        self.short_name_DW = QLabel(self.data_company_CT)
        self.short_name_DW.setObjectName(u"short_name_DW")
        self.short_name_DW.setMinimumSize(QSize(0, 20))

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.short_name_DW)

        self.short_name_IW = QLineEdit(self.data_company_CT)
        self.short_name_IW.setObjectName(u"short_name_IW")
        self.short_name_IW.setMinimumSize(QSize(0, 20))

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.short_name_IW)

        self.country_DW = QLabel(self.data_company_CT)
        self.country_DW.setObjectName(u"country_DW")
        self.country_DW.setMinimumSize(QSize(0, 20))

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.country_DW)

        self.country_IW = QComboBox(self.data_company_CT)
        self.country_IW.setObjectName(u"country_IW")
        self.country_IW.setMinimumSize(QSize(0, 20))

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.country_IW)

        self.tin_DW = QLabel(self.data_company_CT)
        self.tin_DW.setObjectName(u"tin_DW")
        self.tin_DW.setMinimumSize(QSize(0, 20))
        self.tin_DW.setMaximumSize(QSize(16777215, 20))

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.tin_DW)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_6 = QSpacerItem(1, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_6)

        self.tin_country_IW = QLineEdit(self.data_company_CT)
        self.tin_country_IW.setObjectName(u"tin_country_IW")
        sizePolicy2 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.tin_country_IW.sizePolicy().hasHeightForWidth())
        self.tin_country_IW.setSizePolicy(sizePolicy2)
        self.tin_country_IW.setMinimumSize(QSize(50, 20))
        self.tin_country_IW.setMaximumSize(QSize(50, 16777215))
        self.tin_country_IW.setReadOnly(True)

        self.horizontalLayout.addWidget(self.tin_country_IW)

        self.tin_IW = QLineEdit(self.data_company_CT)
        self.tin_IW.setObjectName(u"tin_IW")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(200)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.tin_IW.sizePolicy().hasHeightForWidth())
        self.tin_IW.setSizePolicy(sizePolicy3)
        self.tin_IW.setMinimumSize(QSize(133, 20))

        self.horizontalLayout.addWidget(self.tin_IW)

        self.horizontalSpacer_5 = QSpacerItem(1, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_5)


        self.formLayout_2.setLayout(3, QFormLayout.FieldRole, self.horizontalLayout)


        self.gridLayout_3.addWidget(self.data_company_CT, 0, 0, 1, 2)

        self.data_person_CT = QFrame(self.data_CT)
        self.data_person_CT.setObjectName(u"data_person_CT")
        self.data_person_CT.setFrameShape(QFrame.StyledPanel)
        self.data_person_CT.setFrameShadow(QFrame.Raised)
        self.formLayout_3 = QFormLayout(self.data_person_CT)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.first_name_DW = QLabel(self.data_person_CT)
        self.first_name_DW.setObjectName(u"first_name_DW")
        self.first_name_DW.setMinimumSize(QSize(0, 20))

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.first_name_DW)

        self.first_name_IW = QLineEdit(self.data_person_CT)
        self.first_name_IW.setObjectName(u"first_name_IW")
        self.first_name_IW.setMinimumSize(QSize(0, 20))

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.first_name_IW)

        self.second_name_DW = QLabel(self.data_person_CT)
        self.second_name_DW.setObjectName(u"second_name_DW")
        self.second_name_DW.setMinimumSize(QSize(0, 20))

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.second_name_DW)

        self.second_name_IW = QLineEdit(self.data_person_CT)
        self.second_name_IW.setObjectName(u"second_name_IW")
        self.second_name_IW.setMinimumSize(QSize(0, 20))

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.second_name_IW)

        self.surname_DW = QLabel(self.data_person_CT)
        self.surname_DW.setObjectName(u"surname_DW")
        self.surname_DW.setMinimumSize(QSize(0, 20))

        self.formLayout_3.setWidget(2, QFormLayout.LabelRole, self.surname_DW)

        self.surname_IW = QLineEdit(self.data_person_CT)
        self.surname_IW.setObjectName(u"surname_IW")
        self.surname_IW.setMinimumSize(QSize(0, 20))

        self.formLayout_3.setWidget(2, QFormLayout.FieldRole, self.surname_IW)


        self.gridLayout_3.addWidget(self.data_person_CT, 1, 0, 1, 2)


        self.gridLayout_2.addWidget(self.data_CT, 0, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 0, 4, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout.addWidget(self.scrollArea, 3, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_3 = QSpacerItem(300, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.company_B = QRadioButton(add_contractor_QWidget)
        self.company_B.setObjectName(u"company_B")
        self.company_B.setChecked(True)

        self.horizontalLayout_2.addWidget(self.company_B)

        self.person_B = QRadioButton(add_contractor_QWidget)
        self.person_B.setObjectName(u"person_B")

        self.horizontalLayout_2.addWidget(self.person_B)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)


        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.clear_B = QPushButton(add_contractor_QWidget)
        self.clear_B.setObjectName(u"clear_B")
        self.clear_B.setMaximumSize(QSize(350, 16777215))

        self.horizontalLayout_3.addWidget(self.clear_B)

        self.add_B = QPushButton(add_contractor_QWidget)
        self.add_B.setObjectName(u"add_B")

        self.horizontalLayout_3.addWidget(self.add_B)


        self.gridLayout.addLayout(self.horizontalLayout_3, 5, 0, 1, 1)

        QWidget.setTabOrder(self.long_name_IW, self.short_name_IW)
        QWidget.setTabOrder(self.short_name_IW, self.country_IW)
        QWidget.setTabOrder(self.country_IW, self.tin_IW)
        QWidget.setTabOrder(self.tin_IW, self.first_name_IW)
        QWidget.setTabOrder(self.first_name_IW, self.address_IW)
        QWidget.setTabOrder(self.address_IW, self.town_IW)
        QWidget.setTabOrder(self.town_IW, self.zipe_code_IW)
        QWidget.setTabOrder(self.zipe_code_IW, self.email_IW)
        QWidget.setTabOrder(self.email_IW, self.phone_number_IW)
        QWidget.setTabOrder(self.phone_number_IW, self.surname_IW)
        QWidget.setTabOrder(self.surname_IW, self.add_B)
        QWidget.setTabOrder(self.add_B, self.tin_country_IW)
        QWidget.setTabOrder(self.tin_country_IW, self.scrollArea)
        QWidget.setTabOrder(self.scrollArea, self.company_B)
        QWidget.setTabOrder(self.company_B, self.person_B)
        QWidget.setTabOrder(self.person_B, self.clear_B)
        QWidget.setTabOrder(self.clear_B, self.second_name_IW)

        self.retranslateUi(add_contractor_QWidget)

        QMetaObject.connectSlotsByName(add_contractor_QWidget)
    # setupUi

    def retranslateUi(self, add_contractor_QWidget):
        add_contractor_QWidget.setWindowTitle(QCoreApplication.translate("add_contractor_QWidget", u"Form", None))
        self.additional_data_CT.setTitle(QCoreApplication.translate("add_contractor_QWidget", u"Additional Data", None))
        self.phone_number_DW.setText(QCoreApplication.translate("add_contractor_QWidget", u"Phone Number", None))
        self.email_DW.setText(QCoreApplication.translate("add_contractor_QWidget", u"Email", None))
        self.town_DW.setText(QCoreApplication.translate("add_contractor_QWidget", u"Town", None))
        self.zip_code_DW.setText(QCoreApplication.translate("add_contractor_QWidget", u"Zip Code", None))
        self.address_DW.setText(QCoreApplication.translate("add_contractor_QWidget", u"Address", None))
        self.data_CT.setTitle(QCoreApplication.translate("add_contractor_QWidget", u"Data", None))
        self.long_name_DW.setText(QCoreApplication.translate("add_contractor_QWidget", u"Long Name", None))
        self.short_name_DW.setText(QCoreApplication.translate("add_contractor_QWidget", u"Short Name", None))
        self.country_DW.setText(QCoreApplication.translate("add_contractor_QWidget", u"Country", None))
        self.tin_DW.setText(QCoreApplication.translate("add_contractor_QWidget", u"TIN", None))
#if QT_CONFIG(accessibility)
        self.tin_country_IW.setAccessibleDescription("")
#endif // QT_CONFIG(accessibility)
        self.first_name_DW.setText(QCoreApplication.translate("add_contractor_QWidget", u"First Name", None))
        self.second_name_DW.setText(QCoreApplication.translate("add_contractor_QWidget", u"Second Name", None))
        self.surname_DW.setText(QCoreApplication.translate("add_contractor_QWidget", u"Surname", None))
        self.company_B.setText(QCoreApplication.translate("add_contractor_QWidget", u"Company", None))
        self.person_B.setText(QCoreApplication.translate("add_contractor_QWidget", u"Person", None))
        self.clear_B.setText(QCoreApplication.translate("add_contractor_QWidget", u"Clear", None))
        self.add_B.setText(QCoreApplication.translate("add_contractor_QWidget", u"Add", None))
    # retranslateUi

