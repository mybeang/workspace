import pdb

class ColorDB(object):
    GRAY = '\033[1;30m'
    RED = '\033[1;31m'
    GREEN =  '\033[1;32m'
    YELLOW = '\033[1;33m'
    BLUE = '\033[1;34m'
    MAGNETA = '\033[1;35m'
    CYAN = '\033[1;36m'
    DEFAULT = '\033[1;m'
    HRED = '\033[1;41m'
    HGREEN = '\033[1;42m'
    HYELLOW = '\033[1;43m'
    HBLUE = '\033[1;44m'
    HMAGNETA = '\033[1;45m'
    HCYAN = '\033[1;46m'
    HGRAY = '\033[1;47m'


def cprint(msg, color='default'):
    cdb =  ColorDB()
    try:
        _front = eval("cdb.{}".format(color.upper()))
        _end = ColorDB.DEFAULT
        print("{}{}{}".format(_front, msg, _end))
    except AttributeError:
        raise
    finally:
        del cdb


if __name__=="__main__":
    color_lists = ['red', 'green', 'yellow', 'blue', 'magneta', 'cyan', 'default',
                   'hred', 'hgreen', 'hyellow', 'hblue', 'hmagneta', 'hcyan', 'hgray',
                   'error']
    for color in color_lists:
        cprint("Color is = {}".format(color), color)
