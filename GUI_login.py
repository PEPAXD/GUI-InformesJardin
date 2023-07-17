import os.path
import tkinter
import customtkinter
import mainScript
from PIL import ImageTk,Image

class LoginLabel(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
        customtkinter.set_default_color_theme("green")  # Themes: blue (default), dark-blue, green

        self.geometry("600x440")
        self.minsize(440, 440)
        self.title('Login')

        # wallpaper
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "Image")
        img1 = Image.open(os.path.join(image_path, "pattern.png"))
        img1 = ImageTk.PhotoImage(img1)

        l1 = customtkinter.CTkLabel(master=self, image=img1)
        l1.pack()

        # creating custom frame
        frame = customtkinter.CTkFrame(master=l1, width=320, height=360, corner_radius=15)
        frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        # Title
        l2 = customtkinter.CTkLabel(master=frame, text="INFORME EVALUATIVO", font=('Century Gothic', 20, "underline"))
        l2.place(x=52, y=25)

        # Create TextEntry-Data
        entry1 = customtkinter.CTkEntry(master=frame, width=220, placeholder_text='Nombre-Maestra')
        entry1.place(x=50, y=80)
        entry2 = customtkinter.CTkEntry(master=frame, width=220, placeholder_text='Nombre-Alumno')
        entry2.place(x=50, y=120)
        entry3 = customtkinter.CTkEntry(master=frame, width=220, placeholder_text='Nombre-Sala')
        entry3.place(x=50, y=160)

        # Create RadioButtonCheck
        radio_var = tkinter.IntVar(value=0)
        radio_button_1 = customtkinter.CTkRadioButton(master=frame, text="1 año", variable=radio_var, value=0)
        radio_button_1.place(x=60, y=215)
        radio_button_2 = customtkinter.CTkRadioButton(master=frame, text="2 año", variable=radio_var, value=1)
        radio_button_2.place(x=130, y=215)
        radio_button_3 = customtkinter.CTkRadioButton(master=frame, text="3 año", variable=radio_var, value=2)
        radio_button_3.place(x=200, y=215)

        # Create switch Ciclo
        switchText = customtkinter.CTkLabel(master=frame, text="Etapa °1")
        switchText.place(x=85, y=248)
        switch = customtkinter.CTkSwitch(master=frame, text="Etapa °2")
        switch.place(x=142, y=250)

        def nextWindow():
            self.destroy()
            mainScript.GUI_WorkLabel()

        # Create custom button
        button1 = customtkinter.CTkButton(master=frame, width=220, text="Login", command=nextWindow, corner_radius=6)
        button1.place(x=50, y=300)

def main():
    LoginLabel().mainloop()


