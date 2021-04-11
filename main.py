from lib.center_window import centralize
from gui.main_gui import MainGui
from tkinter import Tk, messagebox


def main():
    """
    This is the main function of the mysql runner script.
    :return: None
    """
    try:
        # Initializing the root element
        main_window = Tk()
        main_window.title('MySQL Runner')
        main_window.iconbitmap(r'.\sql_icon.ico')
        main_window.resizable(False, False)
        main_window.config(bg='#1C2541')
        centralize(width=800, height=400, root_window=main_window)

        # Initializing the main widgets of the GUI
        MainGui(window=main_window)

        # Mainloop
        main_window.mainloop()
    except Exception as error:
        messagebox.showerror('An error occurred', f'An error occurred when trying to initialize the script GUI.\nMore '
                                                  f'details: {error}.')
