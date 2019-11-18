import PySimpleGUI as sg

data = [
    [sg.Checkbox("Hi", key="_HI1_"), sg.In(""), sg.Text("Saveme")],
    [sg.Checkbox("Hi", key="_HI2_"), sg.In(""), sg.Text("Saveme")]
]

layout = [
    [sg.Table(values=data, headings=['a', 'b', 'c'], key="_TABLE_",
              def_col_width=20,
              max_col_width=20,
              col_widths=20,
              auto_size_columns=False,
              num_rows=20,
              enable_events=True)],
    [sg.Exit()]
]

w = sg.Window('Table', grab_anywhere=False, resizable=True).Layout(layout)
while True:
    event, values = w.Read()
    if event is None or event == "Exit":
        break
    print(event, values)