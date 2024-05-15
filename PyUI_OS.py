import customtkinter as tk
import modules.Calculator as calculator

#import tkinter as tk

class MainApplication:
    def __init__(self, root):
        self.root = root
        self.root.title("PyUI_OS")
        self.root.geometry("800x600")
        self.root.resizable(False, False)

        # Define a list of window sizes
        self.window_sizes = ["800x600", "1024x768", "1280x720", "1920x1080"]

        # Create a string to hold the selected window size
        self.selected_size = tk.StringVar(value=self.window_sizes[0])

        # Create the OptionMenu
        self.size_menu = tk.CTkOptionMenu(self.root, variable=self.selected_size, values=self.window_sizes, command=self.change_window_size)
        self.size_menu.pack()
        
        # self.change_window_size()

        # Create a Frame for the taskbar
        self.taskbar = tk.CTkFrame(self.root)
        self.taskbar.pack(side="bottom", fill="x")

        # # Add buttons to the taskbar
        # self.open_calculator_button = tk.CTkButton(self.taskbar, text="Open Calculator", command=self.open_calculator)
        # self.open_calculator_button.pack(side="left")

        # Create start menu button on the taskbar
        self.start_menu = tk.CTkButton(self.taskbar, text="Start", command=self.open_calculator, width=85, corner_radius=0)
        self.start_menu.pack(side="left")

        # Keep track of open windows on taskbar
        self.open_windows = {}

        # Add a placeholder widget to push the buttons down
        placeholder = tk.CTkLabel(self.root, text="", height=0)
        placeholder.pack()
        # Add buttons to open child windows
        self.open_calculator_button = tk.CTkButton(self.root, text="Calculator", command=self.open_calculator, width=75, height=50, corner_radius=0)
        self.open_calculator_button.pack(anchor="nw", padx = 10, pady = 10)

        self.open_text_editor_button = tk.CTkButton(self.root, text="Notebook", command=self.open_calculator, width=75, height=50, corner_radius=0)
        self.open_text_editor_button.pack(anchor="nw", padx = 10, pady = 10)

        self.open_internet_browser_button = tk.CTkButton(self.root, text="Internet", command=self.open_calculator, width=75, height=50, corner_radius=0)
        self.open_internet_browser_button.pack(anchor="nw", padx = 10, pady = 10)

        self.open_settings_button = tk.CTkButton(self.root, text="Settings", command=self.open_calculator, width=75, height=50, corner_radius=0)
        self.open_settings_button.pack(anchor="nw", padx = 10, pady = 10)

        
    def change_window_size(self, event):
        # This method is called when a size is selected from the dropdown menu
        self.root.geometry(self.selected_size.get())

    def open_calculator(self):
        calculator_window = tk.CTkToplevel(self.root)
        calculator_window.title("Calculator")
        calculator_window.geometry("200x200")
        calculator_window.attributes('-topmost', True)  # This line makes the 

        # Add calculator GUI components and functionalities
        # ...


if __name__ == "__main__":
    root = tk.CTk()
    app = MainApplication(root)
    root.mainloop()
