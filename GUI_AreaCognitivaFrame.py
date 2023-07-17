import tkinter
import customtkinter

class LoginLabel(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
        customtkinter.set_default_color_theme("green")  # Themes: blue (default), dark-blue, green

        # set grid layout 1x2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # configure window size
        self.geometry(f"{450}x{650}")

        # create HomeFrame
        self.HomeFrame = customtkinter.CTkFrame(self, corner_radius=0)
        self.HomeFrame.grid(row=0, column=1, padx=30, pady=30, sticky="nsew")

        # TEXT-LABEL
        self.label = customtkinter.CTkLabel(master=self.HomeFrame, text="CRITERIOS E INDICADORES",
                                            font=("Arial Black", 22, "underline"))
        self.label.place(relx=0.5, rely=0.04, anchor=tkinter.CENTER)

        # TEXT-LABEL2
        self.label2 = customtkinter.CTkLabel(master=self.HomeFrame, text="ÁREA COGNITIVA", font=("Arial Black", 22))
        self.label2.place(relx=0.5, rely=0.10, anchor=tkinter.CENTER)




def main():
    LoginLabel().mainloop()

if __name__ == '__main__':
    main()