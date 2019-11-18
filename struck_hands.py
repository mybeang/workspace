import struct

dst_mac = "00:00:01:00:00:01"
src_mac = "00:00:02:00:00:01"
ethtype = 0x0800


dst_ip = "192.192.192.2"
src_ip = "192.192.192.1"
result = b'E\x00\x00\x14\x00\x01\x00\x00@\x00yd\xc0\xc0\xc0\x01\xc0\xc0\xc0\x02'
data = b''

def esf(data, split_char=""):
    if not split_char:
        if isinstance(data, str):
            _data = [int(data, 16)]
        else:
            return struct.pack(">h", data)
    else:
        _data = [int(i, 16) for i in data.split(split_char)]
    print(_data)
    return struct.pack("{}B".format(len(_data)), *(_data))


data += b'E\x00\x00\x14\x00\x01\x00\x00@\x00yd'
src_ip = [int(i) for i in src_ip.split(".")]
data += struct.pack("{}B".format(len(src_ip)), *(src_ip))
dst_ip = [int(i) for i in dst_ip.split(".")]
data += struct.pack("{}B".format(len(dst_ip)), *(dst_ip))
test_string = b"DASANZHONE TESTPACKET"
print(len(test_string))
data += struct.pack("{}s".format(len(test_string)), test_string)
print(data)