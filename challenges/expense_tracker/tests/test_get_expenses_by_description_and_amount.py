import main
import pytest

def test_empty_list():
    expenses = []
    assert main.get_expenses_by_description_and_amount(expenses, '', -10) == []

def test_bad_description():
    expenses = [{"description": "Lunch", "amount": 25.50}]
    with pytest.RaisesExc(ValueError):
        main.get_expenses_by_description_and_amount(expenses, '', -10)

def test_bad_min_value():
    expenses = [{"description": "Lunch", "amount": 25.50}]
    with pytest.RaisesExc(ValueError):
        main.get_expenses_by_description_and_amount(expenses, 'apple', -30)

def test_normal_case():
    expenses = [
    {"description": "Lunch", "amount": 25.50},
    {"description": "Bus", "amount": 5.00},
    {"description": "Lunch", "amount": 40.00},
    {"description": "Coffee", "amount": 8.50}
    ]

    result = main.get_expenses_by_description_and_amount(
        expenses,
        " lunch ",
        30
    )
    assert result == [
                        {"description": "Lunch", "amount": 40.00}
                    ]

    result = main.get_expenses_by_description_and_amount(
        expenses,
        "LUNCH",
        20
    )
    assert result == [
                        {"description": "Lunch", "amount": 25.50},
                        {"description": "Lunch", "amount": 40.00}
                    ]