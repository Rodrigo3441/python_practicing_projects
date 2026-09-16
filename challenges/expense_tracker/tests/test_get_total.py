import main

def test_get_total():
    expenses = []

    assert main.get_total(expenses) == 0

    expenses = [
        {"description": "Lunch", "amount": 25.50},
        {"description": "Bus", "amount": 5.00},
        {"description": "Coffee", "amount": 8.50}
    ]

    assert main.get_total(expenses) == 39.00