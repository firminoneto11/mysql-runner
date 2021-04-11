from tkinter import *
from tkinter import ttk
from time import sleep
from os import system
from lib.service_checker import check_win_service


class MainGui:

    @staticmethod
    def __turn_on():
        system("net start mysql80")

    @staticmethod
    def __turn_off():
        system("net stop mysql80")

    def __init__(self, window):
        """
        This __init__ method initializes the main widgets of the script gui.
        :param window: The main Tk object.
        """
        # Storing the main window object into an attribute
        self.root = window

        # Saving the service status into an attribute
        self.service_status = check_win_service()

        # If the service is stopped
        if self.service_status == 'stopped':
            # These widgets will be displayed if the mysql server is offline.
            self.main_label = Label(self.root, text=f'The MySQL server is currently offline. Would you like to turn '
                                                    f'it on?', font=('Helvetica', 16), fg='red', bg='#1C2541')
            self.frame_buttons = Frame(self.root, bg='#1C2541')
            self.yes_button = Button(self.frame_buttons, text='Yes', font=('Helvetica', 14), fg='white', bg='green',
                                     width=10, relief=FLAT, activebackground='#5BC0BE',
                                     command=lambda: self.__yes_pressed(current_status=False))
            self.no_button = Button(self.frame_buttons, text='No', font=('Helvetica', 14), fg='white', bg='red',
                                    width=10, command=self.__no_pressed, relief=FLAT, activebackground='#5BC0BE')

            # Packing
            self.main_label.pack(pady=100)
            self.frame_buttons.pack(pady=20)

            self.yes_button.grid(row=0, column=0, padx=5)
            self.no_button.grid(row=0, column=1, padx=5)
        # If the service is running
        elif self.service_status == 'running':
            # These widgets will be displayed if the mysql server is online.
            self.main_label = Label(self.root, text=f'The MySQL server is currently online. Would you like to turn '
                                                    f'it off?', font=('Helvetica', 16), fg='green', bg='#1C2541')

            self.frame_buttons = Frame(self.root, bg='#1C2541')
            self.yes_button = Button(self.frame_buttons, text='Yes', font=('Helvetica', 14), fg='white', bg='green',
                                     width=10, relief=FLAT, activebackground='#5BC0BE',
                                     command=lambda: self.__yes_pressed(current_status=True))
            self.no_button = Button(self.frame_buttons, text='No', font=('Helvetica', 14), fg='white', bg='red',
                                    width=10, command=self.__no_pressed, relief=FLAT, activebackground='#5BC0BE')

            # Packing
            self.main_label.pack(pady=100)
            self.frame_buttons.pack(pady=20)

            self.yes_button.grid(row=0, column=0, padx=5)
            self.no_button.grid(row=0, column=1, padx=5)
        # If an error occurred
        else:
            # These widgets will be displayed if the check_win_service() function returns an exception
            self.main_label = Label(self.root, text=self.service_status, font=('Helvetica', 16), fg='white',
                                    bg='#1C2541')
            self.close_button = Button(self.root, text='Exit', font=('Helvetica', 14), width=10, fg='white',
                                       bg='#3A506B', command=self.root.quit, relief=FLAT, activebackground='#5BC0BE')

            # Packing them onto the screen
            self.main_label.pack(pady=100)
            self.close_button.pack(pady=20)

    def __no_pressed(self):
        """
        This method is called when the 'No' button is pressed. When it's pressed, it destroys all the current widgets
        and creates a new label and an 'exit' button.
        :return: None
        """
        # Getting rid of the old widgets
        self.main_label.destroy()
        self.frame_buttons.destroy()

        # Creating the new widgets
        self.new_label = Label(self.root, text='See you next time!', font=('Helvetica', 16), fg='white', bg='#1C2541')
        self.close_button = Button(self.root, text='Exit', font=('Helvetica', 14), width=10, fg='white', bg='#3A506B',
                                   command=self.root.quit, relief=FLAT, activebackground='#5BC0BE')

        # Packing them onto the screen
        self.new_label.pack(pady=100)
        self.close_button.pack(pady=20)

    def __yes_pressed(self, current_status):
        """
        This method is called when the 'yes' button is pressed on either one of the screens that are displayed depending
        on the MySQL service current state.
        If the MySQL server is online, this method will turn it off, and if it's offline, it will turn it on.
        :param current_status: An boolean value. It's False if the MySQL server is offline and True if it's online.
        :return: None
        """
        if current_status is False:
            # Getting rid of the old widgets
            self.main_label.destroy()
            self.frame_buttons.destroy()

            # Executing the method that will turn on the MySQL server
            MainGui.__turn_on()

            # Styling the progress bar
            style = ttk.Style()
            style.theme_use('alt')
            style.configure('darkblue.Horizontal.TProgressbar', background='darkblue')

            # Creating and displaying a progress bar
            self.status_label = Label(self.root, text='Starting the MySQL server...', font=('Helvetica', 16),
                                      fg='#eeeeee', bg='#1C2541')
            self.progress_bar = ttk.Progressbar(self.root, mode='determinate', orient=HORIZONTAL, length=300,
                                                style='darkblue.Horizontal.TProgressbar')
            self.percentage_label = Label(self.root, text='0%', font=('Helvetica', 14), fg='#eeeeee', bg='#1C2541')

            # Placing the widgets onto the screen
            self.status_label.place(x=100, y=150)
            self.progress_bar.place(x=100, y=200)
            self.percentage_label.place(x=100, y=250)

            # Loading the progress bar
            for _ in range(100):
                self.progress_bar['value'] = self.progress_bar['value'] + 1
                self.percentage_label.config(text=f"{self.progress_bar['value']}%")
                self.root.update()
                sleep(0.050)

            # Cleaning the screen
            self.status_label.destroy()
            self.progress_bar.destroy()
            self.percentage_label.destroy()

            # Creating new widgets
            self.new_label = Label(self.root, text='MySQL Server was successfully started and is now online!',
                                   font=('Helvetica', 16), fg='white', bg='#1C2541')
            self.close_button = Button(self.root, text='Exit', font=('Helvetica', 14), width=10, fg='white',
                                       bg='#3A506B', command=self.root.quit, relief=FLAT,
                                       activebackground='#5BC0BE')

            # Packing them onto the screen
            self.new_label.pack(pady=100)
            self.close_button.pack(pady=20)
        else:
            # Getting rid of the old widgets
            self.main_label.destroy()
            self.frame_buttons.destroy()

            # Executing the method that will turn off the MySQL server
            MainGui.__turn_off()

            # Styling the progress bar
            style = ttk.Style()
            style.theme_use('alt')
            style.configure('darkblue.Horizontal.TProgressbar', background='darkblue')

            # Creating and displaying a progress bar
            self.status_label = Label(self.root, text='Shutting down the MySQL server...', font=('Helvetica', 16),
                                      fg='#eeeeee', bg='#1C2541')
            self.progress_bar = ttk.Progressbar(self.root, mode='determinate', orient=HORIZONTAL, length=300,
                                                style='darkblue.Horizontal.TProgressbar')
            self.percentage_label = Label(self.root, text='0%', font=('Helvetica', 14), fg='#eeeeee', bg='#1C2541')

            # Placing the widgets onto the screen
            self.status_label.place(x=100, y=150)
            self.progress_bar.place(x=100, y=200)
            self.percentage_label.place(x=100, y=250)

            # Loading the progress bar
            for _ in range(100):
                self.progress_bar['value'] = self.progress_bar['value'] + 1
                self.percentage_label.config(text=f"{self.progress_bar['value']}%")
                self.root.update()
                sleep(0.050)

            # Cleaning the screen
            self.status_label.destroy()
            self.progress_bar.destroy()
            self.percentage_label.destroy()

            # Creating new widgets
            self.new_label = Label(self.root, text='MySQL Server was successfully shut down and is now offline.',
                                   font=('Helvetica', 16), fg='white', bg='#1C2541')
            self.close_button = Button(self.root, text='Exit', font=('Helvetica', 14), width=10, fg='white',
                                       bg='#3A506B', command=self.root.quit, relief=FLAT,
                                       activebackground='#5BC0BE')

            # Packing them onto the screen
            self.new_label.pack(pady=100)
            self.close_button.pack(pady=20)
