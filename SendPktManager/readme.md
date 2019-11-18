# SendPktManager

Send Packet Manager.

    This module can send the packet without the finishing.
    You can terminate any time after start to send the packets.
    Refer to the test.py for using.


# Simple Usage:
```python
>>> pkt = Ether () / IP () # the packet format should be kept the scapy.
>>> spm = SendPktManager()
>>> spm.add_pkt(td.pkt[0], 'lo')
>>> spm.start_traffic()
>>> spm.stop_traffic()
>>> pkt_list = spm.get_packets()
>>> del spm
```

# Test 
```
root@dzytest001:~/workspace/SendPktManager
# python test.py

######################
## Test Description ##
######################
Check to send the list of packet

Send packet list 0 to 3 in same add_pkt
######################

Send Traffic
Wait 10 seconds
..........** Result:
pkt_0,pkt_1,pkt_2,pkt_3,pkt_0,pkt_1,pkt_2,pkt_3,pkt_0,pkt_1

######################
## Test Description ##
######################
Check to send in many add_pkt.

Send packet list 0 to 2 in the other add_pkt with different interval.
######################

Send Traffic
Wait 5 seconds
..................** Result:
pkt_0,pkt_2,pkt_1,pkt_2,pkt_0,pkt_2,pkt_2,pkt_0,pkt_1,pkt_2,pkt_2,pkt_0,pkt_2,pkt_2,pkt_1,pkt_0,pkt_2,pkt_2

######################
## Test Description ##
######################
Check enable/disable pkt

Send packet list 0 to 4 in the other add_pkt with different interval.
pkt_0, pkt_1, pkt_4 are enable.
pkt_2, pkt_3 are disable.
######################

Send Traffic
Wait 5 seconds
...............................** Result:
pkt_0,pkt_4,pkt_1,pkt_1,pkt_1,pkt_1,pkt_1,pkt_0,pkt_1,pkt_1,pkt_1,pkt_1,pkt_1,pkt_0,pkt_1,pkt_1,pkt_1,pkt_1,pkt_1,pkt_0,pkt_1,pkt_1,pkt_1,pkt_1,pkt_1,pkt_0,pkt_1,pkt_1,pkt_1,pkt_1,pkt_1
```

