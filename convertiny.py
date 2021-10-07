# fonte craido dia 04/10/2021
# autor: Jose Duarte
#Compactador de imagens para o site San Diego
import PySimpleGUI as sg
import tinify
from glob import glob
import os.path
import shutil
sg.theme('Reddit')
layout = [
    [sg.Text("Pasta de Imagens: "), sg.Input(key="-IN2-" ,change_submits=True), sg.FolderBrowse(key="-IN-")],
    [sg.Button("Compactar")],
    [sg.Button('Exit', button_color=('white', 'firebrick3'))],
    [sg.Text('Imagens Compactadas')],
    [sg.Multiline(key='files', size=(70,10), autoscroll=True)],
    ]
tinify.key = "Your-Key-HERE"
window = sg.Window('Compactador de Imagens', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event=="Exit":
        window.close()
        break
    if event in ('Exit', None):
        break
    elif event == "Compactar":
        source_dir_name = (values["-IN2-"])
        filenames = os.listdir(source_dir_name)
        # it uses `key='files'` to access `Multiline` widget
        window['files'].update("\n".join(filenames))
        files = glob(source_dir_name + '\*')
        if os.path.exists('Compactadas'):
            shutil.rmtree('Compactadas')
        os.mkdir('Compactadas') 
        destination_dir_name =os.path.join(os.getcwd(), "Compactadas")
        for file in files:
            source = tinify.from_file(file)
            file_name, ext = os.path.splitext(file)
            file_name = file_name.replace(source_dir_name + "\\",'' )
            source.to_file(destination_dir_name + '\\' + file_name + ".jpg")
        filenames = sorted(os.listdir(destination_dir_name))
            # it use `key='files'` to `Multiline` widget
        window['files'].update("\n".join(filenames))
        sg.Popup('Tudo Certo!', 'Todas as imagens Foram Compactadas','Pasta de saida ' + destination_dir_name)
        
