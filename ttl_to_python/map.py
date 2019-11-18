import time


def sendln(text):
    if len(text.split("'")) > 3:
        pass
    else:
        print(text.replace("'", ""))


def mpause(text):
    time.sleep(int(text.spript()) / 1000)


def pause(text):
    time.sleep(int(text.spript()))


def int2str(text):
    _int = text.split(" ")[1]
    return str(_int)


func_map = {
    'sendln': sendln,
    'mpause': mpause,
    'puase': pause,
    'int2str': int2str
}