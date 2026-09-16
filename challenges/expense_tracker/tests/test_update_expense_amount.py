import main
import pytest

def test_empty_list():
    expenses = []
    assert main.update_expense_amount(expenses, " lunch ", 40.00) == False

def test_bad_description():
    expenses = [{"description": "Lunch", "amount": 25.50}]
    with pytest.RaisesExc(ValueError):
        main.update_expense_amount(expenses, '', 420)

def test_bad_amount():
    expenses = [{"description": "Lunch", "amount": 25.50}]
    with pytest.RaisesExc(ValueError):
        main.update_expense_amount(expenses, 'lunch', 0)

def test_normal_case():
    expenses = [
    {"description": "Lunch", "amount": 25.50},
    {"description": "Bus", "amount": 5.00},
    {"description": "Lunch", "amount": 30.00}
    ]

    updated = main.update_expense_amount(expenses, " lunch ", 40.00)

    assert updated == True
    assert expenses == [
                            {"description": "Lunch", "amount": 40.00},
                            {"description": "Bus", "amount": 5.00},
                            {"description": "Lunch", "amount": 30.00}
                        ]