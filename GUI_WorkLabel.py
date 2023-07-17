import tkinter
import GUI_AddKids
import customtkinter
import os
from PIL import ImageTk, Image

class WorkLabel(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
        customtkinter.set_default_color_theme("green")  # Themes: blue (default), dark-blue, green

        # configure window size
        self.geometry(f"{650}x{650}")

        # min window size
        self.minsize(650, 650)

        # FULL-SCREEN
        #self.after(0, lambda: self.state('zoomed'))

        # Configure window title
        self.title("DataGeneratorDOCX_JardinEstrellitas.py")

        # configure expand Windows_False
        # self.resizable(False, False)

        # set grid layout 1x2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # create navigation frame
        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(8, weight=1)

        # load images ---> Image_folder
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "Image")
        self.logo_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "EstrellitaLogo.png")),
                                                 size=(60, 60))
        self.BasicData = customtkinter.CTkImage(Image.open(os.path.join(image_path, "kidsPerfil.png")), size=(30, 30))
        self.AreaCognitiva = customtkinter.CTkImage(Image.open(os.path.join(image_path, "AreaCognitiva.png")),
                                                    size=(30, 30))
        self.AreaPsicomotriz = customtkinter.CTkImage(Image.open(os.path.join(image_path, "AreaPsicomotriz.png")),
                                                      size=(30, 30))
        self.LenguajeComunicacion = customtkinter.CTkImage(
            Image.open(os.path.join(image_path, "LenguajeComunicacion.png")), size=(30, 30))
        self.ExpresionPlastica = customtkinter.CTkImage(Image.open(os.path.join(image_path, "ExpresionPlastica.png")),
                                                        size=(30, 30))
        self.AreaLudica = customtkinter.CTkImage(Image.open(os.path.join(image_path, "AreaLudica.png")), size=(30, 30))
        self.Observaciones = customtkinter.CTkImage(Image.open(os.path.join(image_path, "Observaciones.png")),
                                                        size=(30, 30))

        # create logoFrame
        self.navigation_frame_label = customtkinter.CTkLabel(self.navigation_frame, text=" JARDIN ESTRELLITAS   ",
                                                             image=self.logo_image,
                                                             compound="left",
                                                             font=customtkinter.CTkFont(size=15, weight="bold"))
        self.navigation_frame_label.grid(row=0, column=0, padx=5, pady=5)

        # create kidsLogoPerfil
        self.BasicData = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10,
                                                 text="Perfil Niño/a",
                                                 fg_color="transparent", text_color=("gray10", "gray90"),
                                                 hover_color=("gray70", "gray30"),
                                                 font=customtkinter.CTkFont(size=15),
                                                 image=self.BasicData, anchor="w", command=self.BasicData_button_event)
        self.BasicData.grid(row=1, column=0, sticky="nsew")

        # create AreaCognitiva
        self.AreaCognitiva = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40,
                                                     border_spacing=10,
                                                     text="Area Cognitiva",
                                                     fg_color="transparent", text_color=("gray10", "gray90"),
                                                     hover_color=("gray70", "gray30"),
                                                     font=customtkinter.CTkFont(size=15),
                                                     image=self.AreaCognitiva, anchor="w",
                                                     command=self.AreaCognitiva_button_event)
        self.AreaCognitiva.grid(row=2, column=0, sticky="ew")

        # create AreaPsicomotriz
        self.AreaPsicomotriz = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40,
                                                       border_spacing=10,
                                                       text="Area Psicomotriz",
                                                       fg_color="transparent", text_color=("gray10", "gray90"),
                                                       hover_color=("gray70", "gray30"),
                                                       font=customtkinter.CTkFont(size=15),
                                                       image=self.AreaPsicomotriz, anchor="w",
                                                       command=self.AreaPsicomotriz_button_event)
        self.AreaPsicomotriz.grid(row=3, column=0, sticky="ew")

        # create LenguajeComunicacion
        self.LenguajeComunicacion = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40,
                                                            border_spacing=10,
                                                            text="Lenguaje y Comunicacion",
                                                            fg_color="transparent", text_color=("gray10", "gray90"),
                                                            hover_color=("gray70", "gray30"),
                                                            font=customtkinter.CTkFont(size=15),
                                                            image=self.LenguajeComunicacion, anchor="w",
                                                            command=self.LenguajeComunicacion_button_event)
        self.LenguajeComunicacion.grid(row=4, column=0, sticky="ew")

        # create ExpresionPlastica
        self.ExpresionPlastica = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40,
                                                         border_spacing=10,
                                                         text="Expresíon Plástica",
                                                         fg_color="transparent", text_color=("gray10", "gray90"),
                                                         hover_color=("gray70", "gray30"),
                                                         font=customtkinter.CTkFont(size=15),
                                                         image=self.ExpresionPlastica, anchor="w",
                                                         command=self.ExpresionPlastica_button_event)
        self.ExpresionPlastica.grid(row=5, column=0, sticky="ew")

        # create AreaLudica
        self.AreaLudica = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10,
                                                  text="Área Lúdica",
                                                  fg_color="transparent", text_color=("gray10", "gray90"),
                                                  hover_color=("gray70", "gray30"),
                                                  font=customtkinter.CTkFont(size=15),
                                                  image=self.AreaLudica, anchor="w",
                                                  command=self.AreaLudica_button_event)
        self.AreaLudica.grid(row=6, column=0, sticky="ew")

        # create observaciones
        self.Observaciones = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40,
                                                     border_spacing=10,
                                                     text="Observaciones Docente",
                                                     fg_color="transparent", text_color=("gray10", "gray90"),
                                                     hover_color=("gray70", "gray30"),
                                                     font=customtkinter.CTkFont(size=15),
                                                     image=self.Observaciones, anchor="w",
                                                     command=self.Observaciones_button_event)
        self.Observaciones.grid(row=7, column=0, sticky="ew")

        # create printDocsButton
        self.printDocsButton = customtkinter.CTkButton(self.navigation_frame, width=220, corner_radius=5,
                                                       border_spacing=7, border_width=2,
                                                       fg_color="transparent", text_color=("gray10", "gray90"),
                                                       text="GUARDAR INFORME",
                                                       font=customtkinter.CTkFont(size=15, weight="bold"),
                                                       command=self.printDocsButton_button_event)
        self.printDocsButton.grid(row=8, column=0, pady=20, sticky="s")

        # select default frame
        self.select_frame_by_name("Perfil Niño/a")

    # SetButton
    def select_frame_by_name(self, name):
        # set button color for selected button
        self.BasicData.configure(fg_color=("gray75", "gray25") if name == "Perfil Niño/a" else "transparent")
        self.AreaCognitiva.configure(fg_color=("gray75", "gray25") if name == "Area Cognitiva" else "transparent")
        self.AreaPsicomotriz.configure(fg_color=("gray75", "gray25") if name == "Area Psicomotriz" else "transparent")
        self.LenguajeComunicacion.configure(
            fg_color=("gray75", "gray25") if name == "Lenguaje y Comunicacion" else "transparent")
        self.ExpresionPlastica.configure(
            fg_color=("gray75", "gray25") if name == "Expresíon Plástica" else "transparent")
        self.AreaLudica.configure(fg_color=("gray75", "gray25") if name == "Área Lúdica" else "transparent")
        self.Observaciones.configure(
            fg_color=("gray75", "gray25") if name == "Observaciones Docente" else "transparent")

    # Trigger Button_KidsData
    def BasicData_button_event(self):
        self.select_frame_by_name("Perfil Niño/a")
        print("CHECK KIDS PERFIL BUTTON")

        #GUI_AddKids.main()

    # Trigger Button_AreaCognitiva
    def AreaCognitiva_button_event(self):
        self.select_frame_by_name("Area Cognitiva")
        print("CHECK AREA COGNITIVA BUTTON")

    # Trigger Button_AreaPsicomotriz
    def AreaPsicomotriz_button_event(self):
        self.select_frame_by_name("Area Psicomotriz")
        print("CHECK AREA PSICOMOTRIZ BUTTON")

    # Trigger Button_AreaPsicomotriz
    def LenguajeComunicacion_button_event(self):
        self.select_frame_by_name("Lenguaje y Comunicacion")
        print("CHECK AREA COMUNICACION BUTTON")

    # Trigger Button_Expresíon Plástica
    def ExpresionPlastica_button_event(self):
        self.select_frame_by_name("Expresíon Plástica")
        print("CHECK AREA PLASTICA BUTTON")

    # Trigger Button_AreaLudica
    def AreaLudica_button_event(self):
        self.select_frame_by_name("Área Lúdica")
        print("CHECK AREA LUDICA BUTTON")

    # Trigger Button_AreaLudica
    def Observaciones_button_event(self):
        self.select_frame_by_name("Observaciones Docente")
        print("CHECK OBSERVACIONES BUTTON")

    def printDocsButton_button_event(self):
        print("CHECK PRINT BUTTON")

def main():
    WorkLabel().mainloop()

if __name__ == '__main__':
    main()