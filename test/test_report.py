import pytest
from src.coffee_machine import CoffeeMachine


@pytest.fixture
def payment_test():
    return CoffeeMachine()


def test_full_machine_report(payment_test, capsys):
    payment_test.print_report()

    captured = capsys.readouterr()
    output = captured.out.strip()

    assert output == """Water: 300ml\nMilk: 200ml\nCoffee: 100g\nMoney: $0"""


def test_empty_machine_report(payment_test, capsys):
    payment_test.resources = {
        "water": 0,
        "milk": 0,
        "coffee": 0,
    }
    payment_test.print_report()

    captured = capsys.readouterr()
    output = captured.out.strip()

    assert output == """Water: 0ml\nMilk: 0ml\nCoffee: 0g\nMoney: $0"""
