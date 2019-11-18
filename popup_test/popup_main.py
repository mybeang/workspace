# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'popup_test.ui',
# licensing of 'popup_test.ui' applies.
#
# Created: Mon Mar  4 09:36:20 2019
#      by: pyside2-uic  running on PySide2 5.12.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(728, 402)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.TE_1 = QtWidgets.QTextEdit(self.centralwidget)
        self.TE_1.setGeometry(QtCore.QRect(20, 20, 331, 301))
        self.TE_1.setObjectName("TE_1")
        self.TE_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.TE_2.setGeometry(QtCore.QRect(360, 20, 351, 301))
        self.TE_2.setObjectName("TE_2")
        self.PB_1 = QtWidgets.QPushButton(self.centralwidget)
        self.PB_1.setGeometry(QtCore.QRect(20, 330, 75, 23))
        self.PB_1.setObjectName("PB_1")
        self.PB_2 = QtWidgets.QPushButton(self.centralwidget)
        self.PB_2.setGeometry(QtCore.QRect(360, 330, 75, 23))
        self.PB_2.setObjectName("PB_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 728, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None, -1))
        self.PB_1.setText(QtWidgets.QApplication.translate("MainWindow", "print on 1", None, -1))
        self.PB_2.setText(QtWidgets.QApplication.translate("MainWindow", "print on 2", None, -1))

