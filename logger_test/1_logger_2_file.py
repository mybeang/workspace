import logging
from pathlib2 import Path

d_file = str(Path(__file__).parent.joinpath('debug_log.txt'))
d_logging_fmt = '%(asctime)-15s %(levelname)-7s {%(module)s:%(lineno)d} %(message)s'

i_file = str(Path(__file__).parent.joinpath('info_log.txt'))
i_logging_fmt = '%(asctime)-15s %(message)s'

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter(logging_fmt)
FileHandler = logging.FileHandler(filename)
FileHandler.setFormatter(formatter)
logger.addHandler(FileHandler)