from texttables import Dialect
from texttables.fixed import DictReader
from texttables.fixed   import writer
from collections import OrderedDict

import re, pdb

class r_dialect(Dialect):
    header_delimiter = '='
    corner_border = ' '
    top_border = '='
    bottom_border = '='
    cell_delimiter = ' '

class w_dialect(Dialect):
    header_delimiter = '='
    row_delimiter = '-'
    top_border = '-'
    bottom_border = '-'
    left_border = '|'
    cell_delimiter = '|'
    right_border = '|'
    corner_border = '+'


class StoreList(object):
    def __init__(self):
        self._data_list = list()

    def write(self, data):
        self._data_list.append(data)

    def to_string(self):
        return ''.join(self._data_list)


class Table(object):
    def __init__(self, data, dialect_cls):
        self.data = data
        self.dialect_cls = dialect_cls

    def to_dict_list(self):
        return [row for row in DictReader(self.data.splitlines(),
                                          self.extract_hd_len(),
                                          dialect=self.dialect_cls)]

    def to_odict_list(self):
        return self.dl_to_odl(self.to_dict_list())

    def extract_hd_len(self):
        hd_list = list()
        for item in re.split('\s|\n', self.data):
            if not re.findall(r'\w', item):
                hd_list.append(item)
            else:
                break
        for i, item in enumerate(hd_list):
            hd_list[i] = len(item)
        return hd_list

    def extract_hd_list(self):
        hd_list = []
        hd_string = self.data.split("\n")[1]
        index_list = map(lambda x: hd_string.index(str(x)), self.to_dict_list()[0].keys())
        index_list.sort()
        for i, j in zip(index_list, self.extract_hd_len()):
            hd_list.append(hd_string[i: i + j].strip())
        return hd_list

    def dl_to_odl(self, dict_list):
        result_list = list()
        for dict_data in dict_list:
            result_list.append(self.dict_to_orderedict(dict_data))
        return result_list

    def dict_to_orderedict(self, dict_data):
        list_of_tuples = [(key, dict_data[key]) for key in self.extract_hd_list()]
        return OrderedDict(list_of_tuples)

    def to_string(self):
        sst = StoreList()
        w = writer(sst, self.extract_hd_len(), dialect=w_dialect)
        w.writetop()
        w.writeheader(tuple(self.extract_hd_list()))
        result_list = list()
        for item in self.to_odict_list():
            result_list.append(tuple(item.values()))
        w.writerows(result_list)
        w.writebottom()
        return sst.to_string()

    def to_list(self, start_char='', end_char=''):
        _temp = list()
        for i in self.to_string().split("\n"):
            _temp.append(start_char + str(i) + end_char)
        return _temp

def example():
    data0 = (
        "===== ===== =======\n"
        "A     B     A and B\n"
        "===== ===== =======\n"
        "False False False  \n"
        "True  False False  \n"
        "False True  False  \n"
        "True  True  True   \n"
        "===== ===== =======\n"
    ).strip()

    data1 = (
        "======= ====== ==========\n"
        "Port    Expect Not-Expect\n"
        "======= ====== ==========\n"
        "port[1] flow0            \n"
        "port[2] flow1            \n"
        "======= ====== ==========\n"
    ).strip()

    data2 = (
        "===== ======================= ==== ============= ====== =======\n"
        "Flow  Send Port               Type DA            SA     Vlan   \n"
        "===== ======================= ==== ============= ====== =======\n"
        "flow0 dut[0].olt[0].onu[0][0] tag  Broadcast     mac[0] vlan[0]\n"
        "flow1 dut[0].olt[0].onu[0][0] tag  Unknown Ucast mac[1] vlan[0]\n"
        "flow2 dut[0][0]               tag  Broadcast     mac[2] vlan[0]\n"
        "flow3 dut[0][0]               tag  Unknown Ucast mac[3] vlan[0]\n"
        "===== ======================= ==== ============= ====== =======\n"
    ).strip()

    data3 = (
        "======= ======= ======= ====== ======= ===== ========= ========\n"
        "Flow    Send    Type    SA     VID     SIP   DIP       Group   \n"
        "======= ======= ======= ====== ======= ===== ========= ========\n"
        "flow[0] port[0] igmp.GQ mac[0] vlan[0] ip[0] 224.0.0.1         \n"
        "flow[1] port[0] mcast   mac[0] vlan[0] ip[0] group[0]          \n"
        "flow[2] port[0] mcast   mac[0] vlan[0] ip[0] group[1]          \n"
        "flow[3] port[1] igmp.MR mac[1] vlan[0] ip[1] group[0]  group[0]\n"
        "flow[4] port[1] igmp.MR mac[1] vlan[0] ip[1] group[1]  group[1]\n"
        "flow[5] port[2] igmp.MR mac[2] vlan[0] ip[2] group[0]  group[0]\n"
        "flow[6] port[2] igmp.MR mac[2] vlan[0] ip[2] group[1]  group[1]\n"
        "flow[7] port[1] igmp.LG mac[1] vlan[0] ip[1] 224.0.0.2 group[0]\n"
        "======= ======= ======= ====== ======= ===== ========= ========\n"
    ).strip()

    table = [Table(data0, r_dialect),
             Table(data1, r_dialect),
             Table(data2, r_dialect),
             Table(data3, r_dialect)]
    data_list = [data0, data1, data2, data3]
    for i in zip(table, data_list):
        print("*" * 10 + " Before " + "*" * 10)
        print(i[1])
        print("\n")
        print("*" * 10 + " After " + "*" * 10)
        print(i[0].to_string())
        print("\n\n")

if __name__=="__main__":
    example()
