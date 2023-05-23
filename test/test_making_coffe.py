from src.coffee_machine import CoffeeMachine
from src.menu import MENU
from io import StringIO
from unittest.mock import patch
import pytest


@patch("builtins.input", side_effect=[6, 2, 1, 0])
def test_make_coffee_success(mock_input, capsys):
    coffee_machine = CoffeeMachine()
    coffee_machine.make_coffee("espresso")
    captured = capsys.readouterr()
    assert captured.out == "Insert coins:\nHere is $0.25 in change.\nHere is your espresso. Enjoy!\n"


@patch("builtins.input", side_effect=[0, 2, 1, 0])
def test_make_not_enough_payment(mock_input, capsys):
    coffee_machine = CoffeeMachine()
    coffee_machine.make_coffee("espresso")
    captured = capsys.readouterr()
    assert captured.out == "Insert coins:\nInsuficient payment!\n"


@patch("builtins.input", side_effect=[10, 2, 1, 0])
def test_make_not_enough_resources(mock_input, capsys):
    coffe_machine = CoffeeMachine()
    coffe_machine.resources = {
        "water": 0,
        "milk": 0,
        "coffee": 0,
    }
    coffe_machine.make_coffee("latte")

    captured = capsys.readouterr()

    assert captured.out == "Sorry, there is not enough water.\n"


@patch("builtins.input", side_effect=[10, 2, 1, 0])
def test_make_no_coffe(mock_input, capsys):
    coffe_machine = CoffeeMachine()
    coffe_machine.make_coffee("latte machiato")

    captured = capsys.readouterr()

    assert captured.out == "We don't have that coffe here.\n"
