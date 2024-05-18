import customtkinter as tk
import modules.Calculator as calculator
import modules.NetBrowser as netbrowser
import modules.Notebook as notebook
import modules.Settings as settings
from datetime import datetime
from PIL import Image, ImageTk
from PyQt5.QtWidgets import QApplication
import threading

class MainApplication:
    def __init__(self, root):
        self.root = root
        self.root.title("PyUI_OS")
        self.root.width = 800
        self.root.height = 600
        self.root.geometry(f"{self.root.width}x{self.root.height}")
        self.root.resizable(False, False)
        self.root.theme = tk.StringVar(value="Dark-Blue")
        
        # Create a Frame for the taskbar
        self.taskbar = tk.CTkFrame(self.root)
        self.taskbar.pack(side="bottom", fill="x")


        # Create shutdown button on the taskbar
        self.start_menu = tk.CTkButton(self.taskbar, text="Shutdown", command=self.shutdown, width=50, height=30, corner_radius=10, fg_color="#5b0600", text_color="#C0C0C0")
        self.start_menu.pack(side="left", padx = 3)
           
        
        # Create Clock label on taskbar
        self.clock = tk.CTkLabel(self.taskbar, text="", width=85, corner_radius=0)
        self.clock.pack(side="right")

        self.update_clock() # begin clock updating time

        # Add a placeholder widget to push the buttons down
        placeholder = tk.CTkLabel(self.root, text="", height=0)
        placeholder.pack()

        # Define Button Images
        calculator_image = ImageTk.PhotoImage(Image.open("res/icon.png").resize((100,100)))

        # Add buttons to open child windows    
        self.open_calculator_button = tk.CTkButton(self.root, text="Calculator", command=self.open_calculator_window, width=85, height=50, corner_radius=0, image=calculator_image, compound="top")
        self.open_calculator_button.pack(anchor="nw", padx = 10, pady = 10)

        self.open_text_editor_button = tk.CTkButton(self.root, text="Notebook", command=self.open_notebook_window, width=85, height=50, corner_radius=0)
        self.open_text_editor_button.pack(anchor="nw", padx = 10, pady = 10)

        self.open_net_browser_button = tk.CTkButton(self.root, text="Net Browser", command=self.open_net_browser_window, width=85, height=50, corner_radius=0)
        self.open_net_browser_button.pack(anchor="nw", padx = 10, pady = 10)

        self.open_settings_button = tk.CTkButton(self.root, text="Settings", command=self.open_settings_window, width=85, height=50, corner_radius=0)
        self.open_settings_button.pack(anchor="nw", padx = 10, pady = 10)

    # Create a Window/Instance of the calculator app
    def open_calculator_window(self):
        calculator_window = tk.CTkToplevel(root)
        calculator.CalcWin(calculator_window, root)

    # Create a Window/Instance of the notebook app
    def open_notebook_window(self):
        notebook_window = tk.CTkToplevel(root)
        notebook.NotebookWin(notebook_window, root)

    # Create an instance of the PyQt5 web browser window on a seperate thread, as both tkinter and PyQt5 run their own loops
    def open_net_browser_window(self):
        def start_qt_app():
            self.app = QApplication([])
            self.window = netbrowser.NetBrowserWin()
            self.window.open_browser()
            self.app.exec_()
        threading.Thread(target=start_qt_app).start()

    def open_settings_window(self):
        settings_window = tk.CTkToplevel(root)
        settings.SettingsWin(settings_window, root)

    def shutdown(self):
        self.root.quit()

    def update_clock(self):
        system_time = datetime.now().strftime("%H:%M:%S %p\n%a %d/%m/%Y ") # set the clock time and date format and value
        self.clock.configure(text = system_time) # Update the clock
        self.root.after(1000, self.update_clock) # Schedule the update_clock method to be called again after 1000ms (every second)

if __name__ == "__main__":
    
    root = tk.CTk()
    app = MainApplication(root)
    tk.set_appearance_mode("dark")
    tk.set_default_color_theme("dark-blue")
    root.mainloop()
