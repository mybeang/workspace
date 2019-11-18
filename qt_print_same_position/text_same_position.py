import sys, time
from PySide2 import QtCore, QtGui, QtWidgets
from qt_print_same_position.text_edit import Ui_Form


class UI(Ui_Form):
    def __init__(self):
        Ui_Form.__init__(self)
        self.cnt = 5

    def append_to_text(self):
        _text = self.lineEdit.text()
        self.textEdit.append(_text)
        self.lineEdit.clear()

    def insert_to_text(self, text=None):
        if not text:
            _text = self.lineEdit.text()
        else:
            _text = text
        cursor = self.textEdit.textCursor()
        self.textEdit.moveCursor(QtGui.QTextCursor.End, QtGui.QTextCursor.MoveAnchor)
        self.textEdit.moveCursor(QtGui.QTextCursor.StartOfLine, QtGui.QTextCursor.MoveAnchor)
        self.textEdit.moveCursor(QtGui.QTextCursor.End, QtGui.QTextCursor.KeepAnchor)
        self.textEdit.textCursor().removeSelectedText()
        self.textEdit.textCursor().deletePreviousChar()
        self.textEdit.setTextCursor(cursor)
        self.textEdit.append(_text)
        if not text:
            self.lineEdit.clear()

    def count(self):
        self.insert_to_text("Press 's' key to go to Boot Mode: %s" % str(self.cnt))
        self.cnt = self.cnt - 1
        if self.cnt < 0:
            self.cnt = 5

    def handlers(self):
        self.bt_append.clicked.connect(self.append_to_text)
        self.bt_insert.clicked.connect(self.insert_to_text)
        self.bt_count.clicked.connect(self.count)


if __name__=="__main__":
    app = QtWidgets.QApplication()
    ui = UI()
    win = QtWidgets.QMainWindow()
    ui.setupUi(win)
    ui.retranslateUi(win)
    ui.handlers()
    win.show()
    sys.exit(app.exec_())