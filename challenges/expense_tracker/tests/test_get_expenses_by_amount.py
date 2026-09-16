import main

def test_get_expenses_by_amount():
    expenses = []
    assert main.get_expenses_by_amount(expenses, 10) == []

    expenses = [
    {"description": "Lunch", "amount": 25.50},
    {"description": "Bus", "amount": 5.00},
    {"description": "Coffee", "amount": 8.50},
    {"description": "Rent", "amount": 1000.00}
    ]

    result = main.get_expenses_by_amount(expenses, 10)
    assert result == [
                        {"description": "Lunch", "amount": 25.50},
                        {"description": "Rent", "amount": 1000.00}
                    ]

    result = main.get_expenses_by_amount(expenses, 0)
    assert result == expenses