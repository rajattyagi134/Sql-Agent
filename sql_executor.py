from database import Database


class SQLExecutor:

    def __init__(self):

        self.db = Database()

    def execute(
        self,
        sql
    ):

        try:

            results = self.db.execute(
                sql
            )

            return {

                "success": True,

                "results": results

            }

        except Exception as e:

            return {

                "success": False,

                "error": str(e)

            }

    def close(self):

        self.db.close()