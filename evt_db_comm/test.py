import unittest

class TestBase(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestBase, self).__init__(*args, **kwargs)

    def test_test001(self):
        import pdb
        pdb.set_trace()
