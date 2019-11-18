import struct
import pythoncom
import wmi


def make_data_pkt(length=None):
    MAX_PKT_SIZE = 1500 - 16 - 21 - 20
    if isinstance(length, int):
        if length > MAX_PKT_SIZE:
            raise ValueError("Too big payload!!")
        payload = struct.pack("{}s".format(length), b"0"*length)
    else:
        payload = b""
    test_string = b"DASANZHONE TESTPACKET"
    payload += struct.pack("{}s".format(len(test_string)), test_string)
    #data = ether_header + ip_header + payload
    return payload

# Interface
###############
def find_if(ifname, db):
    pythoncom.CoInitialize()
    for iface_obj in wmi.WMI().Win32_NetworkAdapterConfiguration():
        if iface_obj.Index == db[ifname]:
            return iface_obj

def get_if_list():
    pythoncom.CoInitialize()
    adapter_list = list()
    adapter_db = dict()
    for adapter in wmi.WMI().Win32_NetworkAdapter():
        if adapter.PhysicalAdapter:
            if 'ROOT' not in adapter.PNPDeviceID:
                adapter_list.append(adapter.Name)
                adapter_db.update({adapter.Name: adapter.Index})
    return adapter_list, adapter_db
