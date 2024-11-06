import customtkinter
import backend

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Documenter")
        self.geometry("850x700")
        #customtkinter.set_default_color_theme("dark-blue")
        self.configure(fg_color="#000522")  
        self.iconbitmap('')
        self.grid_columnconfigure((0, 1), weight=1)
        self.button = customtkinter.CTkButton(self, text="my button", command=backend.button_clicked)
        self.button.grid(row=0, column=0, padx=20, pady=20, sticky="ew", columnspan=2)
        self.checkbox_1 = customtkinter.CTkCheckBox(self, text="checkbox 1")
        self.checkbox_1.grid(row=1, column=0, padx=20, pady=(0, 20), sticky="w")
        self.checkbox_2 = customtkinter.CTkCheckBox(self, text="checkbox 2")
        self.checkbox_2.grid(row=1, column=1, padx=20, pady=(0, 20), sticky="w")
        

