from src.coffee_machine import CoffeeMachine
from src.menu import MENU
import pytest


def test_not_enough_resources(capsys):
    coffe_machine = CoffeeMachine()
    coffe_machine.resources = {
        "water": 0,
        "milk": 0,
        "coffee": 0,
    }

    coffe_machine.make_coffe("latte")

    captured = capsys.readouterr()
    output = captured.out.strip()

    assert output == "Sorry, there is not enough water."


def test_make_espresso():
    coffe_machine = CoffeeMachine()
