from sql_validator import SQLValidator

validator = SQLValidator()

queries = [

    "SELECT * FROM employees",

    "DELETE FROM employees",

    "DROP TABLE employees",

    "UPDATE employees SET salary=0"

]

for query in queries:

    print(query)

    print(

        validator.validate(query)

    )

    print()