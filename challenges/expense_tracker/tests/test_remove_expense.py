import main

def test_remove_expense():
    expenses = []

    assert main.remove_expense(expenses, 'test') == False
    expenses = [
    {"description": "Lunch", "amount": 25.50},
    {"description": "Bus", "amount": 5.00},
    {"description": "Lunch", "amount": 30.00}
    ]

    removed = main.remove_expense(expenses, " lunch ")

    assert removed == True
    assert expenses == [
                            {"description": "Bus", "amount": 5.00},
                            {"description": "Lunch", "amount": 30.00}
                        ]

    removed = main.remove_expense(expenses, " Rent ")
    assert removed == False