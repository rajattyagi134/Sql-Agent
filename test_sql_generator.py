from schema import SchemaManager
from sql_generator import SQLGenerator

schema = SchemaManager()

generator = SQLGenerator()

question = "Who earns the highest salary?"

sql = generator.generate_sql(

    question,

    schema.get_schema()

)

print(sql)

schema.close()