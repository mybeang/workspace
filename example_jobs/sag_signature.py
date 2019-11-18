import struct
import random
from scapy.all import Raw

HEAD_START = 'SAG'
HEAD_END = 'sag'

def convert_list_str(input_data):
    if isinstance(input_data, str):
        _tuple_data = struct.unpack('%sB' % len(input_data), input_data)
        return ''.join(map(str, _tuple_data))
    elif isinstance(input_data, list):
        return struct.pack('%sB' % len(input_data), *tuple(input_data))
    else:
        print("Wrong Type. Type are list and str.")
        return

def make_signature():
    #flow id range = 0x000000 ~ 0xFFFFFF
    flow_id = list()
    for _ in range(0, 6):
        flow_id.append(random.randrange(0, 16))
    __tag = convert_list_str(flow_id)
    flow_id = ''.join(map(str, flow_id))
    raw = Raw(HEAD_START+__tag+HEAD_END)
    raw.show()
    return flow_id, raw

if __name__=="__main__":
    flow_id, raw = make_signature()
    print "flow_id = {}".format(flow_id)
    tag = convert_list_str(raw.load[3:-3])
    print "tag = {}".format(tag)
    print (flow_id==tag)
