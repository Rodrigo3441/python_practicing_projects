import main

def test_find_expenses_by_description():
    expenses = []

    assert main.find_expenses_by_description(expenses, 'asd') == []

    expenses = [
    {"description": "Lunch", "amount": 25.50},
    {"description": "Bus", "amount": 5.00},
    {"description": "lunch", "amount": 30.00},
    {"description": "Coffee", "amount": 8.50}
    ]

    assert main.find_expenses_by_description(expenses, "  LUNCH ") == [
                                                                            {"description": "Lunch", "amount": 25.50},
                                                                            {"description": "lunch", "amount": 30.00}
                                                                        ]