# Expense Tracker

A small in-memory expense tracker built with Python as part of my programming practice projects.

The challenge was developed incrementally, implementing one function at a time and writing unit tests to verify each function's behavior.

## Features

- Add expenses
- Calculate the total of expenses
- Calculate the average expense
- Find expenses by description
- Filter expenses by minimum amount
- Filter expenses by description and amount
- Remove expenses
- Update expense amounts
- Generate an expense summary
- Extract unique expense descriptions
- Group expenses by description

## Project Structure

```text
expense_tracker/
├── main.py
└── tests/
    ├── test_add_expense.py
    ├── test_find_expenses_by_description.py
    ├── test_get_expenses_by_amount.py
    ├── test_get_expenses_by_description_and_amount.py
    ├── test_get_expenses_summary.py
    ├── test_get_total.py
    ├── test_get_average_expense.py
    ├── test_get_expense_categories.py
    ├── test_remove_expense.py
    └── test_update_expense_amount.py
```

## Concepts Practiced

- Functions and type hints
- Lists and dictionaries
- Loops and conditionals
- Input validation
- List filtering
- Data transformation
- In-place updates
- Reusing functions
- Handling edge cases
- Unit testing with pytest