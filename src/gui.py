import PySimpleGUI as sg
import os

def main_window():
    layout = [
        [sg.Text("File Encryption/Decryption", font=("Helvetica", 16))],
        [sg.Text("Choose File:"), sg.Input(), sg.FileBrowse(key="-FILE-")],
        [sg.Text("Output Path:"), sg.Input(), sg.SaveAs(key="-OUT-")],
        [sg.Text("Password:"), sg.Input(password_char='*', key="-PWD-")],
        [sg.Button("Encrypt"), sg.Button("Decrypt"), sg.Button("Exit")]
    ]
    return sg.Window("Portable Encryptor", layout, finalize=True)

def popup_success(msg):
    sg.popup(msg, title="Success")

def popup_error(msg):
    sg.popup_error(msg, title="Error")
