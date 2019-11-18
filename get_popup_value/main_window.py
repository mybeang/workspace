# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui',
# licensing of 'main_window.ui' applies.
#
# Created: Tue Feb 19 11:16:08 2019
#      by: pyside2-uic  running on PySide2 5.12.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(636, 480)
        self.terminal = QtWidgets.QTextEdit(Form)
        self.terminal.setGeometry(QtCore.QRect(20, 20, 591, 381))
        self.terminal.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.terminal.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.terminal.setObjectName("terminal")
        self.bt_start = QtWidgets.QPushButton(Form)
        self.bt_start.setGeometry(QtCore.QRect(20, 430, 75, 23))
        self.bt_start.setObjectName("bt_start")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtWidgets.QApplication.translate("Form", "Form", None, -1))
        self.bt_start.setText(QtWidgets.QApplication.translate("Form", "Start", None, -1))

