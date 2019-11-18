from PySide2 import QtCore
from time import sleep

class LoggingApp(object):
    def __init__(self):
        pass

    def set_queue(self, queue):
        self.queue = queue


class GUILoggingApp(QtCore.QThread, LoggingApp):
    job_sig = QtCore.Signal(str)

    def __init__(self, terminal):
        QtCore.QThread.__init__(self)
        self.terminate = terminal

    def set_queue(self, queue):
        self.queue = queue

    def run(self):
        self.print_out()

    def string_out(self, string):
        if self.queue.full():
            self.queue.get()
        self.queue.put(string)

    def print_out(self):
        while True:
            sleep(0.1)
            if not self.queue.empty():
                for _ in range(self.queue.qsize()):
                    string = self.queue.get()
                    print(string)
                    self.job_sig.emit(string)
