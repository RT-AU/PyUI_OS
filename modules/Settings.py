import customtkinter as tk
import modules.Application as application

class SettingsWin(application.ApplicationWin):
    def __init__(self, root, main_window):
        super().__init__(root, main_window, window_title="Settings", window_width=300, window_height=300, window_pos="nw")  # Call the constructor of ApplicationWin

        ### Window Size Setting ###
        # Define a list of window sizes
        self.window_sizes = ["800x600", "1024x768", "1280x720", "1920x1080"]

        # Fetch the currently selected window size
        self.selected_size = tk.StringVar(value=self.main_window.geometry().split('+')[0])

        # Create the OptionMenu
        self.size_menu = tk.CTkOptionMenu(self.root, variable=self.selected_size, values=self.window_sizes, command=self.change_window_size)
        self.size_menu.pack(anchor="nw", padx = 10, pady = 10)

        
        ### Appearance Setting ###
        # Define a list of appearances
        self.appearances = ["Dark","Light"]
        # Fetch the currently selected appearance
        self.selected_appearance = tk.StringVar(value=tk.get_appearance_mode())

        self.appearance_menu = tk.CTkOptionMenu(self.root, variable=self.selected_appearance, values=self.appearances, command=self.change_appearance)
        self.appearance_menu.pack(anchor="nw", padx = 10, pady = 10)     


    def change_window_size(self, event):
        # This method is called when a size is selected from the dropdown menu
        self.main_window.geometry(self.selected_size.get())

    def change_appearance(self, event):
        tk.set_appearance_mode(self.selected_appearance.get())
    

    def settings(self):
        print("settings code goes here")