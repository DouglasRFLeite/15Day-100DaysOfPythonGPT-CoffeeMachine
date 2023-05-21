from src.menu import MENU


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
        for ingredient in self.resources:
            print(f"{ingredient.capitalize()}: {self.resources[ingredient]}")

    def make_espresso(self):
        if self.get_payment(MENU["espresso"]["cost"]):
            return
