"""Database module for the application."""

import sqlite3
from logging import getLogger


class Database:
    def __init__(self, db_file):
        """
        Create a connection to the database file.
        """
        try:
            self.db_file = db_file
            self.conn = sqlite3.connect(self.db_file)
            self.cursor = self.conn.cursor()
            self.logger = getLogger(__name__)
            self.logger.info("Connected to database.")
        except Exception as e:
            self.logger.error(e)
            print(e)

    def create_table(self, table_name: str, columns: list) -> None:
        """
        Create a table in the database.
        """
        try:
            column_definitions = ", ".join(f"{column} TEXT" for column in columns)
            self.cursor.execute(
                f"CREATE TABLE IF NOT EXISTS `{table_name}` ({column_definitions})"
            )
            self.conn.commit()
            self.logger.info(f"Table {table_name} created.")
        except Exception as e:
            self.logger.error(e)
            print(e)

    def insert_data(self, table_name: str, data: dict) -> None:
        """
        Insert data into the database.
        """
        try:
            keys_to_check = ["time", "temp", "humidity", "light"]
            for key in keys_to_check:
                if data.get(key) is None:
                    data[key] = None
            self.cursor.execute(
                f"INSERT INTO `{table_name}` (time, temp, humidity, light) VALUES (?, ?, ?, ?)",
                (data["time"], data["temp"], data["humidity"], data["light"]),
            )
            self.conn.commit()
            self.logger.info("Data inserted.")
        except Exception as e:
            self.logger.error(e)
            print(e)
