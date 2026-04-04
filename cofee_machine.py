cofee_types = {
    "Espresso": {"water": 50, "cofee": 18, "milk": 0, "price": 1.5},
    "Latte": {"water": 200, "cofee": 24, "milk": 150, "price": 2.5},
    "Cappuccino": {"water": 250, "cofee": 24, "milk": 100, "price": 3.0}
}

materials_in_machine = {"water": 300, "milk": 200, "cofee": 100, "cash":0}

def resource_validation(cofee_type):
    for item in cofee_types[cofee_type]:
        if item != 'price':
            if materials_in_machine[item] < cofee_types[cofee_type][item]:
                print(f"Sorry, not enough {item}")
                return False
    return True

def process_coin():
    total = int(input("Enter the number of quarters: ")) * 0.25
    total += int(input("Enter the number of dimes: ")) * 0.1
    total += int(input("Enter the number of nickels: ")) * 0.05
    total += int(input("Enter the number of pennies: ")) * 0.01
    print(f"You paid ${total}")
    return total

def prepare_cofee(cofee_type):
    if resource_validation(cofee_type):
        print(f"Cost for {cofee_type} is ${cofee_types[cofee_type]['price']}")
        recieved_money = process_coin()
        if recieved_money < cofee_types[cofee_type]['price']:
            print(f"Insufficient Money for '{cofee_type}'. Need ${cofee_types[cofee_type]['price'] - recieved_money}")
        else:
            change = recieved_money - cofee_types[cofee_type]["price"]
            print(f"Here is your '{cofee_type}' and here is your change of ${round(change, 2)}.")
            update_resources(cofee_type)
    else:
        print("Sorry, that's not enough money. Money refunded.")

def update_resources(cofee_type):
    recipe = cofee_types[cofee_type]
    for item in recipe:
        if item != 'price':
            materials_in_machine[item] -= recipe[item]
    materials_in_machine["cash"] += recipe["price"]

def report():
    print("Cofee machine has below levels of raw ingredients")
    for item in materials_in_machine:
        print(f"{item}: {materials_in_machine[item]}")
    
def main():
    print("Good day")
    is_on = True
    while is_on:
        choice = input("What would you like to have Cappuccino('c'), Latte('l'), Espresso('e'): ").lower()
        match choice:
            case 'c':
                prepare_cofee('Cappuccino')
                continue
            case 'l':
                prepare_cofee('Latte')
                continue
            case 'e':
                prepare_cofee('Espresso')
                continue
            case  'r':
                report()
                continue
            case 'o':
                print("Cofee Machine is off")
                is_on = False
                break
            case 'f':
                for item in materials_in_machine:
                    if item != "cash":
                        materials_in_machine[item] = 500 # Set back to max levels
                        print("Machine refilled!")
            case _:
                print("Invalid Choice")
                continue
        

if __name__ == "__main__":
    main()
