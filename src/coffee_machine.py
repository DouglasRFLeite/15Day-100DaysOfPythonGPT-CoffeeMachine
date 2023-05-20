from menu import MENU


class CoffeeMachine:
    def __init__(self) -> None:
        resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }
        money = 0

    def get_payment(self, price):
        print("Insert coins:")
        quarters = int(input("\thow many quartes: "))
        dimes = int(input("\thow many dimes: "))
        nickles = int(input("\thow many nickles: "))
        pennies = int(input("\thow many pennies: "))

        payment = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
        change = payment - price
        if change < payment:
            print("Insuficient payment!")
            return True  # to stop
        else:
            self.money += price
            print(f"Here is ${change:.2f} in change.")
            return False  # to stop

    def make_espresso(self):
        if self.get_payment(MENU["espresso"]["cost"]):
            return
