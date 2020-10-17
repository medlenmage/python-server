from models.animals import Animal
import sqlite3
import json

ANIMALS = [
    Animal(1, "Snickers", "Dog", "Recreation", 1, 4),
    Animal(2, "Bard", "Cat", "napping", 2, 3)
    ]

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
            a.customer_id,
            a.location_id
        FROM animal a
        """)

        animals = []

        dataset = db_cursor.fetchall()

        for row in dataset:

            animal = Animal(row['id'], row['name'], row['breed'],
                            row['status'], row['location_id'],
                            row['customer_id'])

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

def create_animal(animal):
    last_animal = ANIMALS[-1]
    new_id = last_animal.id + 1
    animal["id"] = new_id
    new_animal = Animal(animal['id'], animal['name'], animal['species'], animal['status'], animal['location_id'], animal['customer_id'])
    ANIMALS.append(new_animal)
    return animal

def delete_animal(id):
    with sqlite3.connect("./kennels.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM animal
        WHERE id = ?
        """, (id, ))

def update_animal(id, updated_animal):

    for index, animal in enumerate(ANIMALS):
        if animal.id == id:
            ANIMALS[index] = Animal(updated_animal['id'], updated_animal['name'], updated_animal['species'], updated_animal['status'], updated_animal['location_id'], updated_animal['customer_id'])
            break
