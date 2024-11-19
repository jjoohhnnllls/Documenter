import customtkinter
from PIL import Image
import backend

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Documenter")
        self.geometry("850x650")
        customtkinter.set_default_color_theme("dark-blue")
        self.configure(fg_color="#000522")  
        self.iconbitmap('')
        #configure grid 
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_columnconfigure(3, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)

        #title
        self.title_label = customtkinter.CTkLabel(self, text="Documenter",font=("Kafka", 24,"bold"))
        self.title_label.place(x=50,y=50)
    
        #subtitle
        self.subtitle = customtkinter.CTkLabel(self, text= "choose a template", font=("Arial",20))
        self.subtitle.place(x=350,y=150)


        #load images
        self.image_O1 = customtkinter.CTkImage(light_image=Image.open("resources/O1.png"), size=(250, 250))
        self.image_O2 = customtkinter.CTkImage(light_image=Image.open("resources/O2.png"), size=(250, 250))
        #first option button
        self.button_option_1 = customtkinter.CTkButton(self, image=self.image_O1, command= backend.button_clicked,text="", fg_color="#000522" , hover_color="#484F7D",corner_radius=20)
        self.button_option_1.grid(row=1, column=1)
        #2nd option button
        self.button_option_2 = customtkinter.CTkButton(self, image=self.image_O2, command= backend.button_clicked,text="", fg_color="#000522" , hover_color="#484F7D",corner_radius=20)
        self.button_option_2.grid(row=1, column=2)


   
    


        

