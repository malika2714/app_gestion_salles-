class Salle:
    def __init__(self, code, libelle, typee, capacite):
        self.code = code
        self.libelle = libelle
        self.type = typee
        self.capacite = capacite

    def afficher_infos(self):
        return f"Code: {self.code}, Libellé: {self.libelle}, Type: {self.typee}, Capacité: {self.capacite}"
