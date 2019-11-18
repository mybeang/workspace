import logging


class TestData(object):
    def __init__(self, values):
        if isinstance(values, list):
            self.__values = values
        elif isinstance(values, dict):
            self.__values = list(values.values())
        self._divide_data()

    def _divide_data(self):
        self.tc_data = self.__values[:16]
        self.session_data = self.__values[16:22]
        self.pcm = self.__values[22:28]

    def gen_tc_data(self):
        tc_name = ["Evt.test_test00{}".format(i) for i in range(1, 9)]
        tc_flags = self.tc_data[:8]
        tc_repeats = [i if i is not None else 0 for i in self.tc_data[8:]]
        tc_dict = {'test_list': []}
        for f, n, r in zip(tc_flags, tc_name, tc_repeats):
            if f:
                tc_dict['test_list'].append({"name": n, "repeat": int(r)})
        return tc_dict, tc_flags

    def gen_session_data(self):
        if self.session_data[0]:
            data = {
                "Connection": {
                    "serial": {
                        "port": self.session_data[2],
                        "baudrate": self.session_data[3]
                    }
                }
            }
        else:
            data = {
                "Connection": {
                    "tcp_ip": {
                        "type": "telent",
                        "ip": self.session_data[4],
                        "port": self.session_data[5]
                    }
                }
            }
        return data

    def gen_pcm_data(self):
        if self.pcm[0]:
            _type = "APC"
            _ip = self.pcm[2]
            _port = self.pcm[3]
        else:
            _type = "V100"
            _ip = self.pcm[4]
            _port = self.pcm[5]
        data = {
            "type": _type,
            "ip": _ip,
            "port": _port
        }
        return data