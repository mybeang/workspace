import socket
import time


iface1 = "ASIX AX88772A USB2.0 to Fast Ethernet Adapter"
iface2 = "Realtek USB FE Family Controller #3"
pkt_data = b"0"*1000
sock1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock1.bind(("192.192.193.1", 61000))
sock2.bind(("192.192.192.1", 61000))
cnt = 0
while True:
    if cnt < 1000:
        try:
            snd_bytes = sock1.sendto(pkt_data, ("192.192.192.1", 61000))
        except KeyboardInterrupt:
            break
        else:
            if snd_bytes != 1000:
                print("ERROR CODE: {}".format(snd_bytes))
        cnt += 1
    else:
        cnt = 0
        time.sleep(0.001)

