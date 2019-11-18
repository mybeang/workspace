import pdb
import re
import wr_table
import os
from pprint import pprint as pp

ok_msg = """
************ input string ************
line = {}, indents = {}
**************************************
{}
************ output string ***********
{}
"""

err_msg = """
************ input string ************
{}
**************************************
Cannot change table in line {} automatically
Please change manually
**************************************
"""

class ChangeTableInTP(object):
    def __init__(self, old_file):
        self.old_file = old_file
        lof = open(old_file, 'r+') # readlines
        rof = open(old_file, 'r+') # read
        self.raw_string_list = lof.readlines()
        self.raw_m_string = rof.read()
        lof.close()
        rof.close()
        self.data_list = list()
        self.err_tables = list()
        self.change()

    def _find_table_index(self):
        table_index_list = list()
        for i, raw_string in enumerate(self.raw_string_list):
            if re.findall(r"\+==", raw_string.strip("\n")):
                pass
            elif re.findall(r"===", raw_string.strip("\n")):
                table_index_list.append(i)
        table_index_list = table_index_list[1:]
        table_index_list = [table_index_list[n:n + 3] for n in range(0, len(table_index_list), 3)]
        return table_index_list

    def _post_processing(self, start_index, end_index):
        without_pp_string_list = list()
        data_string_list = list()
        header_len = len(self.raw_string_list[start_index].strip())
        for i in range(start_index, end_index):
            p_processing = self.raw_string_list[i].strip()
            if header_len > len(p_processing):
                p_processing = p_processing + ' ' * (header_len - len(p_processing))
            data_string_list.append(p_processing)
            without_pp_string_list.append(self.raw_string_list[i])
        return data_string_list, without_pp_string_list

    def change(self):
        for i in self._find_table_index():
            start_index = i[0]
            end_index = i[2] + 1
            indents = self.raw_string_list[start_index].index("===")
            ds_list, nps_list = self._post_processing(start_index, end_index)
            without_pp_string = ''.join(nps_list)
            data_string = '\n'.join(ds_list)
            try:
                table = wr_table.Table(data_string, wr_table.r_dialect)
                print_string = table.to_string()
                self.raw_m_string = self.raw_m_string.replace(
                    without_pp_string,
                    ''.join(table.to_list(' ' * indents, '\n'))
                )
            except:
                self.err_tables.append(err_msg.format(data_string, start_index + 1))
            else:

                self.data_list.append(ok_msg.format(
                    start_index + 1, indents, data_string, print_string
                ))

    def screen_out(self):
        print("**** Filname: {} ****".format(self.old_file))
        for i in self.data_list:
            print(i)
        for i in self.err_tables:
            print(i)

    def to_file(self, filename):
        nf = open(filename, 'w+')
        nf.write(self.raw_m_string)
        nf.close()
        for i in self.err_tables:
            print(i)

"""
if __name__=="__main__":
    # Switch
    root_path = "/root/workspace/ytest/YTest/TC/"
    dir_list = ['IpMulticast', 'IpProtocol', 'L2', 'QoS', 'Security', 'NetworkMgmt', 'PON', 'QinQ', 'SystemMgmt', 'TR247']
    for dir in dir_list:
        full_path = "{}{}".format(root_path, dir)
        file_list = os.listdir(full_path)
        for file in file_list:
            if file != '__init__.py':
                print("Change file: {}/{}".format(full_path, file))
                new_filename = "{}_new.py".format(file[:-3])
                kk = ChangeTableInTP("{}/{}".format(full_path, file))
                kk.to_file("{}/{}".format(full_path, new_filename))
    # Fiberlan
    root_path = "/root/workspace/ytest/YTest/TC/FiberLan/"
    dir_list = ['IpMulticast', 'L2', 'PE', 'QoS', 'Security']
    for dir in dir_list:
        full_path = "{}{}".format(root_path, dir)
        file_list = os.listdir(full_path)
        for file in file_list:
            if file != '__init__.py':
                print("Change file: {}/{}".format(full_path, file))
                new_filename = "{}_new.py".format(file[:-3])
                kk = ChangeTableInTP("{}/{}".format(full_path, file))
                kk.to_file("{}/{}".format(full_path, new_filename))
"""
if __name__=="__main__":
    kk = ChangeTableInTP("{}/{}".format('.', 'example.txt'))
    kk.screen_out()
