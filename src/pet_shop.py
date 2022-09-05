# WRITE YOUR FUNCTIONS HERE

def get_pet_shop_name(pet_shop):
    return pet_shop['name']

def get_total_cash(pet_shop):
    total_cash = pet_shop['admin']['total_cash']
    return total_cash

def add_or_remove_cash(pet_shop, cash):
    pet_shop['admin']['total_cash'] += cash

def get_pets_sold(pet_shop):
    pets_sold = pet_shop['admin']['pets_sold']
    return pets_sold

def increase_pets_sold(pet_shop, pets):
    pet_shop['admin']['pets_sold'] += pets

def get_stock_count(pet_shop):
    return len(pet_shop['pets'])

def get_pets_by_breed(pet_shop, breed):
    breed_total = []
    for pet in pet_shop['pets']:
        if pet['breed'] == breed:
            breed_total.append(pet)
    return breed_total

def find_pet_by_name(pet_shop, pet_name):
    for pet in pet_shop['pets']:
        if pet['name'] == pet_name:
            return pet

def remove_pet_by_name(pet_shop, pet_name):
    for pet in pet_shop['pets']:
        if pet['name'] == pet_name:
            pet_shop['pets'].remove(pet)

def add_pet_to_stock(pet_shop, new_pet):
    pet_shop['pets'].append(new_pet)

def get_customer_cash(customer):
    return customer['cash']

def remove_customer_cash(customer, cash_to_remove):
    customer['cash'] -= cash_to_remove

def get_customer_pet_count(customer):
    pets_list = []
    for pet in customer['pets']:
        pets_list.append(pet)
    return len(pets_list)

def add_pet_to_customer(customer, new_pet):
    customer['pets'].append(new_pet)

def customer_can_afford_pet(customer, new_pet):
    return customer['cash'] >= new_pet['price']
    
def sell_pet_to_customer(pet_shop, pet, customer):
    if pet == None:
        pass
    else:
        if customer_can_afford_pet(customer, pet) == False:
            pass
        else:
            remove_pet_by_name(pet_shop, pet['name'])
            add_pet_to_customer(customer, pet)
            increase_pets_sold(pet_shop, 1)        
            remove_customer_cash(customer, pet['price'])
            add_or_remove_cash(pet_shop, pet['price'])