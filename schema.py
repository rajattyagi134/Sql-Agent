from database import Database


class SchemaManager:

    def __init__(self):

        self.db = Database()

    def get_schema(self):

        schema = ""

        tables = self.db.execute("""

            SELECT name

            FROM sqlite_master

            WHERE type='table'

            ORDER BY name

        """)

        for table in tables:

            table_name = table["name"]

            schema += f"\nTable: {table_name}\n"

            columns = self.db.execute(
                f"PRAGMA table_info({table_name})"
            )

            for column in columns:

                schema += (
                    f"- {column['name']} "
                    f"({column['type']})\n"
                )

        return schema

    def close(self):

        self.db.close()