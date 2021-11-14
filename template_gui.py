import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import WINDOW_CLOSED

layout = [
    [sg.Text("Linha 1", key="-Line1-"), sg.Button("botão linha 1")],
    [sg.In("Input 2", key="-Input2"), sg.Button("botão linha 2")],
]

window = sg.Window("teste", layout)

while True:
    event, values = window.read()
    print(event, values)
    if event == sg.WINDOW_CLOSED:
        break

window.close()