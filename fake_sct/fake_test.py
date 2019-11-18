from fake_sct.fake_dal import FakeDal
from PySide2 import QtCore
from time import sleep

class FakeTest(object):
    def __init__(self, log_app):
        self.dal = FakeDal()
        self.log_app = log_app

    def run_test(self):
        self.log_app.set_queue(self.dal.q)
        self.log_app.string_out("++++ Start Test ++++")
        self.log_app.start()
        self.dal.read_file()
        self.log_app.string_out("++++ Finish Test ++++")


class BufferTest(object):
    def __init__(self, log_app):
        self.dal = FakeDal()
        self.log_app = log_app

    def run_test(self):
        self.log_app.set_queue(self.dal.q)
        self.log_app.string_out("++++ Start Test ++++")
        self.log_app.start()
        for i in range(1000000):
            sleep(0.05)
            self.log_app.string_out("{}".format(i+1))
        self.log_app.string_out("++++ Finish Test ++++")


class TestThread(QtCore.QThread):
    def __init__(self, test_obj, ui_obj):
        QtCore.QThread.__init__(self)
        self.test = test_obj
        self.led = ui_obj.status_display

    def run(self):
        self.led.start()
        self.test.run_test()
        self.led.finish()
