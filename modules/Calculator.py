import customtkinter as ctk
# import tkinter as ctk

def create_gui():
    ctk.set_appearance_mode("Dark")
    ctk.set_default_color_theme("dark-blue")

    root = ctk.CTk()
    root.geometry("500x350")
    root.title("PyUI_OS")

    def login():
        print("Test")

    frame = ctk.CTkFrame(master=root)
    frame.pack(pady=20, padx=60, fill="both", expand=True)

    label = ctk.CTkLabel(master=frame, text = "Welcome to PyUI_OS")
    label.pack(pady=12, padx=10)

    entry1 = ctk.CTkEntry(master=frame, placeholder_text="Username")
    entry1.pack(pady=12, padx=10)

    entry2 = ctk.CTkEntry(master=frame, placeholder_text="Password", show="*")
    entry2.pack(pady=12, padx=10)

    button = ctk.CTkButton(master=frame,text="Login", command=login)
    button.pack(pady=12, padx=10)

    checkbox = ctk.CTkCheckBox(master=frame, text="Remember Me")
    checkbox.pack(pady=12, padx=10)
    root.mainloop()

######################

# root=ctk.Tk()
# root.geometry("500x350")

# def login():
#     print("Test")

# frame = ctk.Frame(master=root)
# frame.pack(pady=20, padx=60, fill="both", expand=True)

# label = ctk.Label(master=frame, text = "Login System")
# label.pack(pady=12, padx=10)

# entry1 = ctk.Entry(master=frame, textvariable="Username")
# entry1.pack(pady=12, padx=10)

# entry2 = ctk.Entry(master=frame,textvariable="Password", show="*")
# entry2.pack(pady=12, padx=10)

# button = ctk.Button(master=frame,text="Login", command=login)
# button.pack(pady=12, padx=10)

# checkbox = ctk.Checkbutton(master=frame, text="Remember Me")
# checkbox.pack(pady=12, padx=10)


