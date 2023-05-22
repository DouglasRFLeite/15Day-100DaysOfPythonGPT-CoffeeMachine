from src.menu import MENU
from copy import deepcopy


class CoffeeMachine:
    def __init__(self) -> None:
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }
        self.money = 0

    def get_payment(self, price):
        print("Insert coins:")
        quarters = int(input("\thow many quartes: "))
        dimes = int(input("\thow many dimes: "))
        nickles = int(input("\thow many nickles: "))
        pennies = int(input("\thow many pennies: "))

        payment = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
        change = payment - price
        if change < 0:
            print("Insuficient payment!")
            return True  # to stop
        else:
            self.money += price
            print(f"Here is ${change:.2f} in change.")
            return False  # to stop

    def print_report(self):
        print(f"Water: {self.resources['water']}ml")
        print(f"Milk: {self.resources['milk']}ml")
        print(f"Coffee: {self.resources['coffee']}g")
        print(f"Money: ${self.money}")

    def check_and_reduce_resources(self, ingredients):
        new_resourses = deepcopy(self.resources)
        for ingredient in ingredients:
            if new_resourses[ingredient] > ingredients[ingredient]:
                new_resourses[ingredient] -= ingredients[ingredient]
            else:
                print(f"Sorry, there is not enough {ingredient}.")
                return False
        return new_resourses

    def make_coffe(self, coffe):
        if not (coffe in MENU):
            print("We don't have that coffe here.")
            return

        if self.get_payment(MENU[coffe]["cost"]):
            return

        new_resources = self.check_and_reduce_resources(
            MENU[coffe]["ingredients"])
        if new_resources:
            self.resources = deepcopy(new_resources)
            print(f"Here is your {coffe}. Enjoy!")
