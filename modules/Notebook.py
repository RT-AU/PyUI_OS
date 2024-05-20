import customtkinter as tk
import modules.Application as application

class NotebookWin(application.ApplicationWin):
    def __init__(self, root, main_window):
        super().__init__(root, main_window, window_title="Notebook", window_width=800, window_height=600, window_pos="nw")  # Call the constructor of ApplicationWin
        
        self.placeholder = tk.CTkLabel(root, text = "Currently Under Development")
        self.placeholder.pack(pady=20)
        

     

    def notebook(self):
        print("notebook code goes here")