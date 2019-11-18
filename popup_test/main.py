import asyncio
import logging, sys, time
from popup_test.popup_main import Ui_MainWindow
from PySide2 import QtWidgets, QtCore, QtGui


class Th1(QtCore.QThread):
    log = QtCore.Signal(str)
    popup = QtCore.Signal(str, int)

    def __init__(self):
        QtCore.QThread.__init__(self)

    def run(self):
        for i in range(20):
            logging.debug("Print on Terminal 1")
            self.log.emit("Print on Terminal 1")
            if i % 3 == 1:
                self.popup.emit("hello", 0)
            time.sleep(0.2)


class Th2(QtCore.QThread):
    log = QtCore.Signal(str)

    def __init__(self, popup_msg):
        QtCore.QThread.__init__(self)
        self.popup_msg = popup_msg

    def run(self):
        for i in range(20):
            logging.debug("Print on Terminal 2")
            self.log.emit("Print on Terminal 2")
            if i % 3 == 1:
                self.popup_msg("hello")
            time.sleep(0.2)


class MainWD(Ui_MainWindow):
    def __init__(self):
        self.t1 = Th1()
        self.t2 = Th2(self.popup_msg)
        self.t1.log.connect(self.print_1)
        self.t2.log.connect(self.print_2)
        self.t1.popup.connect(self.popup_msg)

    def popup_msg(self, msg, level=0):
        """
        :param msg: Message
        :param level: 0 == 'Info", 1 == 'Warning", 2 == 'Critical'
        """
        logging.debug("func: popup_msg({}, {})".format(msg, level))
        _level = [QtWidgets.QMessageBox.Information,
                  QtWidgets.QMessageBox.Warning,
                  QtWidgets.QMessageBox.Critical]
        msg_box = QtWidgets.QMessageBox()
        if level == 0:
            msg_box.setWindowTitle("INFO")
        elif level == 1:
            msg_box.setWindowTitle("WARNING")
        else:
            msg_box.setWindowTitle("CRITICAL")
        msg_box.setText(msg)
        msg_box.setIcon(_level[level])
        msg_box.exec_()
        del msg_box

    def start_1(self):
        self.t1.start()

    def start_2(self):
        self.t2.start()

    def print_1(self, string):
        self.TE_1.append(string)

    def print_2(self, string):
        self.TE_2.append(string)


if __name__=="__main__":
    logger = logging.getLogger()
    fmt = "[%(levelname)s] %(msg)s"
    log_level = logging.DEBUG
    logger.setLevel(log_level)
    hdl = logging.StreamHandler(sys.stdout)
    fmtter = logging.Formatter(fmt)
    hdl.setFormatter(fmtter)
    logger.addHandler(hdl)

    app = QtWidgets.QApplication(sys.argv)
    ui = MainWD()
    win = QtWidgets.QMainWindow()
    ui.setupUi(win)
    ui.retranslateUi(win)
    ui.PB_1.clicked.connect(ui.start_1)
    ui.PB_2.clicked.connect(ui.start_2)

    win.show()
    sys.exit(app.exec_())
