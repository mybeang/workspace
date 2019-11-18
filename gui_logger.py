from logger import set_logger
import pdb
import logging
import time
import sys
import PySimpleGUI as sg
from gui_utils import TestData


_, _, _, string_io = set_logger()

TC_01 = "Power On/Off Test"
TC_02 = "Boot Loader Booting Test"
TC_03 = "EEPROM Read/Write Test"
TC_04 = "Diagnostic Test"
TC_05 = "OS Image Download Test"
TC_06 = "OS Booting Test"
TC_07 = "RTC Operating Test"
TC_08 = "Watchdog Test"
TC_LIST = [TC_01, TC_02, TC_03, TC_04, TC_05, TC_06, TC_07, TC_08]

tab1_left = [
    [sg.Text("Test Items", font=("Helvetica", 12))],
    [sg.Checkbox(TC_01, tooltip="(with Momentary Power Interruption)", size=(20, 1))],
    [sg.Checkbox(TC_02, tooltip="(with Momentary Power Interruption)", size=(20, 1))],
    [sg.Checkbox(TC_03, size=(20, 1))],
    [sg.Checkbox(TC_04, size=(20, 1))],
    [sg.Checkbox(TC_05, size=(20, 1))],
    [sg.Checkbox(TC_06, size=(20, 1))],
    [sg.Checkbox(TC_07, size=(20, 1))],
    [sg.Checkbox(TC_08, size=(20, 1))]
]
tab1_center = [
    [sg.Text("Repetition", font=("Helvetica", 12))],
    [sg.Input("", size=(5, 1), do_not_clear=True, justification="center")],
    [sg.Input("", size=(5, 1), do_not_clear=True, justification="center")],
    [sg.Input("", size=(5, 1), do_not_clear=True, justification="center")],
    [sg.Input("", size=(5, 1), do_not_clear=True, justification="center")],
    [sg.Input("", size=(5, 1), do_not_clear=True, justification="center")],
    [sg.Input("", size=(5, 1), do_not_clear=True, justification="center")],
    [sg.Input("", size=(5, 1), do_not_clear=True, justification="center")],
    [sg.Input("", size=(5, 1), do_not_clear=True, justification="center")]
]
tab1_right = [
    [sg.Text("Description", font=("Helvetica", 12))],
    [sg.Text("Some description", font=("System", 8))],
    [sg.Text("Some description", font=("System", 8))],
    [sg.Text("Some description", font=("System", 8))],
    [sg.Text("Some description", font=("System", 8))],
    [sg.Text("Some description", font=("System", 8))],
    [sg.Text("Some description", font=("System", 8))],
    [sg.Text("Some description", font=("System", 8))],
    [sg.Text("Some description", font=("System", 8))]
]

tab1_layout = [
    [sg.Column(tab1_left), sg.Column(tab1_center), sg.Column(tab1_right)],
    [sg.Button("Save TestCase Info")]
]

tab2_terminal_frame = sg.Frame(
    layout=[
        [sg.Column([[sg.Radio("Console", "SESSION")], [sg.Radio("Telnet", "SESSION"), ]]),
         sg.Column([[sg.InputOptionMenu(values=('COM1', 'COM2', 'COM3'), size=(10, 1)),
                     sg.InputOptionMenu(values=(9600, 115200), size=(15, 1))],
                    [sg.Text("IP Address"), sg.Input("", size=(20, 1), do_not_clear=True),
                     sg.Text("Port"), sg.Input("", size=(10, 1), do_not_clear=True)]])]
    ],
    title="Terminal"
)

tab2_power_control_frame = sg.Frame(
    layout=[
        [sg.Column([[sg.Radio("APC", "POWERCONTROL")], [sg.Radio("V100", "POWERCONTROL")]]),
         sg.Column([[sg.Text("IP Address"), sg.Input("", size=(20, 1), do_not_clear=True),
                     sg.Text("Port"), sg.Input("", size=(10, 1), do_not_clear=True)],
                    [sg.Text("IP Address"), sg.Input("", size=(20, 1), do_not_clear=True),
                     sg.Text("Port"), sg.Input("", size=(10, 1), do_not_clear=True)]])],
    ],
    title="Power Control"
)

tab2_layout = [
    [tab2_terminal_frame],
    [tab2_power_control_frame],
    [sg.Button("Save Config")]
]

tab3_left_frame = [
    [sg.Text("\n".join(TC_LIST), key="_TC_LIST_")]
]
tab3_left = sg.Column([
    [sg.Text("Running Tests", font=("System", 12))],
    [sg.Frame(
        layout=tab3_left_frame,
        title="",
        size=(20, 50)
    )],
])
tab3_right = sg.Column([
    [sg.Text("Screen", font=("System", 12))],
    [sg.Output(size=(60, 30))]
])
tab3_layout = [
    [sg.Button("Start Test")],
    [tab3_left, tab3_right],
    [sg.In(""), sg.FolderBrowse("LogPath"), sg.Button("Make Document")]
]

layout = [
    [sg.TabGroup([[sg.Tab('testcase', tab1_layout),
                   sg.Tab('setup', tab2_layout),
                   sg.Tab('Monitoring', tab3_layout)]])],
    [sg.Exit()]
]

windows = sg.Window('EVT').Layout(layout)
while True:
    event, values = windows.Read()
    td = TestData(values)
    if event is None or event == 'Exit':
        break

    if event == 'Save TestCase Info':
        tc_data, tc_flags = td.gen_tc_data()
        logging.info(tc_data)

        tc_list = []
        j = 0
        for i, flag in enumerate(tc_flags):
            if flag:
                _sub = ["test_0%.2d" % i for i in range(1, tc_data['test_list'][j]['repeat']+1)]
                tc_list.append("|- " + TC_LIST[i] + "\n|  |- " + "\n|  |- ".join(_sub))
        logging.info(tc_list)
        windows.FindElement("_TC_LIST_").Update("\n".join(tc_list))
    if event == 'Save Config':
        logging.info(td.gen_session_data())

    if event == 'Start Test':
        cli = "bin/evt evt_test.json"
        logging.info(cli)
windows.Close()

"""
i = 1
_buf = ""
while i < 10:                 # Event Loop
  window.ReadNonBlocking()
  logging.info(i)
  print(string_io.getvalue().splitlines()[-1])
  time.sleep(1)
  i += 1
"""

logging.info((event, values))
