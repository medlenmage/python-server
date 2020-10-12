from models.customers import Customer

CUSTOMERS = [
    Customer(1, "Luke", True)
]

def get_all_customers():
    return CUSTOMERS

def get_single_customer(id):
    requested_customer = None
    for customer in CUSTOMERS:
        if customer.id == id:
            requested_customer = customer

    return requested_customer

def create_customer(customer):
    last_customer = CUSTOMERS[-1]
    new_id = last_customer.id + 1
    customer["id"] = new_id
    new_customer = Customer(customer["id"], customer["name"], customer['isBroke'])
    CUSTOMERS.append(new_customer)
    return customer

def delete_customer(id):
    customer_index = -1
    for index, customer in enumerate(CUSTOMERS):
        if customer["id"] == id:
            customer_index = index
    if customer_index >= 0:
        CUSTOMERS.pop(customer_index)

def update_customer(id, new_customer):
    for index, customer in enumerate(CUSTOMERS):
        if customer["id"] == id:
            CUSTOMERS[index] = new_customer
            break
