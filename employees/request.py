EMPLOYEES = [
    {
        "id": 1,
        "name": "Captain Spaulding",
        "locationId": 1,
        "manager": True,
        "full-time": True,
        "hourly-rate": 30.50
    },
    {
        "id": 2,
        "name": "John Wick",
        "locationId": 2,
        "manager": True,
        "full-time": True,
        "hourly-rate": 30.50
    },
    {
        "id": 3,
        "name": "Tiny",
        "locationId": 1,
        "manager": False,
        "full-time": True,
        "hourly-rate": 15
    }
]

def get_all_employees():
    return EMPLOYEES

# Function with a single parameter
def get_single_employee(id):
    # Variable to hold the found animal, if it exists
    requested_employee = None

    # Iterate the ANIMALS list above. Very similar to the
    # for..of loops you used in JavaScript.
    for employee in EMPLOYEES:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if employee["id"] == id:
            requested_employee = employee

    return requested_employee
