from database import Database


db = Database()

# -------------------------
# Departments Table
# -------------------------

db.execute("""
CREATE TABLE IF NOT EXISTS departments(

    id INTEGER PRIMARY KEY,

    department_name TEXT
)
""")

# -------------------------
# Employees Table
# -------------------------

db.execute("""
CREATE TABLE IF NOT EXISTS employees(

    id INTEGER PRIMARY KEY,

    name TEXT,

    department_id INTEGER,

    salary INTEGER,

    joining_year INTEGER,

    FOREIGN KEY(department_id)
    REFERENCES departments(id)
)
""")

# -------------------------
# Projects Table
# -------------------------

db.execute("""
CREATE TABLE IF NOT EXISTS projects(

    id INTEGER PRIMARY KEY,

    project_name TEXT,

    employee_id INTEGER,

    status TEXT,

    FOREIGN KEY(employee_id)
    REFERENCES employees(id)
)
""")

db.commit()

print("Database Created Successfully!")

db.close()