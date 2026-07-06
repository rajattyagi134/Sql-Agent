class SQLValidator:

    ALLOWED = [
        "SELECT"
    ]

    BLOCKED = [

        "INSERT",
        "UPDATE",
        "DELETE",
        "DROP",
        "ALTER",
        "CREATE",
        "TRUNCATE",
        "REPLACE",
        "ATTACH",
        "DETACH",
        "PRAGMA"

    ]

    def validate(
        self,
        sql
    ):

        query = sql.upper().strip()

        if not query.startswith("SELECT"):

            return False

        for keyword in self.BLOCKED:

            if keyword in query:

                return False

        return True