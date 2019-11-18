import asyncio
import logging, sys, time
from popup_test.popup_main import Ui_MainWindow
from PySide2 import QtWidgets, QtCore, QtGui


def popup_msg(msg, level=0):
    """
    :param msg: Message
    :param level: 0 == 'Info", 1 == 'Warning", 2 == 'Critical'
    """
    #logging.debug("func: popup_msg({}, {})".format(msg, level))

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


class MainWD(Ui_MainWindow):
    def __init__(self):
        self.times = 1

    def print_1(self):
        msg = "hello %d" % self.times
        popup_msg(msg)
        self.TE_1.append(msg)
        self.times += 1

    def print_2(self):
        msg = "what? %d" % self.times
        popup_msg(msg)
        self.TE_2.append(msg)
        self.times += 1


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
    ui.PB_1.clicked.connect(ui.print_1)
    ui.PB_2.clicked.connect(ui.print_2)

    win.show()
    sys.exit(app.exec_())