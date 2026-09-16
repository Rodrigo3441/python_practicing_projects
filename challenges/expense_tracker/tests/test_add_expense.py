import main
import pytest

def test_add_expense():
    expenses = []

    main.add_expense(expenses, "Lunch", 25.50)
    main.add_expense(expenses, "Bus", 5.00)

    assert expenses == [
                            {"description": "Lunch", "amount": 25.50},
                            {"description": "Bus", "amount": 5.00}
                       ]

def test_value_error_exc():
    expenses = []

    with pytest.RaisesExc(ValueError):
        main.add_expense(expenses, '', 10)

    with pytest.RaisesExc(ValueError):
        main.add_expense(expenses, 'Lunch', 0)

    with pytest.RaisesExc(ValueError):
        main.add_expense(expenses, 'Lunch', -10)

    with pytest.RaisesExc(ValueError):
        main.add_expense(expenses, '    ', 10)