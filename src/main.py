import gui
import crypto_utils
import PySimpleGUI as sg

def main():
    window = gui.main_window()

    while True:
        event, values = window.read()

        if event in (sg.WIN_CLOSED, "Exit"):
            break

        file = values["-FILE-"]
        output = values["-OUT-"]
        password = values["-PWD-"]

        if not file or not output or not password:
            gui.popup_error("Please provide all required information.")
            continue

        try:
            if event == "Encrypt":
                crypto_utils.encrypt_file(file, output, password)
                gui.popup_success("File encrypted successfully!")
            elif event == "Decrypt":
                crypto_utils.decrypt_file(file, output, password)
                gui.popup_success("File decrypted successfully!")
        except Exception as e:
            gui.popup_error(f"An error occurred: {e}")

    window.close()

if __name__ == "__main__":
    main()
