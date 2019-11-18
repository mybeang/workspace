from pandas import DataFrame
from tabulate import tabulate
from copy import copy

# Test Data
pizza_ports = [str(i) for i in range(1, 49)]
chassis_ports = ['tengigabitethernet 0/1', 'tengigabitethernet 0/2', 'tengigabitethernet 0/3',
                 'tengigabitethernet 0/4', 'tengigabitethernet 1/1', 'tengigabitethernet 1/2',
                 'tengigabitethernet 1/3', 'tengigabitethernet 1/4']

my_p_port = ['1', '12']
my_c_port = ['0/1', '1/2']

def ck_chassis(ports):
    result = list()
    for port in ports:
        if "/" in port:
            result.append(True)
        else:
            result.append(False)
    if False in result:
        return False
    else:
        return True

def actual_ports(ports, start, end):
    is_chassis = ck_chassis(ports)
    _start = 0
    _end = -1
    if not is_chassis:
        _start = ports.index(start)
        _end = ports.index(end) + 1
    else:
        for i, p_name in enumerate(ports):
            if start in p_name:
                _start = i
            if end in p_name:
                _end = i + 1
    _ports = ports[_start: _end]
    return len(_ports), _ports

def print_topology(ports):
    _ports = copy(ports)
    _2nd_port = _ports.pop(1)
    _ports.append(_2nd_port)
    _ports.insert(0, 'Lan1')
    _ports.append('Lan2')
    tps_tuple_list = list(zip(_ports[0::2], _ports[1::2]))
    tps = ["{} <-> {}".format(*tp) for tp in tps_tuple_list]
    data = {"Topology":tps}
    tp_data = DataFrame(data)
    print(tabulate(tp_data, headers='keys', tablefmt='grid'))


def vlan_setting(n_port, ports):
    vlan_num = int(n_port / 2)
    vlans = [i + 10 for i in range(vlan_num)]
    _ports = copy(ports)
    _2nd_port = _ports.pop(1)
    _ports.append(_2nd_port)
    mem_list = list(zip(_ports[0::2], _ports[1::2]))
    data = {"vlan_id": vlans, "membership": mem_list}
    tp_data = DataFrame(data)
    print(tabulate(tp_data, headers='keys', tablefmt='grid'))
    return tp_data

p_result = actual_ports(pizza_ports, my_p_port[0], my_p_port[1])
print("installed ports = {} ~ {}".format(pizza_ports[0], pizza_ports[-1]))
print("number of ports = {0}, ports_list = {1}".format(*p_result))

print_topology(p_result[1])
vlan_setting(*p_result)

c_result = actual_ports(chassis_ports, my_c_port[0], my_c_port[1])
print("installed ports = {} ~ {}".format(chassis_ports[0], chassis_ports[-1]))
print("number of ports = {0}, ports_list = {1}".format(*c_result))

print_topology(c_result[1])
data = vlan_setting(*c_result)
for row in data.iterrows():
    _, kk = row
    print(kk.tolist())
