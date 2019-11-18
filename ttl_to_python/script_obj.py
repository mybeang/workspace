from ttl_to_python.map import func_map


class Script(object):
    def __init__(self):
        pass

    def open_ttl_file(self, filename):
        with open(filename, 'r') as f:
            self.text_line = f.readlines()

    def add_control(self, text):
        pass

    def add_loop(self, text):
        pass

    def add_attr(self, text):
        pass

    def anaysis(self, text):
        if 'for' in text or 'while' in text:
            self.add_loop(text)
        elif 'if' in text:
            self.add_control(text)
        elif '=' in text:
            self.add_attr(text)
        else:
            func


