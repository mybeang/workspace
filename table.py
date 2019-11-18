class TableBase(object):
    def __init__(self, raw_data, data_range):
        self.raw_data = raw_data
        self.data_range = data_range

    def _split(self):
        if self.data_range[1] < 0: # negative case
            return split_row_data(self.raw_data, row_range=(self.data_range[0], None))[:self.data_range[1]]
        return split_row_data(self.raw_data, row_range=self.data_range)

    def _strip(self, raw):
        return [row.strip() for row in raw]

    def _pre_process(self):
        return self._strip(self._split())

    @abc.abstractmethod
    def parse(self):
        pass