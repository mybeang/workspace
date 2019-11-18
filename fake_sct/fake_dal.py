from multiprocessing import Queue
from time import sleep
from pathlib import Path
from random import choice


OPENFILE = Path(__file__).parent.joinpath("conf.txt")


sec = choice(list(range(1, 100)))


class FakeDal(object):
    def __init__(self):
        self.q = Queue(maxsize=10)

    def read_file(self):
        with open(OPENFILE, "r") as f:
            strings = f.readlines()
        self.q.put("Fake this!!!")
        sleep(10)
        for string in strings:
            if self.q.full():
                self.q.get()
            self.q.put(string)
            sleep(sec * 0.001)
        self.q.put("Fake this really!!!")
        sleep(20)
        self.q.put("Bye ~~")
