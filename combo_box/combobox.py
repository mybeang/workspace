# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'combobox.ui',
# licensing of 'combobox.ui' applies.
#
# Created: Tue Feb 26 18:04:52 2019
#      by: pyside2-uic  running on PySide2 5.12.0
#
# WARNING! All changes made in this file will be lost!
import sys
from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(451, 158)
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(30, 40, 371, 41))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtWidgets.QApplication.translate("Form", "Form", None, -1))
        self.comboBox.setItemText(0, QtWidgets.QApplication.translate("Form", "1", None, -1))
        self.comboBox.setItemText(1, QtWidgets.QApplication.translate("Form", "2", None, -1))
        self.comboBox.setItemText(2, QtWidgets.QApplication.translate("Form", "3", None, -1))
        self.comboBox.setItemText(3, QtWidgets.QApplication.translate("Form", "4", None, -1))
        self.comboBox.setItemText(4, QtWidgets.QApplication.translate("Form", "5", None, -1))
        self.comboBox.setItemText(5, QtWidgets.QApplication.translate("Form", "6", None, -1))
        self.comboBox.setItemText(6, QtWidgets.QApplication.translate("Form", "7", None, -1))
        self.comboBox.setItemText(7, QtWidgets.QApplication.translate("Form", "8", None, -1))
        self.comboBox.setItemText(8, QtWidgets.QApplication.translate("Form", "9", None, -1))
        self.comboBox.setItemText(9, QtWidgets.QApplication.translate("Form", "10", None, -1))

    def get_print(self):
        all_items = [self.comboBox.itemText(i) for i in range(self.comboBox.count())]
        print(all_items)
        print(all_items[all_items.index('2'):all_items.index('5') + 1])


if __name__=="__main__":
    app = QtWidgets.QApplication()
    ui = Ui_Form()
    win = QtWidgets.QMainWindow()
    ui.setupUi(win)
    ui.retranslateUi(win)
    ui.get_print()
    win.show()
    sys.exit(app.exec_())