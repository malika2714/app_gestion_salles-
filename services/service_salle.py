from data.dao_salle import DataSalle

class ServiceSalle:
    def __init__(self):
        self.dao_salle = DataSalle()

def ajouter_salle(self, salle):
    return self.dao_salle.insert_salle(salle)

def ajouter_salle(self, salle):
    if not salle.code or not salle.libelle or not salle.type or salle.capacite is None:
        return False, "Tous les champs sont obligatoires."

    return self.dao_salle.insert_salle(salle), "Traitement terminé."

def ajouter_salle(self, salle):
    if not salle.code or not salle.libelle or not salle.type or salle.capacite is None:
        return False, "Tous les champs sont obligatoires."

    try:
        capacite = int(salle.capacite)
        if capacite < 1:
            return False, "La capacité doit être supérieure ou égale à 1."
    except ValueError:
        return False, "La capacité doit être un entier valide."

    salle.capacite = capacite
    succes = self.dao_salle.insert_salle(salle)

    if succes:
        return True, "Salle ajoutée avec succès."
    return False, "Erreur lors de l'ajout de la salle."