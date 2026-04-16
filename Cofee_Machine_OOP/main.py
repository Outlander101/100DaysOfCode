from menu import Menu
from cofee_maker import CofeeMaker
from money_machine import MoneyMachine

def main():
    menu = Menu()
    cofee_maker = CofeeMaker()
    money_machine = MoneyMachine()
    print("Good Day.")
    is_on = True
    while is_on:
        choice = input(f"Select the type of Cofee {menu.get_item()}: ").lower()
        if choice == 'r' or choice == "report":
            cofee_maker.report()
            money_machine.report()
        elif choice == 'o' or choice == "off":
            print("Cofee Machine is turned off")
            is_on = False
        else: 
            drink = menu.find_drink(choice)
            if drink:
                if cofee_maker.is_resource_sufficient(drink):
                    if money_machine.make_payment(drink.cost):
                        cofee_maker.make_cofee(drink)
                        continue
                continue
        
if __name__ == "__main__":
    main()









