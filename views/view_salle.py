import customtkinter as ctk
from services.service_salle import ServiceSalle


class ViewSalle(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.service_salle = ServiceSalle()

        self.title("Gestion des salles")
        self.geometry("750x550")

        self.cadreInfo = ctk.CTkFrame(self, corner_radius=10)
        self.cadreInfo.pack(pady=10, padx=10, fill="x")
