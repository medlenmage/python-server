from models.employees import Employee

# EMPLOYEES = [
#     {
#         "id": 1,
#         "name": "Captain Spaulding",
#         "locationId": 1,
#         "manager": True,
#         "full-time": True,
#         "hourly-rate": 30
#     },
#     {
#         "id": 2,
#         "name": "John Wick",
#         "locationId": 2,
#         "manager": True,
#         "fullTime": True,
#         "hourlyRate": 30
#     },
#     {
#         "id": 3,
#         "name": "Tiny",
#         "locationId": 1,
#         "manager": False,
#         "full-time": True,
#         "hourly-rate": 15
#     }
# ]

EMPLOYEES = [
    Employee(1, "Captain Spaulding", 1, True, True, 30)
]

def get_all_employees():
    return EMPLOYEES

def get_single_employee(id):
    requested_employee = None
    for employee in EMPLOYEES:
        if employee.id == id:
            requested_employee = employee

    return requested_employee

def create_employee(employee):
    last_employee = EMPLOYEES[-1]
    new_id = last_employee.id + 1
    employee["id"] = new_id
    new_employee = Employee(employee["id"], employee["name"], employee["locationId"], employee["manager"], employee["fullTime"], employee["hourlyRate"])
    EMPLOYEES.append(new_employee)
    return employee

def delete_employee(id):
    employee_index = -1
    for index, employee in enumerate(EMPLOYEES):
        if employee.id == id:
            employee_index = index
    if employee_index >= 0:
        EMPLOYEES.pop(employee_index)

def update_employee(id, new_employee):
    for index, employee in enumerate(EMPLOYEES):
        if employee["id"] == id:
            EMPLOYEES[index] = new_employee
            break
