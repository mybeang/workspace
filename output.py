import PySimpleGUI as sg
import logging
import sys
import multiprocessing as mp
import time
from logging import LogRecord

from log_streaming import print_log


logging_fmt = '%(asctime)-15s %(levelname)-7s {%(module)s:%(lineno)d} %(message)s'
logger = logging.getLogger()
logger.setLevel(logging.INFO)
formatter = logging.Formatter(logging_fmt)
stdoutHandler = logging.StreamHandler()
stdoutHandler.setFormatter(formatter)
logger.addHandler(stdoutHandler)


layout = [
    [sg.Output(size=(50, 30))],
    [sg.Input(key="_INPUT_"), sg.Submit()],
    [sg.Submit("PRINT LOG STRING")]
]


def _execute(w):
    queue = mp.Queue()
    mpp = mp.Process(target=print_log, args=(queue,))
    mpp.start()
    while True:
        if not queue.empty():
            logobj = queue.get()
        else:
            logobj = None
        if isinstance(logobj, LogRecord):
            print(logobj.msg)
            if logobj.msg == 'end':
                break
        w.Refresh()
    mpp.terminate()
    mpp.join()
    del mpp


windows = sg.Window("TEST").Layout(layout)
mp.freeze_support()
while True:
    event, value = windows.Read()
    if event is None:
        break
    if event == "Submit":
        logging.info(value["_INPUT_"])
        #print(value["_INPUT_"])
    if event == "PRINT LOG STRING":
        _execute(windows)