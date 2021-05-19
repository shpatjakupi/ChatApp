from unittest import TestCase
import unittest
import sqlite3
import unittest
from sqlite3 import Error
from datetime import datetime
import time

# CONSTANTS

FILE = "messages_test.db"
PLAYLIST_TABLE = "Messages_test"

class TestDatabase(unittest.TestCase):
    
    def test__create_table(self):
        """
        create new database table if one doesn't exist
        :return: None
        """
        conn = None
        conn = sqlite3.connect(FILE)

        cursor = conn.cursor()
        query = f"""CREATE TABLE IF NOT EXISTS {PLAYLIST_TABLE}
                    (name TEXT, content TEXT, id INTEGER PRIMARY KEY AUTOINCREMENT)"""
        cursor.execute(query)
        conn.commit()

    def get_all_messages(self, limit=100, name=None):
        """
        returns all messages
        :param limit: int
        :return: list[dict]
        """
        conn = None
        conn = sqlite3.connect(FILE)

        cursor = conn.cursor()
        if not name:
            query = f"SELECT * FROM {PLAYLIST_TABLE}"
            cursor.execute(query)
        else:
            query = f"SELECT * FROM {PLAYLIST_TABLE} WHERE NAME = ?"
            cursor.execute(query, (name,))

        result = cursor.fetchall()

        # return messages in sorted order by date
        results = []
        for r in sorted(result, key=lambda x: x[2], reverse=True)[:limit]:
            name, content, _id = r
            data = {"name":name, "message":content}
            results.append(data)

        return list(reversed(results))
    
    def get_messages_by_name(self, name, limit=100):
        """
        Gets a list of messages by user name
        :param name: str
        :return: list
        """
        return self.get_all_messages(limit, name)
    

    def test_save_message(self, limit=1):
            """
            saves the given message in the table
            :param name: str
            :param msg: str
            :param time: datetime
            :return: None
            """

            conn = None
            conn = sqlite3.connect(FILE)

            cursor = conn.cursor()

            query = f"INSERT INTO {PLAYLIST_TABLE} VALUES (?, ?, ?)"
            cursor.execute(query, ("John", "Hello World!", None))
            conn.commit()
            self.assertEqual([{"name": "John", "message": "Hello World!"}],  self.get_messages_by_name(name="John", limit=limit))

if __name__ == '__main__':
    unittest.main()

