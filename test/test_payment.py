from src.coffee_machine import CoffeeMachine

import pytest

# Create a fixture to instantiate the class for testing


@pytest.fixture
def payment_test():
    return CoffeeMachine()

# Write individual test cases


def test_get_payment_insufficient_payment(payment_test, capsys, monkeypatch):
    price = 10

    input_values = '2\n0\n1\n1\n'
    inputs = input_values.split('\n')
    monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))

    payment_test.get_payment(price)  # Call the function

    # Capture the printed output
    captured = capsys.readouterr()
    output = captured.out.strip()

    assert output == "Insert coins:\nInsuficient payment!"
    assert payment_test.money == 0


# Test case for sufficient payment
def test_get_payment_sufficient_payment(payment_test, capsys, monkeypatch):
    price = 10

    input_values = '40\n4\n0\n2\n'
    inputs = input_values.split('\n')
    monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))

    payment_test.get_payment(price)  # Call the function

    # Capture the printed output
    captured = capsys.readouterr()
    output = captured.out.strip()

    assert output == f"Insert coins:\nHere is $0.42 in change."
    assert payment_test.money == price
