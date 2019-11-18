#!bin/python2

import pdb
import logging
from color_code import cprint


def enter_mode(cur_mode):
    def call_func(self, cur_mode, **kwargs):
        if cur_mode == 'global':
            cprint("conf t", 'blue')
        elif cur_mode == 'bridge':
            cprint("conf t", 'blue')
            cprint("bridge", 'blue')
        elif cur_mode == 'interface':
            cprint("conf t", 'blue')
            if 'iface' in kwargs:
                cprint("interface {iface}".format(**kwargs), 'blue')
            elif 'vid' in kwargs:
                cprint("interface {}{vid}".format(self.vlan_str, **kwargs), 'blue')
            else:
                logging.warn("Not support interface")
        else:
            logging.warn("Not support mode")

    def end_func():
        cprint("end", 'blue')

    def decorator(func):
        def wrapper(self, *args, **kwargs):
            if 'deco_skip' not in kwargs:
                kwargs['deco_skip'] = False

            if not kwargs['deco_skip']:
                if isinstance(cur_mode, str):
                    call_func(self, cur_mode, **kwargs)
                else:
                    logging.warn("The input param should be string type")
                del kwargs['deco_skip']
                func(self, *args, **kwargs)
                end_func()
            else:
                func(self, *args, **kwargs)
        return wrapper
    return decorator


class TEST1G(object):
    def __init__(self):
        self.mode = None
        self.vlan_str = ''

    def get_mac_table(self):
        cprint("show mac", 'yellow')

    @enter_mode('global')
    def global_mode(self):
        print(">>>>>> Some config in global mode")

    @enter_mode('bridge')
    def bridge_mode(self):
        print(">>>>>> Some config in bridge mode")

    @enter_mode('interface')
    def interface_mode(self, **kwargs):
        if 'vid' in kwargs:
            print(">>>>>> Some config in interface {}{vid} mode".format(self.vlan_str, **kwargs))
        else:
            print(">>>>>> Some config in interface {iface} mode".format(self.vlan_str, **kwargs))


class TEST2G(object):
    def __init__(self):
        self.mode = None
        self.vlan_str = 'vlan '

    def get_mac_table(self):
        cprint("show mac", 'yellow')

    @enter_mode('global')
    def global_mode(self):
        print(">>>>>> Some config in global mode")

    @enter_mode('bridge')
    def bridge_mode(self):
        print(">>>>>> Some config in bridge mode")

    @enter_mode('interface')
    def interface_mode(self, **kwargs):
        if 'vid' in kwargs:
            print(">>>>>> Some config in interface {}{vid} mode".format(self.vlan_str, **kwargs))
        else:
            print(">>>>>> Some config in interface {iface} mode".format(self.vlan_str, **kwargs))


class TEST3G(object):
    def __init__(self):
        self.mode = None
        self.vlan_str = 'vlan1.'

    def get_mac_table(self):
        cprint("show mac address-table", 'yellow')

    @enter_mode('global')
    def global_mode(self):
        print(">>>>>> Some config in global mode")

    @enter_mode('bridge')
    def bridge_mode(self):
        print(">>>>>> Some config in bridge mode")

    @enter_mode('interface')
    def interface_mode(self, **kwargs):
        if 'vid' in kwargs:
            print(">>>>>> Some config in interface {}{vid} mode".format(self.vlan_str, **kwargs))
        else:
            print(">>>>>> Some config in interface {iface} mode".format(self.vlan_str, **kwargs))

    @enter_mode('interface')
    def change_switch_mode(self, mode, **kwargs):
        cprint("switchport mode {}".format(mode), 'cyan')

    @enter_mode('interface')
    def add_vlan(self, vid, is_trunk=False, is_native=False, **kwargs):
        if is_trunk:
            self.change_switch_mode('trunk', deco_skip=True)
            cprint("switchport trunk allowed vlan add {}".format(vid), 'yellow')
            if is_native:
                cprint("switchport trunk native vlan {}".format(vid), 'yellow')
        else:
            self.change_switch_mode('access', deco_skip=True)
            cprint("switchport access vlan {}".format(vid), 'yellow')


if __name__=='__main__':
    cprint("++++++++++++ 1G +++++++++++++", 'red')
    g1 = TEST1G()
    g1.global_mode(); print('-' * 30)
    g1.bridge_mode(); print('-' * 30)
    g1.interface_mode(vid='9'); print('-' * 30)
    g1.get_mac_table()
    cprint("++++++++++++ 2G +++++++++++++", 'red')
    g2 = TEST2G()
    g2.global_mode(); print('-' * 30)
    g2.bridge_mode(); print('-' * 30)
    g2.interface_mode(vid=9); print('-' * 30)
    g2.interface_mode(iface='ge0/1'); print('-' * 30)
    g2.get_mac_table()
    cprint("++++++++++++ 3G +++++++++++++", 'red')
    g3 = TEST3G()
    g3.global_mode(); print('-' * 30)
    g3.bridge_mode(); print('-' * 30)
    g3.interface_mode(vid=10); print('-' * 30)
    g3.interface_mode(iface='xe0/1'); print('-' * 30)
    g3.change_switch_mode('access', iface='xe0/2'); print('-' * 30)
    g3.add_vlan(10, iface='xe0/3'); print('-' * 30)
    g3.add_vlan(11, True, iface='xe0/4'); print('-' * 30)
    g3.add_vlan(12, True, True, iface='xe0/5'); print('-' * 30)
    g3.get_mac_table()