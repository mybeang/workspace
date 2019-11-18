import logging

from PySide2 import QtWidgets

def popup_msg(msg, level=0):
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
    return True

if __name__=="__main__":

    for i in range(10):
        popup_msg(i)