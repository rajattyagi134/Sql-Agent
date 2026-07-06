from database import Database
import random

db = Database()

# ----------------------------
# Departments
# ----------------------------

departments = [

    (1, "Engineering"),
    (2, "AI Research"),
    (3, "Finance"),
    (4, "Human Resources"),
    (5, "Sales")

]

db.execute("DELETE FROM projects")
db.execute("DELETE FROM employees")
db.execute("DELETE FROM departments")

for department in departments:

    db.execute(

        """
        INSERT INTO departments
        VALUES (?, ?)
        """,

        department

    )

# ----------------------------
# Employees
# ----------------------------

names = [

    "John","Sarah","Mike","Emma","David",
    "Sophia","Daniel","Olivia","James","Ava",
    "William","Mia","Benjamin","Charlotte",
    "Lucas","Amelia","Henry","Harper",
    "Alexander","Evelyn","Rajat","Noah",
    "Liam","Isabella","Ethan","Grace",
    "Jack","Ella","Aria","Leo",
    "Mason","Chloe","Logan","Emily",
    "Jacob","Aiden","Lily","Zoe",
    "Matthew","Sofia"

]

employee_id = 1

for name in names:

    db.execute(

        """
        INSERT INTO employees
        VALUES (?, ?, ?, ?, ?)
        """,

        (

            employee_id,

            name,

            random.randint(1,5),

            random.randint(60000,180000),

            random.randint(2018,2026)

        )

    )

    employee_id += 1

# ----------------------------
# Projects
# ----------------------------

project_names = [

    "Payment AI",
    "Fraud Detection",
    "AML Monitoring",
    "Customer Analytics",
    "Recommendation Engine",
    "Smart Parking",
    "Risk Prediction",
    "Invoice Automation",
    "Voice Assistant",
    "Credit Scoring"

]

project_id = 1

for employee in range(1,41):

    for _ in range(2):

        db.execute(

            """
            INSERT INTO projects
            VALUES (?, ?, ?, ?)
            """,

            (

                project_id,

                random.choice(project_names),

                employee,

                random.choice(

                    [

                        "Active",
                        "Completed"

                    ]

                )

            )

        )

        project_id += 1

db.commit()

print("Database Populated Successfully!")

db.close()