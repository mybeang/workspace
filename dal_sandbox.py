from textfsm import TextFSM

from io import StringIO
from tabulate import tabulate
from pathlib2 import Path
from dal.factory.manufacturer import Manufacturer as mf
import logging
import time
import threading
import sys
from tabulate import tabulate


class App(object):
    def __init__(self, log_queue):
        self.run_flag = True
        self.log_queue = log_queue
        self.print_th = threading.Thread(target=self.screen_on, args=(self.log_queue,))

    def screen_on(self, log_queue):
        while self.run_flag:
            time.sleep(0.1)
            if not log_queue.empty():
                for _ in range(log_queue.qsize()):
                    print("{}".format(log_queue.get()), end="")
                    sys.stdout.flush()
                    """
                    logging.info("{}".format(queue.get()))
                    """

    def start(self):
        if hasattr(self, "print_th"):
            self.print_th.start()
        else:
            self.run_flag = True
            self.print_th = threading.Thread(target=self.screen_on, args=(self.log_queue,))
            self.print_th.start()

    def stop(self):
        self.run_flag = False

        self.print_th.join()
        del self.print_th


logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
stdoutHandler = logging.StreamHandler(sys.stdout)
logger.addHandler(stdoutHandler)

SPEC_PATH = Path(__file__).parent.parent.joinpath("data").joinpath("dut_spec")

session_info = {
    'proto': 'telnet',
    'host': "10.55.195.144",
    'user': "admin",
    'passwd': ""
}

dev = mf("M1100").manufacture()
dev.create_session(**session_info)

##print_app = App(dev.session[0].queue)
#print_app.start()
#time.sleep(1)
dev.session[0].send_command("", ignore_match=True)
dev.session[0].send_command("admin", ignore_match=True)
dev.session[0].send_command("", ignore_match=True)
time.sleep(1)
dev.session[0].send_command("enable", expect=['word:'])
try_cnt = 0
passwd = "ektks123"
while try_cnt < 3:
    print("{}:{}".format(try_cnt, passwd))
    _, raw = dev.session[0].send_command(passwd + "\r\r", ignore_match=True)
    if "% Bad" in raw:
        break
    elif "#" in raw:
        break
    try_cnt += 1
#dev.session[0].enable()
