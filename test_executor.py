from sql_executor import SQLExecutor

executor = SQLExecutor()

result = executor.execute("""

SELECT name, salary

FROM employees

ORDER BY salary DESC

LIMIT 5

""")

print(result)

executor.close()