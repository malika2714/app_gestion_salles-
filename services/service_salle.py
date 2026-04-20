from data.dao_salle import DataSalle

class ServiceSalle:
    def __init__(self):
        self.dao_salle = DataSalle()

def ajouter_salle(self, salle):
    return self.dao_salle.insert_salle(salle)