from Db import Db

class RequestDb:
    def __init__(self):
        self.__db = Db(host="localhost", user="root", password="rootequipe7+", database="budget_buddy")

    def create(self, table, data):
            columns = ', '.join(data.keys())
            placeholders = ', '.join(['%s'] * len(data))
            query = f"INSERT INTO {table} ({columns}) VALUES ({placeholders})"
            self.__db.executeQuery(query, tuple(data.values()))

    def read(self, table, conditions=None):
            query = f"SELECT * FROM {table}"
            if conditions:
                query += f" WHERE {conditions}"
            return self.__db.fetch(query)

    def update(self, table, data, conditions=None):
        set_clause = ', '.join([f"{key} = %s" for key in data.keys()])
        query = f"UPDATE {table} SET {set_clause}"
        if conditions:
            query += f" WHERE {conditions}"
        self.__db.executeQuery(query, tuple(data.values()))

    def delete(self, table, conditions):
        query = f"DELETE FROM {table} WHERE {conditions}"
        self.__db.executeQuery(query)