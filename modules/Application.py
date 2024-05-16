import customtkinter as tk

class ApplicationWin:  # This is the parent class of the OS applications
    def __init__(self, root, main_window, window_title, window_width, window_height, window_pos="center"):
        self.root = root
        self.main_window = main_window
        self.root.title(window_title)
        self.window_width = window_width
        self.window_height = window_height

        # self.root.geometry(f"{window_width}x{window_height}")
        self.root.resizable(False, False)
        
        self.root.attributes('-topmost', True)  # This line makes the window appear over other windows

        # Get the main window's position and size
        x = self.main_window.winfo_x()
        y = self.main_window.winfo_y()

        match window_pos:
            case "center": # in the case of no open position being defined, open in center
                width = self.main_window.winfo_width()
                height = self.main_window.winfo_height()
                # Calculate the position of the child window
                child_x = x + width//2 - (self.window_width//2)  # half the width of the child window
                child_y = y + height//2 - (self.window_height//2)  # half the height of the child window
            case "nw":
                # Define the buffer distance
                buffer_x = 200  # Buffer distance from the left edge of the main window
                buffer_y = 95  # Buffer distance from the top edge of the main window

                # Calculate the position of the child window
                child_x = x + buffer_x
                child_y = y + buffer_y

        # Set the position of the child window
        self.root.geometry(f"{window_width}x{window_height}+{child_x}+{child_y}")

  