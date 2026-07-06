import sqlite3


class Database:

    def __init__(self):

        self.connection = sqlite3.connect(
            "employees.db"
        )

        self.connection.row_factory = sqlite3.Row

        self.cursor = self.connection.cursor()

    def execute(
        self,
        query,
        params=None
    ):

        if params is None:
            params = ()

        self.cursor.execute(
            query,
            params
        )

        rows = self.cursor.fetchall()

        return [

            dict(row)

            for row in rows

        ]

    def commit(self):

        self.connection.commit()

    def close(self):

        self.connection.close()