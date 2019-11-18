# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'text_edit.ui',
# licensing of 'text_edit.ui' applies.
#
# Created: Mon Feb 18 14:14:45 2019
#      by: pyside2-uic  running on PySide2 5.12.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(821, 456)
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(20, 410, 441, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.bt_append = QtWidgets.QPushButton(Form)
        self.bt_append.setGeometry(QtCore.QRect(470, 410, 101, 23))
        self.bt_append.setAutoDefault(True)
        self.bt_append.setObjectName("bt_append")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(20, 10, 781, 381))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        self.textEdit.setFont(font)
        self.textEdit.setProperty("cursor", QtCore.Qt.IBeamCursor)
        self.textEdit.setReadOnly(True)
        self.textEdit.setOverwriteMode(True)
        self.textEdit.setObjectName("textEdit")
        self.bt_insert = QtWidgets.QPushButton(Form)
        self.bt_insert.setGeometry(QtCore.QRect(580, 410, 101, 23))
        self.bt_insert.setAutoDefault(True)
        self.bt_insert.setObjectName("bt_insert")
        self.bt_count = QtWidgets.QPushButton(Form)
        self.bt_count.setGeometry(QtCore.QRect(690, 410, 111, 23))
        self.bt_count.setObjectName("bt_count")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtWidgets.QApplication.translate("Form", "Form", None, -1))
        self.bt_append.setText(QtWidgets.QApplication.translate("Form", "append", None, -1))
        self.bt_insert.setText(QtWidgets.QApplication.translate("Form", "insert", None, -1))
        self.bt_count.setText(QtWidgets.QApplication.translate("Form", "Count", None, -1))

