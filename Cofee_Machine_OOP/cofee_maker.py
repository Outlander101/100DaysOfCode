class CofeeMaker:
    def __init__(self):
        """Models the machine that makes the coffee"""
        self.resources = {
            "water": 300,
            "milk": 200,
            "cofee": 100,
        }
    
    def report(self):
        """Prints a report of all resources."""
        for item in self.resources:
            if item == "cofee":
                print(f"Cofee: {self.resources['cofee']}g")
            else:
                print(f"{item}: {self.resources[item]}ml")
    
    def is_resource_sufficient(self, drink):
        """Returns True when order can be made, False if ingredients are insufficient."""
        can_make = True
        for item in drink.ingredients:
            if drink.ingredients[item] > self.resources[item]:
                print(f"Sorry, there is not enough {item}")
                can_make = False
        return can_make
    
    def make_cofee(self, drink):
        """Deducts the required ingredients from the resources."""
        for item in self.resources:
            if item != 'cash':
                self.resources[item] -= drink.ingredients[item]
        print(f"Here is your {drink.name}. Enjoy")
