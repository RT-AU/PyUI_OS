import customtkinter as tk
import modules.Application as application

class SettingsWin(application.ApplicationWin):
    def __init__(self, root, main_window):
        super().__init__(root, main_window, window_title="Settings", window_width=300, window_height=300, window_pos="nw")  # Call the constructor of ApplicationWin
        # self.root = root
        # self.main_window = main_window
        # self.root.title("")
        # self.root.geometry("300x300")
        # self.root.resizable(False, False)
        # self.root.attributes('-topmost', True)  # This line makes the window appear over other windows

        # Define a list of window sizes
        self.window_sizes = ["800x600", "1024x768", "1280x720", "1920x1080"]

        # Create a string to hold the selected window size
        self.selected_size = tk.StringVar(value=self.window_sizes[0])

        # Create the OptionMenu
        self.size_menu = tk.CTkOptionMenu(self.root, variable=self.selected_size, values=self.window_sizes, command=self.change_window_size)
        self.size_menu.pack(anchor="nw", padx = 10, pady = 10)

    def change_window_size(self, event):
        # This method is called when a size is selected from the dropdown menu
        self.main_window.geometry(self.selected_size.get())

    def settings(self):
        print("settings code goes here")