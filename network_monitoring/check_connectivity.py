import datetime
import time
import socket
import logging
import ping
import logstash
import json
import multiprocessing as mp


SERVER_LIST = {
    "yjob1": "10.55.195.22",
    "yjob2": "10.55.195.18",
    "gw_195": "10.55.195.254",
    "gw_194": "10.55.194.254",
    "gw_192": "10.55.192.254",
    "apple": "10.55.2.202",
    "CON109": "10.55.192.109",
    "yfcobra": "10.55.195.20",
    "yfserv": "10.55.195.16",
    "rtg_serv_100": "10.55.194.100",
    "rtg_serv_101": "10.55.194.101",
    "rtg_serv_102": "10.55.194.102"
}


class Buf(object):
    def __init__(self):
        self.buf_list = list()

    def qsize(self):
        return len(self.buf_list)

    def put(self, data):
        self.buf_list.append(data)

    def get(self):
        return self.buf_list.pop(0)

    def clear(self):
        self.buf_list = list()


def ping_task(data, timeout=2, interval=1, psize=64):
    dest, q = data
    msg_head = 'ping {}; send to {} ... '.format(SERVER_LIST[dest], dest)
    while True:
        time.sleep(interval)
        try:
            delay = ping.do_one(SERVER_LIST[dest], timeout, psize)
        except socket.gaierror, e:
            print('failed. (socket error: "%s")' % e[1])
        else:
            if delay:
                delay = delay * 1000
                print('{}get ping in {} ms'.format(msg_head, delay))
                result = (dest, SERVER_LIST[dest], 'ok', delay)
            else:
                print('{}failed.(timeout within {} sec.)'.format(msg_head, timeout))
                result = (dest, SERVER_LIST[dest], 'fail', 0)
        finally:
            send_data_to_es(result)


def send_data_to_es(result, logstash_ip="10.55.195.21", logstash_port=50005):
    if result:
        data_dict = dict(dest=result[0], ip_addr=result[1], result=result[2], delay=result[3])
        logger = logging.getLogger('logstash-logger')
        if len(logger.handlers) == 0:
            logger.setLevel(logging.DEBUG)
            formatter = logging.Formatter("%(message)s")
            lh = logstash.LogstashHandler(logstash_ip, logstash_port, version=1)
            lh.setFormatter(formatter)
            logger.addHandler(lh)
        logger.info(json.dumps(data_dict))


if __name__=="__main__":
    q = Buf()
    p = mp.Pool(len(SERVER_LIST.keys()))
    p.map(ping_task, [(server, q) for server in SERVER_LIST.keys()])
