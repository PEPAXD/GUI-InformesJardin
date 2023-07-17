import tkinter
import customtkinter

#LIBRARY GUI_AddKids
#------------------------------------------------------------------------------------------------------
class ScrollableCheckBoxFrame(customtkinter.CTkScrollableFrame):
    def __init__(self, master, item_list, command=None, **kwargs):
        super().__init__(master, **kwargs)

        #CREATE SCROLLBOX
        self.command = command
        self.checkbox_list = []
        for i, item in enumerate(item_list):
            self.add_item(item)

    def add_item(self, item):
        checkbox = customtkinter.CTkCheckBox(self, text=item,)
        if self.command is not None:
            checkbox.configure(command=self.command)
        checkbox.grid(row=len(self.checkbox_list), column=0, pady=(0, 10))
        self.checkbox_list.append(checkbox)

    def remove_item(self):
        for checkbox in self.checkbox_list:
            if checkbox.get() == 1:
                checkbox.destroy()
                self.checkbox_list.remove(checkbox)
        return

    def get_checked_items(self):
        return [checkbox.cget("text") for checkbox in self.checkbox_list if checkbox.get() == 1]
#----------------------------------------------------------------------------------------------------
class LoginLabel(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
        customtkinter.set_default_color_theme("green")  # Themes: blue (default), dark-blue, green

        # set grid layout 1x2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # configure window size
        self.geometry(f"{400}x{650}")

        # create HomeFrame
        self.HomeFrame = customtkinter.CTkFrame(self, corner_radius=0)
        self.HomeFrame.grid(row=0, column=1, padx=30, pady=30, sticky="nsew")

        # TEXT-LABEL
        self.label = customtkinter.CTkLabel(master=self.HomeFrame, text="INFORMES ALUMNOS",
                                            font=("Arial Black", 22, "underline"))
        self.label.place(relx=0.5, rely=0.04, anchor=tkinter.CENTER)

        # TEXT-LABEL
        self.label2 = customtkinter.CTkLabel(master=self.HomeFrame, text="SALA XXXXXXXXXX", font=("Arial Black", 22))
        self.label2.place(relx=0.5, rely=0.10, anchor=tkinter.CENTER)

        # CHANGE-TEXT
        NameKidsRoom = '"SALA PATITO"'
        self.label2.configure(text=str(NameKidsRoom))

        # ADD-KIDS-BUTTON
        self.home_frame_button_2 = customtkinter.CTkButton(self.HomeFrame, width=290, corner_radius=5,
                                                           border_spacing=7, border_width=2,
                                                           fg_color="transparent", text_color=("gray10", "gray90"),
                                                           text="AGREGAR NUEVO ALUMNO",
                                                           font=customtkinter.CTkFont(size=15, weight="bold"),
                                                           command=self.AddKidToList)

        self.home_frame_button_2.place(relx=0.5, rely=0.86, anchor=tkinter.CENTER)

        # create scrollable checkbox frame
        self.scrollable_checkbox_frame = ScrollableCheckBoxFrame(master=self.HomeFrame, width=280, height=370,
                                                                 item_list=[f"item {i}" for i in range(0)])
        self.scrollable_checkbox_frame.place(relx=0.5, rely=0.48, anchor=tkinter.CENTER)

        # REMOVE-KIDS-BUTTON
        self.home_frame_button_2 = customtkinter.CTkButton(self.HomeFrame, width=290, corner_radius=5,
                                                           border_spacing=7, border_width=2,
                                                           fg_color="transparent", text_color=("gray10", "gray90"),
                                                           text="BORRAR ALUMNO",
                                                           hover_color="darkred",
                                                           font=customtkinter.CTkFont(size=15, weight="bold"),
                                                           command=self.RemoveKidToList)

        self.home_frame_button_2.place(relx=0.5, rely=0.94, anchor=tkinter.CENTER)

    #ADD KID TO LIST
    def AddKidToList(self):

        dialog = customtkinter.CTkInputDialog(text="NOMBRE ALUMNO", title="ADD-KID")
        KidsName = dialog.get_input()

        if KidsName != None:
            if KidsName != "":
                self.scrollable_checkbox_frame.add_item(str(KidsName.upper()))

    #REMOVE KID TO LIST
    def RemoveKidToList(self):
        name = "TOMAS"
        self.scrollable_checkbox_frame.remove_item()


def main():
    LoginLabel().mainloop()

if __name__ == '__main__':
    main()