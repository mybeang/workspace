from scapy.all import *
import re

dst_mac = "00:00:01:00:00:01"
src_mac = "00:00:02:00:00:01"
dst_ip = "192.192.192.2"
src_ip = "192.192.192.1"

packet = Ether(dst=dst_mac, src=src_mac) / IP(src=src_ip, dst=dst_ip)
import pdb
pdb.set_trace()
def get_iface(guid):
    for i in get_if_list():
        return re.findall(guid, i)

lan1 = "Realtek USB FE Family Controller"
lan1_guid = "38442143-F72A-4F7C-8D32-2D28847CCBCB"
lan1_iface = get_iface(lan1_guid)
lan2 = "Realtek USB FE Family Controller #2"
lan2_guid = '98F33973-60C6-4295-918B-4036327FC438'
lan3 = 'ASIX AX88179 USB 3.0 to Gigabit Ethernet Adapter'


sendp(packet, iface=lan1, count=1, verbose=0)

