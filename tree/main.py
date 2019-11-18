import sys, time
from PySide2 import QtCore, QtWidgets, QtGui
from tree.main_win import Ui_MainWindow


class TreePrac1(Ui_MainWindow):
    def __init__(self, win):
        super(Ui_MainWindow, self).__init__()
        self.setupUi(win)
        self.retranslateUi(win)
        tcs = ['Power On/Off Test',
               'Boot Loader Booting Test',
               'EEPROM Read/Write Test',
               'Dignostic Test',
               'OS Image Donwload Test',
               'OS Booting Test',
               'RTC Operating Test',
               'Watchdog Test'
               ]

        self.PB_StartTest.clicked.connect(self.hdr_start_test)
        self.PB_PASS.clicked.connect(self.hdr_pass)
        self.PB_FAIL.clicked.connect(self.hdr_fail)

    def get_tcs_state(self):
        check_list = [
            self.CB_PwrOnOff.checkState(),
            self.CB_BLBooting.checkState(),
            self.CB_EEPROM.checkState(),
            self.CB_Diag.checkState(),
            self.CB_OsImgDn.checkState(),
            self.CB_OSBooting.checkState(),
            self.CB_RTCOp.checkState(),
            self.CB_WDOp.checkState(),
        ]
        enable_list = list()
        for check in check_list:
            if check == QtCore.Qt.CheckState.Checked:
                enable_list.append(True)
            else:
                enable_list.append(False)
        return enable_list

    def get_repeats(self):
        return [
            int(self.LE_PowRE.text()),
            int(self.LE_BLBRE.text()),
            int(self.LE_EEPROMRE.text()),
            int(self.LE_DiagRE.text()),
            int(self.LE_DiagRE.text()),
            int(self.LE_OSDNRE.text()),
            int(self.LE_OSBootRE.text()),
            int(self.LE_RTCRE.text()),
            int(self.LE_WDRE.text())
        ]

    def remove_all_children(self, tl):
        """
        Your example doesn't work because you are trying to remove items while iterating over them.
        After each item is removed, the others will move down. So once the half-way point is passed,
        the loop will start giving invalid indexes.

        You can easily fix this by removing the items in reverse order.
        That way, after each item is removed, the other items will stay where they are and
        all the indexes will remain valid:
        """
        print("before: {}: {}".format(tl, tl.childCount()))
        for i in reversed(range(tl.childCount())):
            tl.removeChild(tl.child(i))
        print("After: {}: {}".format(tl, tl.childCount()))

    def update_children(self):
        enable_list = self.get_tcs_state()
        print("enable list = {}".format(enable_list))
        repeat_list = self.get_repeats()
        print("repeat list = {}".format(repeat_list))
        tc_datas = zip(enable_list, repeat_list)
        for index, tc_data in enumerate(tc_datas):
            enable, repeat = tc_data
            tl = self.TR_TC.topLevelItem(index)
            self.remove_all_children(tl)
            if enable:
                for i in range(repeat):
                    child = QtWidgets.QTreeWidgetItem(["test_%.3d" % (i + 1), ""])
                    child.setFlags(child.flags() | QtCore.Qt.ItemIsTristate | QtCore.Qt.ItemIsUserCheckable)
                    child.setCheckState(0, QtCore.Qt.Unchecked)
                    tl.addChild(child)

    def hdr_start_test(self):
        self.update_children()
        self.PTE_what.appendPlainText("whatthe\n\n\n")
        print(self.PTE_what.toPlainText())
        print(self.RB_Console.isChecked())

    def hdr_pass(self):
        try:
            self.TR_TC.topLevelItem(0).child(0).setText(1, "PASS")
            self.TR_TC.topLevelItem(0).child(0).setTextColor(1, "BLUE")
            print(self.TR_TC.topLevelItem(0).child(0).checkState(0))
        except:
            pass

    def hdr_fail(self):
        try:
            self.TR_TC.topLevelItem(0).child(0).setText(1, "FAIL")
            self.TR_TC.topLevelItem(0).child(0).setTextColor(1, "FAIL")
        except:
            pass


if __name__=="__main__":
    app = QtWidgets.QApplication()
    win = QtWidgets.QMainWindow()
    ui = TreePrac1(win)
    win.show()
    sys.exit(app.exec_())