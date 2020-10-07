LOCATIONS = [
    {
        "id": 1,
        "city": "Los Angles",
        "state": "California",
    },
    {
        "id": 2,
        "city": "Atlanta",
        "state": "Georgia",
    },
    {
        "id": 3,
        "city": "Nashville",
        "state": "Tennessee",
    }
]

def get_all_locations():
    return LOCATIONS

# Function with a single parameter
def get_single_location(id):
    # Variable to hold the found animal, if it exists
    requested_location = None

    # Iterate the ANIMALS list above. Very similar to the
    # for..of loops you used in JavaScript.
    for location in LOCATIONS:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if location["id"] == id:
            requested_location = location

    return requested_location
