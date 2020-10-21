from models.employees import Employee
from models.locations import Location
import sqlite3
import json

EMPLOYEES = [
    Employee(1, "Captain Spaulding", "123 seasme street", 1)
]

def get_all_employees():
    # Open a connection to the database
    with sqlite3.connect("./kennels.db") as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            a.id,
            a.name,
            a.address,
            a.location_id,
            l.name location_name,
            l.address location_address
        FROM employee a
        JOIN Location l
            ON l.id = a.location_id
        """)

        employees = []

        dataset = db_cursor.fetchall()

        for row in dataset:

            employee = Employee(row['id'], row['name'], row['address'],
             row['location_id'])

            location = Location(row['location_id'], row['location_name'], row['location_address'])

            employee.location = location.__dict__

            employees.append(employee.__dict__)


    return json.dumps(employees)

def get_single_employee(id):
    with sqlite3.connect("./kennels.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            a.id,
            a.name,
            a.address,
            a.location_id
        FROM employee a
        WHERE a.id = ?
        """, ( id, ))

        data = db_cursor.fetchone()

        employee = Employee(data['id'], data['name'], data['address'],
                        data['location_id'])

        return json.dumps(employee.__dict__)

def create_employee(employee):
    last_employee = EMPLOYEES[-1]
    new_id = last_employee.id + 1
    employee["id"] = new_id
    new_employee = Employee(employee["id"], employee["name"], employee["address"],employee["locationId"])
    EMPLOYEES.append(new_employee)
    return employee

def delete_employee(id):
    with sqlite3.connect("./kennels.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM employee
        WHERE id = ?
        """, (id, ))


def update_employee(id, new_employee):
    for index, employee in enumerate(EMPLOYEES):
        if employee["id"] == id:
            EMPLOYEES[index] = new_employee
            break
