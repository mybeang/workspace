import pdb
import multiprocessing as mp
from scapy.all import *


class _SendPktProcess(mp.Process):
    def __init__(self, pkt, iface, q, inter=1, verbose=0, *args, **kwargs):
        super(_SendPktProcess, self).__init__()
        self.pkt = pkt
        self.q = q
        self.daemon = True
        self.inter = inter
        self.verbose = verbose
        if iface == None:
            self.s = conf.L3socket(*args, **kwargs)
        else:
            self.s = conf.L2socket(iface=iface, *args, **kwargs)

    def run(self, *args, **kwargs):
        self.__gen_pkt()

    def __gen_pkt(self):
        if isinstance(self.pkt[1], str):
            _pkt = conf.raw_layer(load=self.pkt[1])
        if not isinstance(self.pkt, str):
            _pkt = SetGen(self.pkt)
        while True:
            for p in _pkt:
                self.q.put(p)
                if self.verbose:
                    os.write(1, b".")
                self.s.send(p)
                time.sleep(self.inter)


class SendPktManager(object):
    """
    Send Packet Manager.

    This module can send the packet without the finishing.
    You can terminate any time after start to send the packets.
    Refer to the test.py for using.

    Simple Usage:
       >>> pkt = Ether () / IP () # the packet format should be kept the scapy.
       >>> spm = SendPktManager()
       >>> spm.add_pkt(td.pkt[0], 'lo')
       >>> spm.start_traffic()
       >>> spm.stop_traffic()
       >>> pkt_list = spm.get_packets()
       >>> del spm
    """
    def __init__(self, verbose=0):
        self.queue = mp.Queue()
        self._sp_task_list = list()
        self.verbose = verbose

    def add_pkt(self, pkt, iface, inter=1):
        """
        Add the packet data for sending.
        Added the packet data is managed as list.

        :param pkt: scapy packets. can use list type.
        :param iface: interface name.
        :param inter: interval between sending packets.
        """
        self._sp_task_list.append(
            [_SendPktProcess(pkt, iface, self.queue, inter, self.verbose), True]
        )

    def enable_pkt(self, index=None):
        """
        Enable the packet data.
        If you want to send the packets, you should enable the packet data.
        Default is enable.

        :param index: the packet data list's index number.
        """
        if index == None:
            for sp_task in self._sp_task_list:
                sp_task[1] = True
        else:
            self._sp_task_list[index][1] = True

    def disable_pkt(self, index=None):
        """
        Disable the packet data.
        If you do not want to send the packets, you should disable the packet data.

        :param index: the packet data list's index number.
        """
        if index == None:
            for sp_task in self._sp_task_list:
                sp_task[1] = False
        else:
            self._sp_task_list[index][1] = False

    def start_traffic(self):
        """
        Start all enable packets.
        """
        for sp_task in self._sp_task_list:
            if sp_task[1]:
                sp_task[0].start()

    def stop_traffic(self):
        """
        Stop all enable packets.
        """
        for sp_task in self._sp_task_list:
            if sp_task[1]:
                sp_task[0].terminate()

    def get_packets(self):
        """
        Get the sent packets as list.
        After get, you cannot get again

        :return sent packet list.
        """
        q_len = int(self.queue.qsize())
        pkt_list = [self.queue.get() for _ in range(int(q_len))]
        return pkt_list
