from models.animals import Animal
from models.locations import Location
from models.customers import Customer
import sqlite3
import json

def get_all_animals():

    with sqlite3.connect("./kennels.db") as conn:

        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            a.id,
            a.name,
            a.breed,
            a.status,
            a.location_id,
            a.customer_id,
            l.name location_name,
            l.address location_address,
            c.name customer_name,
            c.address customer_address,
            c.email customer_email,
            c.password customer_password
        FROM Animal a
        JOIN Location l
            ON l.id = a.location_id
        JOIN Customer c
            ON c.id = a.customer_id
        """)

        animals = []

        dataset = db_cursor.fetchall()

        for row in dataset:

            animal = Animal(row['name'], row['breed'], row['status'],
                            row['location_id'], row['customer_id'], row['id'])

            location = Location(row['location_id'], row['location_name'], row['location_address'])

            customer = Customer(row['customer_id'], row['customer_name'], row['customer_address'], row['customer_email'], row['customer_password'])

            # Add the dictionary representation of the location to the animal
            animal.location = location.__dict__

            animal.customer = customer.__dict__

            # Add the dictionary representation of the animal to the list
            animals.append(animal.__dict__)
    return json.dumps(animals)


def get_single_animal(id):
    with sqlite3.connect("./kennels.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            a.id,
            a.name,
            a.breed,
            a.status,
            a.customer_id,
            a.location_id
        FROM animal a
        WHERE a.id = ?
        """, ( id, ))

        data = db_cursor.fetchone()

        animal = Animal(data['name'], data['breed'], data['status'],
                        data['location_id'], data['customer_id'],
                        data['id'])

        return json.dumps(animal.__dict__)

# def create_animal(animal):
#     last_animal = ANIMALS[-1]
#     new_id = last_animal.id + 1
#     animal["id"] = new_id
#     new_animal = Animal(animal['id'], animal['name'], animal['breed'], animal['status'], animal['location_id'], animal['customer_id'])
#     ANIMALS.append(new_animal)
#     return animal

def delete_animal(id):
    with sqlite3.connect("./kennels.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM animal
        WHERE id = ?
        """, (id, ))

def update_animal(id, new_animal):
    with sqlite3.connect("./kennels.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        UPDATE Animal
            SET
                name = ?,
                breed = ?,
                status = ?,
                location_id = ?,
                customer_id = ?
        WHERE id = ?
        """, (new_animal['name'], new_animal['breed'],
              new_animal['status'], new_animal['location_id'],
              new_animal['customer_id'], id, ))

        # Were any rows affected?
        # Did the client send an `id` that exists?
        rows_affected = db_cursor.rowcount

    if rows_affected == 0:
        # Forces 404 response by main module
        return False
    else:
        # Forces 204 response by main module
        return True
