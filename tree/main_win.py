# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_win.ui',
# licensing of 'main_win.ui' applies.
#
# Created: Fri Mar 15 17:39:03 2019
#      by: pyside2-uic  running on PySide2 5.12.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.TR_TC = QtWidgets.QTreeWidget(self.centralwidget)
        self.TR_TC.setGeometry(QtCore.QRect(20, 20, 291, 431))
        self.TR_TC.setIndentation(10)
        self.TR_TC.setAllColumnsShowFocus(True)
        self.TR_TC.setExpandsOnDoubleClick(True)
        self.TR_TC.setObjectName("TR_TC")
        item_0 = QtWidgets.QTreeWidgetItem(self.TR_TC)
        item_0 = QtWidgets.QTreeWidgetItem(self.TR_TC)
        item_0 = QtWidgets.QTreeWidgetItem(self.TR_TC)
        item_0 = QtWidgets.QTreeWidgetItem(self.TR_TC)
        item_0 = QtWidgets.QTreeWidgetItem(self.TR_TC)
        item_0 = QtWidgets.QTreeWidgetItem(self.TR_TC)
        item_0 = QtWidgets.QTreeWidgetItem(self.TR_TC)
        item_0 = QtWidgets.QTreeWidgetItem(self.TR_TC)
        self.TR_TC.header().setDefaultSectionSize(200)
        self.TR_TC.header().setMinimumSectionSize(0)
        self.PB_StartTest = QtWidgets.QPushButton(self.centralwidget)
        self.PB_StartTest.setGeometry(QtCore.QRect(320, 20, 75, 23))
        self.PB_StartTest.setObjectName("PB_StartTest")
        self.CB_EEPROM = QtWidgets.QCheckBox(self.centralwidget)
        self.CB_EEPROM.setGeometry(QtCore.QRect(327, 128, 171, 16))
        self.CB_EEPROM.setObjectName("CB_EEPROM")
        self.CB_RTCOp = QtWidgets.QCheckBox(self.centralwidget)
        self.CB_RTCOp.setGeometry(QtCore.QRect(330, 280, 181, 16))
        self.CB_RTCOp.setObjectName("CB_RTCOp")
        self.LE_BLBRE = QtWidgets.QLineEdit(self.centralwidget)
        self.LE_BLBRE.setGeometry(QtCore.QRect(524, 90, 31, 20))
        self.LE_BLBRE.setAlignment(QtCore.Qt.AlignCenter)
        self.LE_BLBRE.setObjectName("LE_BLBRE")
        self.CB_Diag = QtWidgets.QCheckBox(self.centralwidget)
        self.CB_Diag.setGeometry(QtCore.QRect(327, 167, 121, 16))
        self.CB_Diag.setObjectName("CB_Diag")
        self.LE_DiagRE = QtWidgets.QLineEdit(self.centralwidget)
        self.LE_DiagRE.setGeometry(QtCore.QRect(527, 166, 31, 20))
        self.LE_DiagRE.setAlignment(QtCore.Qt.AlignCenter)
        self.LE_DiagRE.setObjectName("LE_DiagRE")
        self.CB_BLBooting = QtWidgets.QCheckBox(self.centralwidget)
        self.CB_BLBooting.setGeometry(QtCore.QRect(324, 91, 171, 16))
        self.CB_BLBooting.setObjectName("CB_BLBooting")
        self.CB_WDOp = QtWidgets.QCheckBox(self.centralwidget)
        self.CB_WDOp.setGeometry(QtCore.QRect(330, 322, 171, 16))
        self.CB_WDOp.setObjectName("CB_WDOp")
        self.LE_EEPROMRE = QtWidgets.QLineEdit(self.centralwidget)
        self.LE_EEPROMRE.setGeometry(QtCore.QRect(527, 127, 31, 20))
        self.LE_EEPROMRE.setAlignment(QtCore.Qt.AlignCenter)
        self.LE_EEPROMRE.setObjectName("LE_EEPROMRE")
        self.CB_OsImgDn = QtWidgets.QCheckBox(self.centralwidget)
        self.CB_OsImgDn.setGeometry(QtCore.QRect(329, 202, 181, 16))
        self.CB_OsImgDn.setObjectName("CB_OsImgDn")
        self.LE_PowRE = QtWidgets.QLineEdit(self.centralwidget)
        self.LE_PowRE.setGeometry(QtCore.QRect(524, 55, 31, 20))
        self.LE_PowRE.setAlignment(QtCore.Qt.AlignCenter)
        self.LE_PowRE.setObjectName("LE_PowRE")
        self.CB_PwrOnOff = QtWidgets.QCheckBox(self.centralwidget)
        self.CB_PwrOnOff.setGeometry(QtCore.QRect(324, 56, 131, 16))
        self.CB_PwrOnOff.setObjectName("CB_PwrOnOff")
        self.CB_OSBooting = QtWidgets.QCheckBox(self.centralwidget)
        self.CB_OSBooting.setGeometry(QtCore.QRect(330, 241, 181, 16))
        self.CB_OSBooting.setObjectName("CB_OSBooting")
        self.LE_WDRE = QtWidgets.QLineEdit(self.centralwidget)
        self.LE_WDRE.setGeometry(QtCore.QRect(530, 320, 31, 20))
        self.LE_WDRE.setAlignment(QtCore.Qt.AlignCenter)
        self.LE_WDRE.setObjectName("LE_WDRE")
        self.LE_RTCRE = QtWidgets.QLineEdit(self.centralwidget)
        self.LE_RTCRE.setGeometry(QtCore.QRect(530, 279, 31, 20))
        self.LE_RTCRE.setAlignment(QtCore.Qt.AlignCenter)
        self.LE_RTCRE.setObjectName("LE_RTCRE")
        self.LE_OSDNRE = QtWidgets.QLineEdit(self.centralwidget)
        self.LE_OSDNRE.setGeometry(QtCore.QRect(529, 200, 31, 20))
        self.LE_OSDNRE.setAlignment(QtCore.Qt.AlignCenter)
        self.LE_OSDNRE.setObjectName("LE_OSDNRE")
        self.LE_OSBootRE = QtWidgets.QLineEdit(self.centralwidget)
        self.LE_OSBootRE.setGeometry(QtCore.QRect(530, 240, 31, 20))
        self.LE_OSBootRE.setAlignment(QtCore.Qt.AlignCenter)
        self.LE_OSBootRE.setObjectName("LE_OSBootRE")
        self.PB_PASS = QtWidgets.QPushButton(self.centralwidget)
        self.PB_PASS.setGeometry(QtCore.QRect(320, 360, 75, 23))
        self.PB_PASS.setObjectName("PB_PASS")
        self.PB_FAIL = QtWidgets.QPushButton(self.centralwidget)
        self.PB_FAIL.setGeometry(QtCore.QRect(320, 380, 75, 23))
        self.PB_FAIL.setObjectName("PB_FAIL")
        self.PTE_what = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.PTE_what.setGeometry(QtCore.QRect(420, 370, 171, 71))
        self.PTE_what.setObjectName("PTE_what")
        self.RB_Console = QtWidgets.QRadioButton(self.centralwidget)
        self.RB_Console.setGeometry(QtCore.QRect(320, 410, 90, 16))
        self.RB_Console.setObjectName("RB_Console")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None, -1))
        self.TR_TC.headerItem().setText(0, QtWidgets.QApplication.translate("MainWindow", "Test Cases", None, -1))
        self.TR_TC.headerItem().setText(1, QtWidgets.QApplication.translate("MainWindow", "Result", None, -1))
        __sortingEnabled = self.TR_TC.isSortingEnabled()
        self.TR_TC.setSortingEnabled(False)
        self.TR_TC.topLevelItem(0).setText(0, QtWidgets.QApplication.translate("MainWindow", "Power On/Off Test", None, -1))
        self.TR_TC.topLevelItem(1).setText(0, QtWidgets.QApplication.translate("MainWindow", "Boot Loader Booting Test", None, -1))
        self.TR_TC.topLevelItem(2).setText(0, QtWidgets.QApplication.translate("MainWindow", "EEPROM Read/Write Test", None, -1))
        self.TR_TC.topLevelItem(3).setText(0, QtWidgets.QApplication.translate("MainWindow", "Diagnostic Test", None, -1))
        self.TR_TC.topLevelItem(4).setText(0, QtWidgets.QApplication.translate("MainWindow", "OS Image Download Test", None, -1))
        self.TR_TC.topLevelItem(5).setText(0, QtWidgets.QApplication.translate("MainWindow", "OS Booting Test", None, -1))
        self.TR_TC.topLevelItem(6).setText(0, QtWidgets.QApplication.translate("MainWindow", "RTC Operating Test", None, -1))
        self.TR_TC.topLevelItem(7).setText(0, QtWidgets.QApplication.translate("MainWindow", "Watchdog Test", None, -1))
        self.TR_TC.setSortingEnabled(__sortingEnabled)
        self.PB_StartTest.setText(QtWidgets.QApplication.translate("MainWindow", "Start Test", None, -1))
        self.CB_EEPROM.setText(QtWidgets.QApplication.translate("MainWindow", "EEPROM Read/Write Test", None, -1))
        self.CB_RTCOp.setText(QtWidgets.QApplication.translate("MainWindow", "RTC Operating Test", None, -1))
        self.LE_BLBRE.setText(QtWidgets.QApplication.translate("MainWindow", "20", None, -1))
        self.CB_Diag.setText(QtWidgets.QApplication.translate("MainWindow", "Diagnostic Test", None, -1))
        self.LE_DiagRE.setText(QtWidgets.QApplication.translate("MainWindow", "20", None, -1))
        self.CB_BLBooting.setText(QtWidgets.QApplication.translate("MainWindow", "Boot Loader Booting Test", None, -1))
        self.CB_WDOp.setText(QtWidgets.QApplication.translate("MainWindow", "Watchdog Operatiog Test", None, -1))
        self.LE_EEPROMRE.setText(QtWidgets.QApplication.translate("MainWindow", "20", None, -1))
        self.CB_OsImgDn.setText(QtWidgets.QApplication.translate("MainWindow", "OS Image Download Test", None, -1))
        self.LE_PowRE.setText(QtWidgets.QApplication.translate("MainWindow", "20", None, -1))
        self.CB_PwrOnOff.setText(QtWidgets.QApplication.translate("MainWindow", "Power On/Off Test", None, -1))
        self.CB_OSBooting.setText(QtWidgets.QApplication.translate("MainWindow", "OS Booting Test", None, -1))
        self.LE_WDRE.setText(QtWidgets.QApplication.translate("MainWindow", "20", None, -1))
        self.LE_RTCRE.setText(QtWidgets.QApplication.translate("MainWindow", "20", None, -1))
        self.LE_OSDNRE.setText(QtWidgets.QApplication.translate("MainWindow", "20", None, -1))
        self.LE_OSBootRE.setText(QtWidgets.QApplication.translate("MainWindow", "20", None, -1))
        self.PB_PASS.setText(QtWidgets.QApplication.translate("MainWindow", "PASS", None, -1))
        self.PB_FAIL.setText(QtWidgets.QApplication.translate("MainWindow", "FAIL", None, -1))
        self.PTE_what.setPlainText(QtWidgets.QApplication.translate("MainWindow", "What is this?", None, -1))
        self.RB_Console.setText(QtWidgets.QApplication.translate("MainWindow", "Console", None, -1))

