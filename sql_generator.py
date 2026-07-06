import ollama


class SQLGenerator:

    def generate_sql(
        self,
        question,
        schema
    ):

        prompt = f"""
You are an expert SQLite SQL developer.

Database Schema:

{schema}

Convert the user's question into a valid SQLite SQL query.

Rules:

1. Return ONLY SQL.
2. Do NOT explain anything.
3. Do NOT use markdown.
4. Do NOT wrap SQL inside ``` blocks.
5. Generate only SELECT statements.
6. Never generate INSERT, UPDATE, DELETE, DROP or ALTER.
7. Use LOWER(column_name) = LOWER('value') for text equality.
8. Prefer LIKE with LOWER() for flexible text matching when appropriate.

User Question:

{question}
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

        sql = response["message"]["content"].strip()

        return sql