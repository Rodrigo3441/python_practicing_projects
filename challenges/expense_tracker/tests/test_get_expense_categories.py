import main

def test_empty_list():
    expenses = []
    assert main.get_expense_categories(expenses) == []

def test_normal_case():
    expenses = [
    {"description": "Lunch", "amount": 25.50},
    {"description": "Bus", "amount": 5.00},
    {"description": "lunch", "amount": 30.00},
    {"description": "Coffee", "amount": 8.50},
    {"description": "BUS", "amount": 10.00}
    ]
    result = main.get_expense_categories(expenses)
    assert result == ["Lunch", "Bus", "Coffee"]

    expenses = [
    {"description": "  Rent  ", "amount": 1000},
    {"description": "rent", "amount": 500}
    ]
    result = main.get_expense_categories(expenses)
    assert result == ["  Rent  "]