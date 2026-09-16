import main

def test_get_expenses_summary():
    expenses = []
    result = main.get_expenses_summary(expenses)
    assert result == {
                        "total": 0,
                        "average": 0,
                        "count": 0
                    }

    expenses = [
    {"description": "Lunch", "amount": 20.00},
    {"description": "Bus", "amount": 10.00},
    {"description": "Coffee", "amount": 6.00}
    ]

    summary = main.get_expenses_summary(expenses)

    assert summary == {
                        "total": 36.00,
                        "average": 12.00,
                        "count": 3
                    }