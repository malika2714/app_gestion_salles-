import json
import mysql.connector
from models.salle import Salle


class DataSalle:
    def get_connection(self):
        try:
            with open("data/config.json", "r", encoding="utf-8") as f:
                config = json.load(f)

            connection = mysql.connector.connect(
                host=config["host"],
                user=config["user"],
                password=config["password"],
                database=config["database"]
            )
            return connection

        except Exception as e:
            print("Erreur de connexion à la base de données :", e)
            return None

    def insert_salle(self, salle):
        connection = self.get_connection()
        if connection is None:
            return False

        cursor = None
        try:
            cursor = connection.cursor()
            sql = "INSERT INTO salle (code, libelle, type, capacite) VALUES (%s, %s, %s, %s)"
            valeurs = (salle.code, salle.libelle, salle.type, salle.capacite)
            cursor.execute(sql, valeurs)
            connection.commit()
            return True

        except Exception as e:
            print("Erreur lors de l'ajout de la salle :", e)
            return False

        finally:
            if cursor is not None:
                cursor.close()
            if connection is not None and connection.is_connected():
                connection.close()

    def update_salle(self, salle):
        connection = self.get_connection()
        if connection is None:
            return False

        cursor = None
        try:
            cursor = connection.cursor()
            sql = "UPDATE salle SET libelle = %s, type = %s, capacite = %s WHERE code = %s"
            valeurs = (salle.libelle, salle.type, salle.capacite, salle.code)
            cursor.execute(sql, valeurs)
            connection.commit()

            if cursor.rowcount > 0:
                return True
            return False

        except Exception as e:
            print("Erreur lors de la modification de la salle :", e)
            return False

        finally:
            if cursor is not None:
                cursor.close()
            if connection is not None and connection.is_connected():
                connection.close()

    def delete_salle(self, code):
        connection = self.get_connection()
        if connection is None:
            return False

        cursor = None
        try:
            cursor = connection.cursor()
            sql = "DELETE FROM salle WHERE code = %s"
            cursor.execute(sql, (code,))
            connection.commit()

            if cursor.rowcount > 0:
                return True
            return False

        except Exception as e:
            print("Erreur lors de la suppression de la salle :", e)
            return False

        finally:
            if cursor is not None:
                cursor.close()
            if connection is not None and connection.is_connected():
                connection.close()

    def get_salle(self, code):
        connection = self.get_connection()
        if connection is None:
            return None

        cursor = None
        try:
            cursor = connection.cursor()
            sql = "SELECT code, libelle, type, capacite FROM salle WHERE code = %s"
            cursor.execute(sql, (code,))
            resultat = cursor.fetchone()

            if resultat:
                return Salle(resultat[0], resultat[1], resultat[2], resultat[3])
            return None

        except Exception as e:
            print("Erreur lors de la recherche de la salle :", e)
            return None

        finally:
            if cursor is not None:
                cursor.close()
            if connection is not None and connection.is_connected():
                connection.close()

    def get_salles(self):
        connection = self.get_connection()
        if connection is None:
            return []

        cursor = None
        try:
            cursor = connection.cursor()
            sql = "SELECT code, libelle, type, capacite FROM salle"
            cursor.execute(sql)
            resultats = cursor.fetchall()

            liste_salles = []
            for row in resultats:
                salle = Salle(row[0], row[1], row[2], row[3])
                liste_salles.append(salle)

            return liste_salles

        except Exception as e:
            print("Erreur lors de la récupération des salles :", e)
            return []

        finally:
            if cursor is not None:
                cursor.close()
            if connection is not None and connection.is_connected():
                connection.close()