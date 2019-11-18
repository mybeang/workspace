import socket
import threading
import sys
import logging
import struct
from time import sleep
from pandas import DataFrame
from pktctrl.utils import find_if, make_data_pkt


class Interface(object):
    def __init__(self, ifname, iface_db, ip=None, subnet="255.255.0.0", output=None):
        self.__gen_ip_host = 1
        self.sniff_buf = list()
        self.output = output
        self.sniff_flags = False
        self.ifname = ifname
        self.iface_db = iface_db
        self.iface_obj = find_if(ifname, self.iface_db)
        if ip is not None:
            if not self.iface_obj.IPAddress:
                ip = "169.254.0.%d".format(self.__gen_ip_host)
                self.__gen_ip_host += 1
            self.iface_obj.EnableStatic(IPAddress=[ip], SubnetMask=[subnet])
            logging.debug("Create Interface")
            sleep(5)
            self.iface_obj = find_if(self.ifname, self.iface_db)
        self.ip_addr = self.iface_obj.IPAddress[0]
        self.mac_addr = self.iface_obj.MACAddress
        logging.debug("iface: {}: {}: {}".format(ifname, self.ip_addr, self.mac_addr))

    def _calcu_percent(self, current_count, total_count):
        return int((current_count * 100) / int(total_count))

    def send(self, pkt_data, target_iface, counts=100000, snd_buff=2 ** 20, ppg=240, interval=0.01, silent=False):
        logging.debug("func: Interface.send - start send")
        if self.output:
            self.output.print("")
        else:
            print("")
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.bind((self.ip_addr, 61000))
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, snd_buff)
        sock.settimeout(60)
        percent_string = "Send progress: [%d%%]"
        r_cnt = 0
        cnt = 0
        for i in range(1, counts + 1):
            req = b"_%s" % str("%.12d" % i).encode()
            seq = struct.pack("%ds" % len(req), req)
            snd_bytes = sock.sendto(pkt_data + seq, (target_iface.ip_addr, 61000))
            if snd_bytes < 1:
                logging.warning("MISSING!!")
            if cnt > ppg:
                if not silent:
                    cur_pg = self._calcu_percent(i, counts)
                    if self.output:
                        self.output.print_sp(percent_string % cur_pg)
                    else:
                        print(percent_string % cur_pg, end="\r")
                cnt = 0
                sleep(interval)
            cnt += 1
            r_cnt += 1
        logging.debug("real send count = {}".format(r_cnt))
        if not silent:
            if self.output:
                self.output.print_sp(percent_string % 100)
            else:
                print(percent_string % 100, end="\r")
        sock.close()
        del sock

    def _recv(self, snd_buff=2 ** 20):
        logging.debug("func: Interface._recv - start recv")
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.bind((self.ip_addr, 61000))
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, snd_buff)
        sock.settimeout(20)
        while True:
            if not self.sniff_flags:
                break
            try:
                buf = sock.recvfrom(65535)
            except socket.timeout:
                logging.debug("sock timeout")
                break
            else:
                if buf:
                    self.sniff_buf.append(buf)
        sock.close()
        del sock

    def start_sniff(self):
        logging.debug("func: Interface.start_sniff")
        self.sniff_flags = True
        self.th = threading.Thread(target=self._recv)
        self.th.daemon = True
        self.th.start()
        sleep(1)

    def stop_sniff(self):
        logging.debug("func: Interface.stop_sniff")
        sleep(1)
        self.sniff_flags = False
        self.th.join()
        del self.th


class PacketControl(object):
    def __init__(self, iface_db, log_app=None):
        self.interfaces = list()
        self.log_app = log_app
        self.iface_db = iface_db

    def add_interface(self, ifname, ip=None, subnet="255.255.0.0"):
        self.interfaces.append(Interface(ifname, self.iface_db, ip, subnet, self.log_app))

    def clear_all_buf(self):
        for iface in self.interfaces:
            iface.sniff_buf.clear()

    def _ck_pkts(self, s_if, d_if, expected_cnt, print_matched_packets=False):
        logging.debug("start ck {}".format(d_if.ifname))
        pkt_key = b"DASANZHONE TESTPACKET"
        matched_count = 0
        sample_pkts = list()
        logging.info("received packet cnt = {}".format(len(d_if.sniff_buf)))
        for i, pkt in enumerate(d_if.sniff_buf):
            same_ip = pkt[1][0] == s_if.ip_addr
            in_sign = pkt_key in pkt[0]
            if same_ip and in_sign:
                matched_count += 1
                if print_matched_packets:
                    s_ip = pkt[1][0]
                    index = pkt.decode('utf-8', 'ignore').index(pkt_key.decode())
                    req = pkt[index:].decode('utf-8', 'ignore')
                    logging.info("recived_pkt: sip:%s - req: %s" % (s_ip, req))
            else:
                sample_pkts.append((i, pkt))
        if matched_count < expected_cnt:
            logging.warning("check rx packets flags: len(not_matched pkts) = {}".format(len(sample_pkts)))
            if len(sample_pkts) > 10:
                _sample_pkts = sample_pkts
            else:
                _sample_pkts = sample_pkts[:20]
            for sample_pkt in _sample_pkts:
                logging.debug("{}: {};{}".format(sample_pkt[0],
                                                 socket.inet_ntoa(sample_pkt[1][16:20]),
                                                 sample_pkt[1][:20]))
        logging.info("Matched pkt cnt = {}".format(matched_count))
        return matched_count

    def analysis(self, expected_count):
        header = ["Ifname", "Result", "Expected", "Actual"]
        result = list()
        for s_if, d_if in zip(reversed(self.interfaces), self.interfaces):
            actual_count = self._ck_pkts(s_if, d_if, expected_count)
            result.append({
                header[0]: d_if.ifname,
                header[1]: "PASS" if expected_count == actual_count else "FAIL",
                header[2]: expected_count,
                header[3]: actual_count
            })

        return DataFrame(result, columns=header)


if __name__=="__main__":
    from pktctrl.utils import get_if_list
    import tabulate
    from dal.factory import manufacturer as mf
    from datetime import datetime

    ########################################################
    #                      Test Data                       #
    ########################################################
    #iface1 = "ASIX AX88772A USB2.0 to Fast Ethernet Adapter"
    iface1 = "ASIX AX88772A USB2.0 to Fast Ethernet Adapter"
    iface2 = "Realtek USB FE Family Controller #3"
    log_file_path = "D:\\PA\\YTest\\kkkk\\pkt_ctl_log{}.log"
    session_info = {
        'proto': 'serial',
        'port': "COM6",
        'baudrate': 9600,
        'user': "admin",
        'passwd': ""
    }
    test_rounds = 1
    device_name = 'V2708M'
    ########################################################


    class App(object):
        def __init__(self, log_queue):
            self.run_flag = True
            self.log_queue = log_queue
            self.print_th = threading.Thread(target=self.screen_on, args=(self.log_queue,))

        def screen_on(self, log_queue):
            buf = ""
            while self.run_flag:
                sleep(0.1)
                if not log_queue.empty():
                    for _ in range(log_queue.qsize()):
                        buf += log_queue.get()
                        if '\n' in buf:
                            logging.debug("dut: %s" % buf.rstrip())
                            buf = ''

        def start(self):
            if hasattr(self, "print_th"):
                self.print_th.start()
            else:
                self.run_flag = True
                self.print_th = threading.Thread(target=self.screen_on, args=(self.log_queue,))
                self.print_th.start()

        def stop(self):
            self.run_flag = False

            self.print_th.join()
            del self.print_th

    NOW = datetime.now().strftime("%Y%m%d_%H%M%S")
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    hdl = logging.StreamHandler(sys.stdout)
    fhdl = logging.FileHandler(log_file_path.format(NOW))
    fmt = "[%(levelname)s] %(msg)s"
    fmter = logging.Formatter(fmt)
    fhdl.setFormatter(fmter)
    hdl.setFormatter(fmter)
    logger.addHandler(hdl)
    logger.addHandler(fhdl)

    dut = mf.Manufacturer(device_name).manufacture()

    dut.create_session(**session_info)
    print_app = App(dut.session[0].queue)
    print_app.start()
    dut.session[0].login()

    _, iface_db = get_if_list()
    pc = PacketControl(iface_db)
    pc.add_interface(iface1)
    pc.add_interface(iface2)
    #test_count = 10
    test_count = 100000
    pkt1 = make_data_pkt(length=1000)
    pkt2 = make_data_pkt(length=1000)

    logging.info("payload_size = %d" % (len(pkt1) + 12)) # with length the seq_number

    # for learning
    pc.interfaces[0].send(pkt1, pc.interfaces[1], 5, silent=True)
    pc.interfaces[1].send(pkt2, pc.interfaces[0], 5, silent=True)

    results = list()
    for i in range(test_rounds):
        times = "[%.2d]" % (i + 1)
        logging.info("\n"+"="*40)
        logging.info(times)
        logging.info(
            "Send Buffer = 1GB | Packets Per Group = 10 | Interval between Groups = 1ms"
        )
        logging.info("clear port stats")
        msg = dut.interface.clear_statistics_all()
        dut.session[0].send([msg])


        logging.info("Start Sniff at iface 1")
        pc.interfaces[1].start_sniff()
        sleep(1)
        logging.info("Start Send from iface 0 to iface 1")
        pc.interfaces[0].send(pkt1, pc.interfaces[1], test_count)
        sleep(5)
        logging.info("Stop Sniff at iface 1")
        pc.interfaces[1].stop_sniff()

        logging.info("Send 2")
        logging.info("Start Sniff at iface 0")
        pc.interfaces[0].start_sniff()
        sleep(1)
        logging.info("Start Send from iface 1 to iface 0")
        pc.interfaces[1].send(pkt2, pc.interfaces[0], test_count)
        sleep(5)
        pc.interfaces[0].stop_sniff()
        logging.info("Stop Sniff at iface 0")
        msgs = list()
        msgs.append(dut.interface.ports[0].get_statistics())
        msgs.append(dut.interface.ports[1].get_statistics())
        result_list = dut.session[0].send(msgs)
        data1 = list()
        for result in result_list:
            df = result.parsed[['IFACE', 'IfInUcastPkts', 'IfOutUcastPkts']]
            data1.append((df.loc[0].tolist()))

        msgs.clear()
        msgs.append(dut.interface.ports[0].get_rmon_statistics())
        msgs.append(dut.interface.ports[1].get_rmon_statistics())
        result_list = dut.session[0].send(msgs)
        data2 = list()
        for result in result_list:
            df = result.parsed[['Pkts1024to1518Octets']]
            data2.append(df.loc[0].tolist())
        result_df = pc.analysis(test_count)
        results.append((times, result_df, data1, data2))
        logging.info("\n" + tabulate.tabulate(result_df, headers='keys', tablefmt='grid'))
        logging.info("\n" + tabulate.tabulate(data1, headers='keys', tablefmt='grid'))
        logging.info("\n" + tabulate.tabulate(data2, headers='keys', tablefmt='grid'))
        pc.clear_all_buf()

    for res in results:
        res[1]['DUT'] = ' ->'
        res[1]['IFACE'] = None
        res[1]['IfInUcastPkts'] = None
        res[1]['IfOutUcastPkts'] = None
        res[1]['Pkts1024to1518Octets'] = None
        res[1]['IFACE'][0] = res[2][0][0]
        res[1]['IFACE'][1] = res[2][1][0]
        res[1]['IfInUcastPkts'][0] = res[2][0][1]
        res[1]['IfInUcastPkts'][1] = res[2][1][1]
        res[1]['IfOutUcastPkts'][0] = res[2][0][2]
        res[1]['IfOutUcastPkts'][1] = res[2][1][2]
        res[1]['Pkts1024to1518Octets'][0] = res[3][0][0]
        res[1]['Pkts1024to1518Octets'][1] = res[3][1][0]

        logging.info(res[0])
        logging.info("\n" + tabulate.tabulate(res[1], headers='keys', tablefmt='grid'))

    print_app.stop()
    del print_app
    del dut
