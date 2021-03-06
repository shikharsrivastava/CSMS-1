# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'deposit.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(521, 374)
        Form.setStyleSheet("margin:5px;\n"
"padding:3px;\n"
"\n"
"")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.memberIdLineEdit = QtWidgets.QLineEdit(Form)
        self.memberIdLineEdit.setObjectName("memberIdLineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.memberIdLineEdit)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.nameLineEdit = QtWidgets.QLineEdit(Form)
        self.nameLineEdit.setReadOnly(True)
        self.nameLineEdit.setObjectName("nameLineEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.nameLineEdit)
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.accountTypeComboBox = QtWidgets.QComboBox(Form)
        self.accountTypeComboBox.setObjectName("accountTypeComboBox")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.accountTypeComboBox)
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.amountLineEdit = QtWidgets.QLineEdit(Form)
        self.amountLineEdit.setObjectName("amountLineEdit")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.amountLineEdit)
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.paymentModeComboBox = QtWidgets.QComboBox(Form)
        self.paymentModeComboBox.setObjectName("paymentModeComboBox")
        self.paymentModeComboBox.addItem("")
        self.paymentModeComboBox.addItem("")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.paymentModeComboBox)
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.depositeDateEdit = QtWidgets.QDateEdit(Form)
        self.depositeDateEdit.setCalendarPopup(True)
        self.depositeDateEdit.setTimeSpec(QtCore.Qt.LocalTime)
        self.depositeDateEdit.setDate(QtCore.QDate(2017, 1, 1))
        self.depositeDateEdit.setObjectName("depositeDateEdit")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.depositeDateEdit)
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.voucherNoLineEdit = QtWidgets.QLineEdit(Form)
        self.voucherNoLineEdit.setObjectName("voucherNoLineEdit")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.voucherNoLineEdit)
        self.commentLineEdit = QtWidgets.QLineEdit(Form)
        self.commentLineEdit.setObjectName("commentLineEdit")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.commentLineEdit)
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setObjectName("label_9")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.horizontalLayout.addLayout(self.formLayout)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.photoLabel = QtWidgets.QLabel(Form)
        self.photoLabel.setMinimumSize(QtCore.QSize(100, 100))
        self.photoLabel.setMaximumSize(QtCore.QSize(100, 100))
        self.photoLabel.setStyleSheet("background-color:rgb(255, 255, 255);")
        self.photoLabel.setText("")
        self.photoLabel.setTextFormat(QtCore.Qt.PlainText)
        self.photoLabel.setScaledContents(True)
        self.photoLabel.setObjectName("photoLabel")
        self.verticalLayout.addWidget(self.photoLabel)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.depositPushButton = QtWidgets.QPushButton(Form)
        self.depositPushButton.setObjectName("depositPushButton")
        self.verticalLayout.addWidget(self.depositPushButton)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Deposit Form"))
        self.label.setText(_translate("Form", "Member Id:"))
        self.label_3.setText(_translate("Form", "Name:"))
        self.label_4.setText(_translate("Form", "Account Type:"))
        self.label_5.setText(_translate("Form", "Amount:"))
        self.label_6.setText(_translate("Form", "Payment Mode:"))
        self.paymentModeComboBox.setItemText(0, _translate("Form", "Cash"))
        self.paymentModeComboBox.setItemText(1, _translate("Form", "Check"))
        self.label_7.setText(_translate("Form", "Deposite Date:"))
        self.label_8.setText(_translate("Form", "Voucher No:"))
        self.label_9.setText(_translate("Form", "Comment:"))
        self.depositPushButton.setText(_translate("Form", "Submit"))

