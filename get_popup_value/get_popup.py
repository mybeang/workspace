from PySide2 import QtWidgets, QtGui, QtCore
from get_popup_value.main_window import Ui_Form
import sys



class UI(Ui_Form):
    def __init__(self):
        self.win = QtWidgets.QMainWindow()
        self.setupUi(self.win)
        self.retranslateUi(self.win)
        self.bt_start.clicked.connect(self.show)

    def popup_msg(self, msg, level=0):
        """
        :param msg: Message
        :param level: 0 == 'Info", 1 == 'Warning", 2 == 'Critical'
        """
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
        # win_icon_path = str(self.get_iudata_path().joinpath("main_window_icon.png"))
        # qimg = QtGui.QPixmap(win_icon_path)
        # msg_box.setWindowIcon(qimg)
        msg_box.setText(msg)
        msg_box.setIcon(_level[level])
        msg_box.exec_()
        return True

    def show(self):
        string = """
+----+------------+
|    | Cabling    |
+====+============+
|  0 | Lan1 <-> 1 |
+----+------------+
|  1 | 3 <-> 4    |
+----+------------+
|  2 | 5 <-> 6    |
+----+------------+
|  3 | 2 <-> Lan2 |
+----+------------+
        """
        self.popup_msg("%s" % (string))

        for i in range(100):
            n = i + 1
            repeat_string = "%d " % n * n
            self.terminal.append("times = %s" % (repeat_string))
            #if i == 10:
            #    self.popup_msg("Please OK")


if __name__=="__main__":
    app = QtWidgets.QApplication()
    ui = UI()
    ui.win.show()

    sys.exit(app.exec_())