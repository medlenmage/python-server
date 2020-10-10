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
    
def get_single_employee(id):
    requested_employee = None
    for employee in EMPLOYEES:
        if employee["id"] == id:
            requested_employee = employee

    return requested_employee

def create_employee(employee):
    max_id = EMPLOYEES[-1]["id"]
    new_id = max_id + 1
    employee["id"] = new_id
    EMPLOYEES.append(employee)
    return employee
