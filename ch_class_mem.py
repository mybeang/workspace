class A(object):
    b = "hwat"
    def __init__(self):
        self.a = 'abc'

    def pp(self):
        pass

a = A()
print(dir(a))
print(hasattr(a, "a"))
print(hasattr(a, "b"))
print(hasattr(a, "pp"))