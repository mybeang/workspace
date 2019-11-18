import pdb
import pprint
import sys
if sys.version_info[0] >= 3:
    import PySimpleGUI as sg
else:
    import PySimpleGUI27 as sg

TC_01 = "Power On/Off Test"
TC_02 = "Boot Loader Booting Test"
TC_03 = "EEPROM Read/Write Test"
TC_04 = "Diagnostic Test"
TC_05 = "OS Image Download Test"
TC_06 = "OS Booting Test"
TC_07 = "RTC Operating Test"
TC_08 = "Watchdog Test"
TC_LIST = [TC_01, TC_02, TC_03, TC_04, TC_05, TC_06, TC_07, TC_08]

treedata = sg.TreeData()

treedata.Insert("", '_TC1_', TC_LIST[0], [])
treedata.Insert("", '_TC2_', TC_LIST[1], [])
treedata.Insert("", '_TC3_', TC_LIST[2], [])
treedata.Insert("", '_TC4_', TC_LIST[3], [])
treedata.Insert("", '_TC5_', TC_LIST[4], [])
treedata.Insert("", '_TC6_', TC_LIST[5], [])
treedata.Insert("", '_TC7_', TC_LIST[6], [])
treedata.Insert("", '_TC8_', TC_LIST[7], [])



layout = [[ sg.Text('Running TestCase') ],
          [ sg.Tree(data=treedata,
                    headings=['Result'],
                    col0_width=20,
                    key='_TREE_',
                    show_expanded=True,
                    def_col_width=100,
                    change_submits=True, text_color="red"),
            ],
          [ sg.Button('Read'), sg.Button('Add'), sg.Button('Update1'), sg.Button('Update2'), sg.Button("Show"),
            sg.Button('Generate'),
          sg.Exit()]]

window = sg.Window('Tree Element Test').Layout(layout)

def gen():
    a = [1, 2]
    yield a

print(treedata)
result_data = {}
while True:     # Event Loop
    event, values = window.Read()
    if event is None or event == "Exit":
        break
    if event == "Add":
        sub = '_sub_1_1_'
        result_data[sub] = ["PASS", "log file full path"]
        treedata.Insert("_TC1_", sub, "test001", result_data[sub])
        sub = '_sub_1_2_'
        result_data[sub] = ["PASS", "log file full path"]
        treedata.Insert("_TC1_", sub, "test002", result_data[sub])
        sub = '_sub_4_1_'
        result_data[sub] = ["PASS", "log file full path"]
        treedata.Insert("_TC4_", sub, "test001", result_data[sub])
        sub = '_sub_4_2_'
        result_data[sub] = ["PASS", "log file full path"]
        treedata.Insert("_TC4_", sub, "test002", result_data[sub])
        window.FindElement('_TREE_').Update(treedata)
    if event == "Update1":
        treedata.tree_dict["_sub_4_1_"].values = ["FAIL", "log file full path"]
        window.FindElement('_TREE_').Update(treedata, "_sub_4_1_", ["FAIL", "log file full path"],
                                            "test001")
        window.Refresh()
    if event == "Update2":
        treedata.tree_dict["_sub_4_2_"].values = ["FAIL", "log file full path"]
        window.FindElement('_TREE_').Update(treedata, "_sub_4_2_", ["FAIL", "log file full path"],
                                            "test002")
        window.Refresh()
    if event == "Show":
        print(pprint.pformat(treedata.tree_dict, indent=4))
    if event == "Generate":
        log_t_list = values['_TREE_']
        for log_t in log_t_list:
            print(treedata.tree_dict[log_t].values[1])

    print(event, values)

