import customtkinter as tk
import modules.Application as application

class CalcWin(application.ApplicationWin):
    def __init__(self, root, main_window):
        super().__init__(root, main_window, window_title="Calculator", window_width=260, window_height=400, window_pos="nw")

        self.expression = ""  # To store the current expression
        self.max_display_length = 32  # Set a maximum length for the display

        self.display = tk.CTkLabel(self.root, text="0", anchor="e", width=240, height=50, corner_radius=0)
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=5, sticky="we")

        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0),              ('.', 4, 2), ('+', 4, 3), 
            ('C', 5, 0), ('(', 5, 1), (')', 5, 2), ('=', 5, 3)
        ]

        for (text, row, col) in buttons:
            columnspan = 2 if text == '0' else 1
            width = 118 if text == '0' else 40
            height = 50
            button = tk.CTkButton(self.root, text=text, command=lambda t=text: self.on_button_click(t), width=width, height=height, corner_radius=50)
            button.grid(row=row, column=col, columnspan=columnspan, padx=1, pady=5)

    def on_button_click(self, char):
        if char == "=":
            self.calculate()
        elif char == "C":
            self.clear()
        else:
            self.append_to_expression(char)

    def append_to_expression(self, char):
        self.expression += str(char)
        self.update_display()

    def update_display(self):
        # Truncate the display text if it exceeds max_display_length
        if len(self.expression) > self.max_display_length:
            display_text = self.expression[-self.max_display_length:]
        else:
            display_text = self.expression

        self.display.configure(text=display_text)

    def calculate(self):
        try:
            result = eval(self.expression)
            if isinstance(result, float):
                result = round(result, self.max_display_length - 2)  # -2 to account for the dot and possible sign
                result_str = f"{result:.{self.max_display_length - 2}g}"
            else:
                result_str = str(result)
            # Truncate the result if it exceeds max_display_length
            display_text = result_str if len(result_str) <= self.max_display_length else result_str[:self.max_display_length]
            self.display.configure(text=display_text)
            self.expression = result_str
        except Exception as e:
            self.display.configure(text="Error")
            self.expression = ""

    def clear(self):
        self.expression = ""
        self.update_display()