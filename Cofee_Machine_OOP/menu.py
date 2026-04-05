class MenuItem:
    def __init__(self, name, water, milk, cofee, cost):
        """Models each Menu Item."""
        self.name = name
        self.cost = cost
        self.ingredients = {
            "water": water,
            "milk": milk,
            "cofee": cofee
        }

class Menu:
    def __init__(self):
        """Models the Menu with drinks."""
        self.menu = [
            MenuItem(name="cappucino", water=250, milk=50, cofee=24, cost=3.0),
            MenuItem(name="latte", water=50, milk=0, cofee=18, cost=1.5),
            MenuItem(name="espresso", water=200, milk=150, cofee=24, cost=2.5)
        ]

    def get_item(self):
        """Returns all the names of the available menu items"""
        options = ""
        for item in self.menu:
            options += f"{item.name}/"
        return options
    
    def find_drink(self, order_name):
        """Searches the menu for a particular drink by name. Returns that item if it exists, otherwise returns None"""
        for item in self.menu:
            if item.name == order_name:
                return item
        print("Sorry, item is unavailble.")

