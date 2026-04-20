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