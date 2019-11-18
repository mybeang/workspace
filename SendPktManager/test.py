from scapy.all import *
from SendPktManager import SendPktManager

class TestData(object):
    def __init__(self):
        self.pkt = [
            Ether(src="00:00:01:00:00:0{}".format(i)) / IP() / Padding(load="pkt_{}".format(i)) for i in range(10)
        ]
        self.iface = 'lo'

def wait(seconds=5):
    print("Wait {} seconds".format(seconds))
    time.sleep(seconds)

def show_pkt_seq(pkt_list):
    rx_list = list()
    for pkt in pkt_list:
        rx_list.append(pkt[Padding].load)
    print("** Result:")
    print(','.join(rx_list))

def test_001():
    """
######################
## Test Description ##
######################
Check to send the list of packet

Send packet list 0 to 3 in same add_pkt
######################
    """
    td = TestData()
    smp = SendPktManager(verbose=1)
    smp.add_pkt(td.pkt[:4], td.iface)
    print("Send Traffic")
    smp.start_traffic()
    wait(10)
    smp.stop_traffic()
    pkt_list = smp.get_packets()
    show_pkt_seq(pkt_list)
    del smp

def test_002():
    """
######################
## Test Description ##
######################
Check to send in many add_pkt.

Send packet list 0 to 2 in the other add_pkt with different interval.
######################
    """
    td = TestData()
    smp = SendPktManager(verbose=1)
    smp.add_pkt(td.pkt[0], td.iface)
    smp.add_pkt(td.pkt[1], td.iface, inter=2)
    smp.add_pkt(td.pkt[2], td.iface, inter=0.5)
    print("Send Traffic")
    smp.start_traffic()
    wait()
    smp.stop_traffic()
    pkt_list = smp.get_packets()
    show_pkt_seq(pkt_list)
    del smp

def test_003():
    """
######################
## Test Description ##
######################
Check enable/disable pkt

Send packet list 0 to 4 in the other add_pkt with different interval.
pkt_0, pkt_1, pkt_4 are enable.
pkt_2, pkt_3 are disable.
######################
    """
    td = TestData()
    smp = SendPktManager(verbose=1)
    smp.add_pkt(td.pkt[0], td.iface)
    smp.add_pkt(td.pkt[1], td.iface, inter=0.2)
    smp.add_pkt(td.pkt[2], td.iface, inter=0.5)
    smp.add_pkt(td.pkt[3], td.iface, inter=2)
    smp.add_pkt(td.pkt[4], td.iface, inter=5)
    smp.disable_pkt(2)
    smp.disable_pkt(3)
    print("Send Traffic")
    smp.start_traffic()
    wait()
    smp.stop_traffic()
    pkt_list = smp.get_packets()
    show_pkt_seq(pkt_list)
    del smp


if __name__=="__main__":
    print(test_001.__doc__)
    test_001()
    print(test_002.__doc__)
    test_002()
    print(test_003.__doc__)
    test_003()