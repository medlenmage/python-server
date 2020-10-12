from models.animals import Animal

ANIMALS = [
    Animal(1, "Snickers", "Dog", "Recreation", 1, 4),
    Animal(2, "Bard", "Cat", "napping", 2, 3)
    ]

def get_all_animals():
    return ANIMALS

# Function with a single parameter
def get_single_animal(id):
    requested_animal = None
    for animal in ANIMALS:
        if animal.id == id:
            requested_animal = animal

    return requested_animal

def create_animal(animal):
    last_animal = ANIMALS[-1]
    new_id = last_animal.id + 1
    animal["id"] = new_id
    new_animal = Animal(animal['id'], animal['name'], animal['species'], animal['status'], animal['location_id'], animal['customer_id'])
    ANIMALS.append(new_animal)
    return animal

def delete_animal(id):
    animal_index = -1
    for index, animal in enumerate(ANIMALS):
        if animal.id == id:
            # Found the animal. Store the current index.
            animal_index = index

    # If the animal was found, use pop(int) to remove it from list
    if animal_index >= 0:
        ANIMALS.pop(animal_index)

def update_animal(id, updated_animal):
    # Iterate the ANIMALS list, but use enumerate() so that
    # you can access the index value of each item.
    for index, animal in enumerate(ANIMALS):
        if animal.id == id:
            # Found the animal. Update the value.
            ANIMALS[index] = Animal(updated_animal['id'], updated_animal['name'], updated_animal['species'], updated_animal['status'], updated_animal['location_id'], updated_animal['customer_id'])
            break
