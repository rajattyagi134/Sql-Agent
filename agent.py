from schema import SchemaManager
from sql_generator import SQLGenerator
from sql_validator import SQLValidator
from sql_executor import SQLExecutor

import ollama


class SQLAgent:

    def __init__(self):

        self.schema = SchemaManager()

        self.generator = SQLGenerator()

        self.validator = SQLValidator()

        self.executor = SQLExecutor()

    def answer_question(
        self,
        question
    ):

        # Step 1
        schema = self.schema.get_schema()

        # Step 2
        sql = self.generator.generate_sql(

            question,

            schema

        )

        print("\nGenerated SQL:\n")

        print(sql)

        # Step 3
        if not self.validator.validate(sql):

            return {

                "success": False,

                "error": "Unsafe SQL generated."

            }

        # Step 4
        result = self.executor.execute(sql)

        if not result["success"]:

            return result

        # Step 5
        prompt = f"""
You are an AI SQL Assistant.

Convert the SQL query result into a
clear and professional natural language answer.

Question:

{question}

SQL:

{sql}

Result:

{result['results']}
"""

        response = ollama.chat(

            model="llama3",

            messages=[

                {

                    "role": "user",

                    "content": prompt

                }

            ]

        )

        return {

            "success": True,

            "sql": sql,

            "results": result["results"],

            "answer": response["message"]["content"]

        }

    def close(self):

        self.schema.close()

        self.executor.close()