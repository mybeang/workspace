import logging
import sys
from dal.model.factory import Dut


log_level = logging.INFO
logging_fmt = '%(asctime)-15s %(levelname)-7s %(message)s'
logger = logging.getLogger()
logger.setLevel(log_level)
formatter = logging.Formatter(logging_fmt)
stdoutHandler = logging.StreamHandler(sys.stdout)
stdoutHandler.setFormatter(formatter)
logger.addHandler(stdoutHandler)


session_info = {'baudrate': 9600, 'port': 'COM3'}
dut = Dut("PilotDut", "serial", session_info)


print(dut.bootloader.get_flash_info())
ip = "10.55.58.225"
gateway = "10.55.58.254"
netmask = "255.255.255.0"
default_addr = '1.1.1.1'
if not (dut.bootloader.get_ip() == ip):
    dut.bootloader.set_ip(ip)
if not (dut.bootloader.get_gateway() == gateway):
    dut.bootloader.set_gateway(gateway)
if not (dut.bootloader.get_netmask() == netmask):
    dut.bootloader.set_netmask(netmask)

dut.bootloader.load_image(
    image_type='os1',
    server_ip='10.55.2.202',
    file_name='H715/1.00/H715.1.00_0003-01.x'
)

dut.bootloader.reboot()
dut.bootloader.boot()
dut.bootloader.enter_mode()
dut.bootloader.set_ip(default_addr)
dut.bootloader.set_gateway(default_addr)
dut.bootloader.set_netmask(default_addr)