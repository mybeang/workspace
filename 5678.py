import socket
import wmi

def find_if(ifname):
    for iface_obj in wmi.WMI().Win32_NetworkAdapterConfiguration(IPEnabled=True):
        if iface_obj.Description == ifname:
            return iface_obj


class What(object):
    def __init__(self):
        self.iface = find_if("Realtek USB FE Family Controller")
        ip = "192.192.192.1"
        self.iface.EnableStatic(IPAddress=[ip], SubnetMask=["255.255.255.0"])
        self.iface = find_if("Realtek USB FE Family Controller")
        import time
        time.sleep(3)
        print(self.iface.IPAddress[0])

    def send(self):
        for i in range(4):
            sock1 = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)
            # sock1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
            # sock1.bind(("192.192.192.1", 0))
            sock1.bind((self.iface.IPAddress[0], 0))
            # sock1.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL,1)
            # sock1.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)
            # sock1.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

            data = b'\xa0\xce\xc8\x06c\x95\xa0\xce\xc8\x05e\x87\x08\x00E\x00\x00\x14\x00\x01\x00\x00@\x00yd\xc0\xc0\xc0\x01\xc0' \
                   b'\xc0\xc0\x020000000000000000'
            sock1.sendto(data+b'%d'%i, ("192.192.192.2", 0))
            #sock1.send(data+b'%d'%i)

w = What()
w.send()