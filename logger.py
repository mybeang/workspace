import logging
import sys



def set_logger(verbose=False):
    if not verbose:
        log_level = logging.INFO
        logging_fmt = '%(asctime)-15s %(levelname)-7s %(message)s'
    else:
        log_level = logging.DEBUG
        logging_fmt = '%(asctime)-15s %(levelname)-7s {%(module)s:%(lineno)d} %(message)s'

    logger = logging.getLogger()
    logger.setLevel(log_level)
    formatter = logging.Formatter(logging_fmt)
    stdoutHandler = logging.StreamHandler(sys.stdout)
    stdoutHandler.setFormatter(formatter)
    logger.addHandler(stdoutHandler)



    return logger, logging_fmt, log_level
