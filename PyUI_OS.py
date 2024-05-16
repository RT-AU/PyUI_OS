import customtkinter as tk
import modules.Calculator as calculator
import modules.NetBrowser as netbrowser
import modules.Notebook as notebook
import modules.Settings as settings
from PIL import Image, ImageTk

class MainApplication:
    def __init__(self, root):
        self.root = root
        self.root.title("PyUI_OS")
        self.root.width = 800
        self.root.height = 600
        self.root.geometry(f"{self.root.width}x{self.root.height}")
        self.root.resizable(False, False)
        
        # Create a Frame for the taskbar
        self.taskbar = tk.CTkFrame(self.root)
        self.taskbar.pack(side="bottom", fill="x")

        # # Add buttons to the taskbar
        # self.open_calculator_button = tk.CTkButton(self.taskbar, text="Open Calculator", command=self.open_calculator)
        # self.open_calculator_button.pack(side="left")

        # Create start menu button on the taskbar
        self.start_menu = tk.CTkButton(self.taskbar, text="Start", command=self.open_start_menu, width=85, corner_radius=0)
        self.start_menu.pack(side="left")

        # Keep track of open windows on taskbar
        self.open_windows = {}

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

    # Create a Window/Instance of the net browser app
    def open_net_browser_window(self):
        net_browser_window = tk.CTkToplevel(root)
        netbrowser.NetBrowserWin(net_browser_window, root)
        
    # Create a Window/Instance of the settings app
    def open_settings_window(self):
        settings_window = tk.CTkToplevel(root)
        settings.SettingsWin(settings_window, root)

    def open_start_menu(self):
        print("start menu")


if __name__ == "__main__":
    tk.set_appearance_mode("dark")
    tk.set_default_color_theme("dark-blue")
    root = tk.CTk()
    app = MainApplication(root)
    root.mainloop()
