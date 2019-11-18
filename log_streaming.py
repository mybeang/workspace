import logging
import multiprocessing as mp
from logging import handlers
import time


def logs(inerval):
    log_string = [
                     'Hi',
                     'This is my log string for my test.',
                     'This is needed the queue'
                 ] * 10 + ["end"]
    for l in log_string:
        time.sleep(inerval)
        yield l

def print_log(q):
    logging_fmt = '%(levelname)-7s %(message)s'
    logger = logging.getLogger()
    h = handlers.QueueHandler(q)
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter(logging_fmt)
    h.setFormatter(formatter)
    logger.addHandler(h)
    log_text = logs(1)
    while True:
        try:
            text = next(log_text)
        except:
            break
        else:
            logging.info(text)
