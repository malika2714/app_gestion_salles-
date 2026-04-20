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

def modifier_salle(self, salle):
    if not salle.code or not salle.libelle or not salle.type or salle.capacite is None:
        return False, "Tous les champs sont obligatoires."

    try:
        capacite = int(salle.capacite)
        if capacite < 1:
            return False, "La capacité doit être supérieure ou égale à 1."
    except ValueError:
        return False, "La capacité doit être un entier valide."

    salle.capacite = capacite
    succes = self.dao_salle.update_salle(salle)

    if succes:
        return True, "Salle modifiée avec succès."
    return False, "Erreur lors de la modification de la salle."


def supprimer_salle(self, code):
    if not code:
        return False, "Le code est obligatoire."

    succes = self.dao_salle.delete_salle(code)
    if succes:
        return True, "Salle supprimée avec succès."
    return False, "Salle introuvable ou erreur de suppression."

def rechercher_salle(self, code):
    if not code:
        return None
    return self.dao_salle.get_salle(code)

def recuperer_salles(self):
    return self.dao_salle.get_salles()