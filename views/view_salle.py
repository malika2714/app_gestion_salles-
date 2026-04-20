import customtkinter as ctk
from tkinter import messagebox
from models.salle import Salle
from services.service_salle import ServiceSalle


class ViewSalle(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.service_salle = ServiceSalle()

        self.title("Gestion des salles")
        self.geometry("750x550")

        self.cadreInfo = ctk.CTkFrame(self, corner_radius=10)
        self.cadreInfo.pack(pady=10, padx=10, fill="x")

        self.label_code = ctk.CTkLabel(self.cadreInfo, text="Code salle")
        self.label_code.grid(row=0, column=0, padx=10, pady=10)

        self.entry_code = ctk.CTkEntry(self.cadreInfo)
        self.entry_code.grid(row=0, column=1, padx=10, pady=10)

        self.label_libelle = ctk.CTkLabel(self.cadreInfo, text="Libellé")
        self.label_libelle.grid(row=1, column=0, padx=10, pady=10)

        self.entry_libelle = ctk.CTkEntry(self.cadreInfo)
        self.entry_libelle.grid(row=1, column=1, padx=10, pady=10)

        self.label_type = ctk.CTkLabel(self.cadreInfo, text="Type")
        self.label_typee.grid(row=2, column=0, padx=10, pady=10)

        self.entry_typee = ctk.CTkEntry(self.cadreInfo)
        self.entry_typee.grid(row=2, column=1, padx=10, pady=10)

        self.label_capacite = ctk.CTkLabel(self.cadreInfo, text="Capacité")
        self.label_capacite.grid(row=3, column=0, padx=10, pady=10)

        self.entry_capacite = ctk.CTkEntry(self.cadreInfo)
        self.entry_capacite.grid(row=3, column=1, padx=10, pady=10)

        self.cadreAction = ctk.CTkFrame(self, corner_radius=10)
        self.cadreAction.pack(pady=10, padx=10, fill="x")

        self.btn_ajouter = ctk.CTkButton(self.cadreAction, text="Ajouter")
        self.btn_ajouter.grid(row=0, column=0, padx=10, pady=10)

        self.btn_modifier = ctk.CTkButton(self.cadreAction, text="Modifier")
        self.btn_modifier.grid(row=0, column=1, padx=10, pady=10)

        self.btn_supprimer = ctk.CTkButton(self.cadreAction, text="Supprimer")
        self.btn_supprimer.grid(row=0, column=2, padx=10, pady=10)

        self.btn_rechercher = ctk.CTkButton(self.cadreAction, text="Rechercher")
        self.btn_rechercher.grid(row=0, column=3, padx=10, pady=10)

    def vider_champs(self):
        self.entry_code.delete(0, "end")
        self.entry_libelle.delete(0, "end")
        self.entry_typee.delete(0, "end")
        self.entry_capacite.delete(0, "end")

    def ajouter_salle(self):
        salle = Salle(
            self.entry_code.get(),
            self.entry_libelle.get(),
            self.entry_typee.get(),
            self.entry_capacite.get()
        )

        succes, message = self.service_salle.ajouter_salle(salle)
        if succes:
            messagebox.showinfo("Succès", message)
            self.vider_champs()
        else:
            messagebox.showerror("Erreur", message)

        self.btn_ajouter = ctk.CTkButton(self.cadreAction, text="Ajouter", command=self.ajouter_salle)

        def modifier_salle(self):
            salle = Salle(
                self.entry_code.get(),
                self.entry_libelle.get(),
                self.entry_type.get(),
                self.entry_capacite.get()
            )

            succes, message = self.service_salle.modifier_salle(salle)
            if succes:
                messagebox.showinfo("Succès", message)
                self.vider_champs()
            else:
                messagebox.showerror("Erreur", message)

        self.btn_modifier = ctk.CTkButton(self.cadreAction, text="Modifier", command=self.modifier_salle)

        def supprimer_salle(self):
            code = self.entry_code.get()
            succes, message = self.service_salle.supprimer_salle(code)

            if succes:
                messagebox.showinfo("Succès", message)
                self.vider_champs()
            else:
                messagebox.showerror("Erreur", message)

        self.btn_supprimer = ctk.CTkButton(self.cadreAction, text="Supprimer", command=self.supprimer_salle)

        def rechercher_salle(self):
            code = self.entry_code.get()
            salle = self.service_salle.rechercher_salle(code)

            if salle:
                self.entry_libelle.delete(0, "end")
                self.entry_libelle.insert(0, salle.libelle)

                self.entry_type.delete(0, "end")
                self.entry_type.insert(0, salle.type)

                self.entry_capacite.delete(0, "end")
                self.entry_capacite.insert(0, str(salle.capacite))
            else:
                messagebox.showerror("Erreur", "Salle introuvable.")