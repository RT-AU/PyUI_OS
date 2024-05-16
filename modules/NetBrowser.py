import customtkinter as tk
import modules.Application as application

class NetBrowserWin(application.ApplicationWin):
    def __init__(self, root, main_window):
        super().__init__(root, main_window, window_title="Net Browser", window_width=800, window_height=600, window_pos="nw")  # Call the constructor of ApplicationWin

        # self.root = root
        # self.root.title("")
        # self.root.geometry("800x600")
        # self.root.resizable(False, False)
        # self.root.attributes('-topmost', True)  # This line makes the window appear over other windows

     

    def browser(self):
        print("Browser code goes here")