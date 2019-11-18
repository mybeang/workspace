import socket
import threading
import wmi
import sys
import struct
import logging
from time import sleep
from pandas import DataFrame


def find_if(ifname):
    for iface_obj in wmi.WMI().Win32_NetworkAdapterConfiguration(IPEnabled=True):
        if iface_obj.Description == ifname:
            return iface_obj


def make_data_pkt(dst_mac, src_mac, src_ip, dst_ip, length=None):
    MAX_PKT_SIZE = 1500 - 16 - 21 - 20
    _dst_mac = [int(i, 16) for i in dst_mac.split(":")]
    ether_header = struct.pack("{}B".format(len(_dst_mac)), *(_dst_mac))
    _src_mac = [int(i, 16) for i in src_mac.split(":")]
    ether_header += struct.pack("{}B".format(len(_src_mac)), *(_src_mac))
    ether_header += b"\x08\x00"
    ip_header = b'E\x00\x00\x14\x00\x01\x00\x00@\x00yd'
    src_ip = [int(i) for i in src_ip.split(".")]
    ip_header += struct.pack("{}B".format(len(src_ip)), *(src_ip))
    dst_ip = [int(i) for i in dst_ip.split(".")]
    ip_header += struct.pack("{}B".format(len(dst_ip)), *(dst_ip))
    if isinstance(length, int):
        if length > MAX_PKT_SIZE:
            raise ValueError("Too big payload!!")
        payload = struct.pack("{}s".format(length), b"0"*length)
    else:
        payload = b""
    test_string = b"DASANZHONE TESTPACKET"
    payload += struct.pack("{}s".format(len(test_string)), test_string)
    data = ether_header + ip_header + payload
    return data


class Interface(object):
    def __init__(self, ifname, ip, subnet="255.255.255.0"):
        self.sniff_buf = list()
        self.sniff_flags = False
        self.ifname = ifname
        self.iface_obj = find_if(ifname)
        self.iface_obj.EnableStatic(IPAddress=[ip], SubnetMask=[subnet])
        logging.debug("Create Interface")
        sleep(5)
        self.iface_obj = find_if(self.ifname)
        self.ip_addr = self.iface_obj.IPAddress[0]
        self.mac_addr = self.iface_obj.MACAddress
        logging.debug(self.ip_addr)
        logging.debug(self.mac_addr)

    def send(self, pkt_data, target_iface, counts=100000):
        sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)
        sock.bind((self.ip_addr, 0))
        sock.settimeout(60)
        for _ in range(counts):
            sock.sendto(pkt_data, (target_iface.ip_addr, 0))
        del sock
        logging.debug("Wait during sending all packets ")
        sleep(5)

    def _recv(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)
        sock.bind((self.ip_addr, 0))
        sock.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
        sock.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)
        sock.settimeout(60)
        if not hasattr(self, "sniff_buf"):
            setattr(self, "sniff_buf", list())
        else:
            self.sniff_buf.clear()
        while True:
            if not self.sniff_flags:
                break
            try:
                buf = sock.recvfrom(2048)
            except socket.timeout:
                break
            else:
                if buf:
                    self.sniff_buf.append(buf[0])
        del sock


    def start_sniff(self):
        self.sniff_flags = True
        self.th = threading.Thread(target=self._recv)
        self.th.daemon = True
        self.th.start()

    def stop_sniff(self):
        self.sniff_flags = False
        self.th.join()
        del self.th


class PacketControl(object):
    def __init__(self):
        self.interfaces = list()

    def add_interface(self, ifname, ip, subnet="255.255.255.0"):
        self.interfaces.append(Interface(ifname, ip, subnet))

    def _ck_pkts(self, iface):
        pkt_key = b"DASANZHONE TESTPACKET"
        matched_count = 0
        for pkt in iface.sniff_buf:
            if pkt[0-len(pkt_key):] == pkt_key:
                matched_count += 1
        return matched_count

    def analysis(self, expected_count):
        header = ["Ifname", "Result", "Expected", "Actual"]
        result = list()
        for iface in self.interfaces:
            actual_count = self._ck_pkts(iface)
            result.append({
                header[0]: iface.ifname,
                header[1]: "PASS" if expected_count == actual_count else "FAIL",
                header[2]: expected_count,
                header[3]: actual_count
            })

        return DataFrame(result, columns=header)


if __name__=="__main__":
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    hdl = logging.StreamHandler(sys.stdout)
    fmt =  "[%(levelname)s] %(msg)s"
    fmter = logging.Formatter(fmt)
    hdl.setFormatter(fmter)
    logger.addHandler(hdl)

    iface1 = "Realtek USB FE Family Controller"
    ip1 = "192.192.192.1"
    iface2 = "Realtek USB FE Family Controller #2"
    ip2 = "192.192.192.2"
    pc = PacketControl()
    pc.add_interface(iface1, ip1)
    pc.add_interface(iface2, ip2)
    test_count = 1000000
    """
    data = make_data_pkt(dst_mac=pc.interfaces[1].mac_addr, src_mac=pc.interfaces[0].mac_addr,
                         src_ip=pc.interfaces[0].ip_addr, dst_ip=pc.interfaces[1].ip_addr,
                         length=1000)
    pc.interfaces[1].start_sniff()
    pc.interfaces[0].send(data, pc.interfaces[1], test_count)
    pc.interfaces[1].stop_sniff()
    """
    data = make_data_pkt(dst_mac=pc.interfaces[0].mac_addr, src_mac=pc.interfaces[1].mac_addr,
                         src_ip=pc.interfaces[1].ip_addr, dst_ip=pc.interfaces[0].ip_addr,
                         length=1000)
    pc.interfaces[0].start_sniff()
    pc.interfaces[1].send(data, pc.interfaces[0], test_count)
    pc.interfaces[0].stop_sniff()
    result = pc.analysis(test_count)
    print(result)

