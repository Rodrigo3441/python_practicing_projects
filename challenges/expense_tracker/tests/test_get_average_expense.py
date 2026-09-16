import main

def test_get_average_expense():
    expenses = []
    result = main.get_average_expense(expenses)
    assert result == 0

    expenses = [
    {"description": "Lunch", "amount": 20.00},
    {"description": "Bus", "amount": 10.00},
    {"description": "Coffee", "amount": 6.00}
    ]
    result = main.get_average_expense(expenses)
    assert result == 12