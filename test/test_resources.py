from src.coffee_machine import CoffeeMachine
from src.menu import MENU


def test_not_enough_resources():
    coffe_machine = CoffeeMachine()
    coffe_machine.resources = {
        "water": 0,
        "milk": 0,
        "coffee": 0,
    }
    ingredients = MENU["latte"]["ingredients"]

    assert not coffe_machine.check_and_reduce_resources(ingredients)


def test_enough_resources():
    coffe_machine = CoffeeMachine()
    ingredients = MENU["latte"]["ingredients"]

    assert coffe_machine.check_and_reduce_resources(ingredients)
