import json
import mysql.connector
from models.salle import Salle


class DataSalle:
    def get_connection(self):
        try:
            with open("Data/config.json", "r", encoding="utf-8") as f:
                config = json.load(f)

            connection = mysql.connector.connect(
                host=config["host"],
                user=config["root"],
                password=config["admin"],
                database=config["db_salles"]
            )
            return connection
        except Exception as e:
            print("Erreur de connexion :", e)
            return None

    def insert_salle(self, salle):
        connection = self.get_connection()
        if connection is None:
            return False

        try:
            cursor = connection.cursor()
            sql = "INSERT INTO salle (code, libelle, type, capacite) VALUES (%s, %s, %s, %s)"
            values = (salle.code, salle.libelle, salle.type, salle.capacite)
            cursor.execute(sql, values)
            connection.commit()
            return True
        except Exception as e:
            print("Erreur insert_salle :", e)
            return False
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    def update_salle(self, salle):
        connection = self.get_connection()
        if connection is None:
            return False

        try:
            cursor = connection.cursor()
            sql = "UPDATE salle SET libelle=%s, type=%s, capacite=%s WHERE code=%s"
            values = (salle.libelle, salle.type, salle.capacite, salle.code)
            cursor.execute(sql, values)
            connection.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print("Erreur update_salle :", e)
            return False
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    def delete_salle(self, code):
        connection = self.get_connection()
        if connection is None:
            return False

        try:
            cursor = connection.cursor()
            sql = "DELETE FROM salle WHERE code=%s"
            cursor.execute(sql, (code,))
            connection.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print("Erreur delete_salle :", e)
            return False
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()


    def get_salle(self, code):
        connection = self.get_connection()
        if connection is None:
            return None

        try:
            cursor = connection.cursor()
            sql = "SELECT code, libelle, type, capacite FROM salle WHERE code=%s"
            cursor.execute(sql, (code,))
            row = cursor.fetchone()

            if row:
                return Salle(row[0], row[1], row[2], row[3])
            return None
        except Exception as e:
            print("Erreur get_salle :", e)
            return None
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    def get_salles(self):
        connection = self.get_connection()
        if connection is None:
            return []

        try:
            cursor = connection.cursor()
            sql = "SELECT code, libelle, type, capacite FROM salle"
            cursor.execute(sql)
            rows = cursor.fetchall()

            salles = []
            for row in rows:
                salles.append(Salle(row[0], row[1], row[2], row[3]))
            return salles
        except Exception as e:
            print("Erreur get_salles :", e)
            return []
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
