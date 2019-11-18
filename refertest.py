import pdb
import gc
import pprint

class Example(object):
    pass


ex1 = Example()

a = [ex1, 1, 2, 3]
b = [ex1]
c = a + b

for i in gc.get_referrers(ex1):
    if isinstance(i, dict):
        pprint.pprint(i)