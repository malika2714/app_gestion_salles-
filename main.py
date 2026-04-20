from models.salle import Salle
from data.dao_salle import DataSalle
from services.service_salle import ServiceSalle

dao = DataSalle()

connection = dao.get_connection()
if connection:
    print("Connexion réussie")
    connection.close()
else:
    print("Echec connexion")

salle1 = Salle("S01", "Salle reseau", "Laboratoire", 20)
print("Ajout :", dao.insert_salle(salle1))

salle1.libelle = "Salle reseau modifiee"
salle1.capacite = 25
print("Modification :", dao.update_salle(salle1))

resultat = dao.get_salle("S01")
if resultat:
    print(resultat.afficher_infos())

for s in dao.get_salles():
    print(s.afficher_infos())

print("Suppression :", dao.delete_salle("S01"))

service = ServiceSalle()
salle1 = Salle("S101", "Salle Réseau", "Laboratoire", 20)
print(service.ajouter_salle(salle1))

salle1.libelle = "Salle Réseau Modifiée"
salle1.capacite = 25
print(service.modifier_salle(salle1))

print(service.supprimer_salle("S101"))

print(service.rechercher_salle("S101"))

liste = service.recuperer_salles()
for s in liste:
    print(s.afficher_infos())

