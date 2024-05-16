import customtkinter as tk
import modules.Application as application
class CalcWin(application.ApplicationWin):
    def __init__(self, root, main_window):

        super().__init__(root, main_window, window_title="Calculator", window_width=300, window_height=450, window_pos="nw")  # Call the constructor of ApplicationWin and pass in the reference for the main window, width and height

        # self.root.title()
        

        # self.root.geometry("300x450")
        
        # self.root.attributes('-topmost', True)  # This line makes the window appear over other windows

        display = tk.CTkLabel(self.root, text="000,000,000")
        display.pack()

    def calculation(self):
        print("Calculation goes here")