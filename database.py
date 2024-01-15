"""Database module for the application."""
import sqlite3
from logging import getLogger


class Database:
    def __init__(self, db_file):
        """
        Create a connection to the database file.
        """
        try:
            self.conn = sqlite3.connect(db_file)
            self.cursor = self.conn.cursor()
            self.logger = getLogger(__name__)
            self.logger.info("Connected to database.")
        except Exception as e:
            self.logger.error(e)
            print(e)
        finally:
            self.conn.close()
            self.logger.info("Disconnected from database.")

    def create_table(self, table_name: str, columns: list) -> None:
        """
        Create a table in the database.
        """
        try:
            self.conn = sqlite3.connect("database.db")
            self.cursor = self.conn.cursor()
            self.cursor.execute(
                f"CREATE TABLE IF NOT EXISTS {table_name} ({columns[0]} {columns[1]}, {columns[2]} {columns[3]}, {columns[4]} {columns[5]})"
            )
            self.conn.commit()
            self.logger.info(f"Table {table_name} created.")
        except Exception as e:
            self.logger.error(e)
            print(e)
        finally:
            self.conn.close()
            self.logger.info("Disconnected from database.")

    def insert_data(self, table_name: str, data: dict) -> None:
        """
        Insert data into the database.
        """
        try:
            self.conn = sqlite3.connect("database.db")
            self.cursor = self.conn.cursor()
            keys_to_check = ["time", "temp", "humidity", "light"]
            for key in keys_to_check:
                if data.get(key) is None:
                    data[key] = None
            self.cursor.execute(
                f"INSERT INTO {table_name} (timestamp, temp, humidity, light) VALUES (?, ?, ?, ?)",
                (data["time"], data["temp"], data["humidity"], data["light"]),
            )
            self.conn.commit()
            self.logger.info("Data inserted.")
        except Exception as e:
            self.logger.error(e)
            print(e)
        finally:
            self.conn.close()
            self.logger.info("Disconnected from database.")
