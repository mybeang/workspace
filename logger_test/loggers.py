from pathlib2 import Path
import logging
import sys


class LogCollector(object):
    def __init__(self):
        self.loggers = []

    def add_logger(self, name, log_level, log_fmt, filename):
        logger = logging.getLogger(name=name)
        logger.setLevel(log_level)
        formatter = logging.Formatter(log_fmt)
        FileHandler = logging.FileHandler(filename)
        FileHandler.setFormatter(formatter)
        logger.addHandler(FileHandler)
        self.loggers.append(logger)

    def info(self, text):
        for log in self.loggers:
            log.info(text)

    def debug(self, text):
        for log in self.loggers:
            log.debug(text)


if __name__=="__main__":
    d_file = str(Path(__file__).parent.joinpath('debug_log.txt'))
    d_logging_fmt = '%(asctime)-15s %(levelname)-7s {%(module)s:%(lineno)d} %(message)s'

    i_file = str(Path(__file__).parent.joinpath('info_log.txt'))
    i_logging_fmt = '%(asctime)-15s %(message)s'

    logcol = LogCollector()
    logcol.add_logger("INFO", logging.INFO, i_logging_fmt, i_file)
    logcol.add_logger(None, logging.DEBUG, d_logging_fmt, d_file)

    logging.info("ROOT LOGGER LOG")
    logcol.info("INFO LEVEL TEST")
    logcol.debug("DEBUG LEVEL TEST")