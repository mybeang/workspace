from scapy.all import *


L2=Ether(dst="00:00:00:00:00:02", src="00:00:00:00:00:01")
L3=IP(src="1.1.1.1", dst="2.2.2.2")
PAD="XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
pkt=L2/L3/PAD
iface = "Realtek USB GbE Family Controller #2"
sock = conf.L2socket(iface="Realtek USB GbE Family Controller #2")
while True:
    try:
        sock.send(pkt)
    except KeyboardInterrupt:
        break
