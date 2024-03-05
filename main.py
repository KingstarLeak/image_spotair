# import tkinter as 
from tkinter import filedialog
import customtkinter as ctk
from PIL import Image


# Fonctions
def get_nom(chemin):
    nom = ""
    for char in chemin:
        if char  == "/" or char == "\\":
            nom = ""
        else:
            nom += char
    return nom

def redim(l, h, img, dossier, nom):
    image= Image.open(img)
    size = (image.width, image.height)
    if size[0] > size[1]:
        if size[0] > l:
            ratio = size[0]/l
            size = (int(size[0] // ratio), int(size[1] // ratio))
        if size[1] > h:
            ratio = size[1]/h
            size = (int(size[0]*ratio // ratio), int(size[1] // ratio))
    else:
        if size[1] > l:
            ratio = size[1] / l
            size  = (int(size[0] // ratio), int(size[1]//ratio))
        if size[0] > h:
            ratio = size[0]/h
            size = (int(size[0]//ratio), int(size[1]//ratio))
    new_image = image.resize(size)
    new_image.save(f"{dossier}\\{nom}")

def string_to_list(chaine):
    chaine = chaine.replace('("', '')
    chaine = chaine.replace("('", '')
    chaine = chaine.replace("')", '')
    chaine = chaine.replace('")', '')
    chaine = chaine.replace(" '", '')
    chaine = chaine.replace("',", ",")
    chaine = chaine.split(sep=',')
    return chaine
# Programme principal -----------------------------------------------------------------------------------------------------------------------
class MainImage(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Mettre la fenêtre en mode plein écran
        self.after(0, lambda: self.wm_state('zoomed'))
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

        self.title("Redimmensionneur d'image")
        
        frame_north = ctk.CTkFrame(self)
        frame_south = ctk.CTkFrame(self)

        # Configurer la gestion de la géométrie des cadres
        frame_north.grid(row=0, column=0, columnspan=3, sticky="nsew")
        frame_south.grid(row=1, column=0, sticky="we", columnspan=3)


        # Configurer la gestion de la géométrie de la fenêtre principale
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(2, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=0)

        self.image = ctk.StringVar()
        self.choix_image = ctk.CTkButton(master=frame_north, text="Sélectionnez des images", command=self.ouvrir_boite_dialogue, width=300, height=80).pack(pady=(60, 15))
        self.dossier = ctk.StringVar()
        self.choix_dossier = ctk.CTkButton(master=frame_north, text="Sélectionnez un dossier d'arrivée", command=self.select_dossier, width=300, height=80).pack(pady=(10, 15))

        # Bouton quitter la fenêtre (placé dans la frame de droite)
        self.boutton_spotair = ctk.CTkButton(master=frame_south, text="Spot'Air", command=self.spotair).pack(anchor="s", padx=(0, 0), pady=(10, 10))

    def spotair(self):
        images = self.image.get()
        dossier = self.dossier.get()
        liste_image = string_to_list(images)
        for img in liste_image:
            name = get_nom(img)
            redim(1600, 1200, img, dossier, name)

    def ouvrir_boite_dialogue(self):
        # Ouvrir une boîte de dialogue de sélection de fichiers
        file = filedialog.askopenfilenames(title="Sélectionner une image", filetypes=[("Fichiers JPEG", "*.jpg;*.jpeg"), ("Tous les fichiers", "*.*")])
        # Vérifier si un fichier a été sélectionné
        if file:
            # Enregistrer le chemin du fichier dans la variable
            self.image.set(file)

    def select_dossier(self):
        dossier = filedialog.askdirectory(initialdir="/", title="Sélectionner un dossier")
        if dossier:
            # Enregistrer le chemin du fichier dans la variable
            self.dossier.set(dossier)

def launch_ajout():
    app = MainImage()
    app.mainloop()

launch_ajout()