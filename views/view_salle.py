import customtkinter as ctk
from tkinter import messagebox
from tkinter import ttk
from models.salle import Salle
from services.service_salle import ServiceSalle


class ViewSalle(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Gestion des salles")
        self.geometry("800x550")

        self.service_salle = ServiceSalle()


        self.cadreInfo = ctk.CTkFrame(self, corner_radius=10)
        self.cadreInfo.pack(pady=10, padx=10, fill="x")

        self.label_code = ctk.CTkLabel(self.cadreInfo, text="Code salle")
        self.label_code.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.entry_code = ctk.CTkEntry(self.cadreInfo, width=200)
        self.entry_code.grid(row=0, column=1, padx=10, pady=10)

        self.label_libelle = ctk.CTkLabel(self.cadreInfo, text="Libellé")
        self.label_libelle.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.entry_libelle = ctk.CTkEntry(self.cadreInfo, width=200)
        self.entry_libelle.grid(row=1, column=1, padx=10, pady=10)

        self.label_type = ctk.CTkLabel(self.cadreInfo, text="Type")
        self.label_type.grid(row=2, column=0, padx=10, pady=10, sticky="w")
        self.entry_type = ctk.CTkEntry(self.cadreInfo, width=200)
        self.entry_type.grid(row=2, column=1, padx=10, pady=10)

        self.label_capacite = ctk.CTkLabel(self.cadreInfo, text="Capacité")
        self.label_capacite.grid(row=3, column=0, padx=10, pady=10, sticky="w")
        self.entry_capacite = ctk.CTkEntry(self.cadreInfo, width=200)
        self.entry_capacite.grid(row=3, column=1, padx=10, pady=10)

        # Cadre actions
        self.cadreAction = ctk.CTkFrame(self, corner_radius=10)
        self.cadreAction.pack(pady=10, padx=10, fill="x")

        self.btn_ajouter = ctk.CTkButton(
            self.cadreAction, text="Ajouter", command=self.ajouter_salle
        )
        self.btn_ajouter.grid(row=0, column=0, padx=10, pady=10)

        self.btn_modifier = ctk.CTkButton(
            self.cadreAction, text="Modifier", command=self.modifier_salle
        )
        self.btn_modifier.grid(row=0, column=1, padx=10, pady=10)

        self.btn_supprimer = ctk.CTkButton(
            self.cadreAction, text="Supprimer", command=self.supprimer_salle
        )
        self.btn_supprimer.grid(row=0, column=2, padx=10, pady=10)

        self.btn_rechercher = ctk.CTkButton(
            self.cadreAction, text="Rechercher", command=self.rechercher_salle
        )
        self.btn_rechercher.grid(row=0, column=3, padx=10, pady=10)

        # Cadre liste
        self.cadreList = ctk.CTkFrame(self, corner_radius=10)
        self.cadreList.pack(pady=10, padx=10, fill="both", expand=True)

        self.treeList = ttk.Treeview(
            self.cadreList,
            columns=("code", "libelle", "type", "capacite"),
            show="headings",
        )

        self.treeList.heading("code", text="CODE")
        self.treeList.heading("libelle", text="LIBELLÉ")
        self.treeList.heading("type", text="TYPE")
        self.treeList.heading("capacite", text="CAPACITÉ")

        self.treeList.column("code", width=100)
        self.treeList.column("libelle", width=220)
        self.treeList.column("type", width=150)
        self.treeList.column("capacite", width=120)

        self.treeList.pack(fill="both", expand=True, padx=10, pady=10)

        self.lister_salles()

    def vider_champs(self):
        self.entry_code.delete(0, "end")
        self.entry_libelle.delete(0, "end")
        self.entry_type.delete(0, "end")
        self.entry_capacite.delete(0, "end")

    def ajouter_salle(self):
        salle = Salle(
            self.entry_code.get().strip(),
            self.entry_libelle.get().strip(),
            self.entry_type.get().strip(),
            self.entry_capacite.get().strip(),
        )

        succes, message = self.service_salle.ajouter_salle(salle)
        if succes:
            messagebox.showinfo("Succès", message)
            self.vider_champs()
            self.lister_salles()
        else:
            messagebox.showerror("Erreur", message)

    def modifier_salle(self):
        salle = Salle(
            self.entry_code.get().strip(),
            self.entry_libelle.get().strip(),
            self.entry_type.get().strip(),
            self.entry_capacite.get().strip(),
        )

        succes, message = self.service_salle.modifier_salle(salle)
        if succes:
            messagebox.showinfo("Succès", message)
            self.vider_champs()
            self.lister_salles()
        else:
            messagebox.showerror("Erreur", message)

    def supprimer_salle(self):
        code = self.entry_code.get().strip()
        succes, message = self.service_salle.supprimer_salle(code)

        if succes:
            messagebox.showinfo("Succès", message)
            self.vider_champs()
            self.lister_salles()
        else:
            messagebox.showerror("Erreur", message)

    def rechercher_salle(self):
        code = self.entry_code.get().strip()
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

    def lister_salles(self):
        self.treeList.delete(*self.treeList.get_children())
        liste = self.service_salle.recuperer_salles()

        for s in liste:
            self.treeList.insert(
                "",
                "end",
                values=(s.code, s.libelle, s.type, s.capacite)
            )