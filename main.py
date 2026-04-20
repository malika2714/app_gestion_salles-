from models.salle import Salle
from data.dao_salle import DataSalle

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