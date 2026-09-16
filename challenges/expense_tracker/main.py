def get_expense_categories(expenses: list) -> list:
    if not expenses:
        return []

    result = []
    added = []

    for expense in expenses:
        # standardizes the current expense description in order to make it unique
        target = expense['description'].lower().strip()

        if target not in added:
            added.append(target)
            result.append(expense['description'])

    return result


def get_expenses_by_description_and_amount(
        expenses: list,
        description: str,
        min_amount: float
) -> list:
    if not expenses:
        return []

    if not description.strip() or min_amount < 0:
        raise ValueError    

    normalized_description = description.strip().lower()
    result = []
        
    for expense in expenses:
        if (expense['description'].lower() == normalized_description and
            expense['amount'] >= min_amount):
            result.append(expense)

    return result

def update_expense_amount(expenses: list, description: str, new_amount: float):
    if not expenses:
        return False

    if not description.strip() or new_amount <= 0:
        raise ValueError

    normalized_description = description.strip().lower()
    
    for expense in expenses:
        if expense['description'].lower() == normalized_description:
            expense['amount'] = new_amount
            return True

    return False


def get_expenses_summary(expenses: list):
    summary = {
                "total": 0,
                "average": 0,
                "count": 0
              }

    if not expenses:
        return summary

    summary['total'] = get_total(expenses)
    summary['count'] = len(expenses)
    summary['average'] = get_average_expense(expenses)

    return summary

def get_average_expense(expenses: list) -> float:
    if not expenses:
        return 0

    return get_total(expenses) / len(expenses)

def get_expenses_by_amount(expenses: list, min_amount: float) -> list:
    if not expenses:
        return []

    result = []

    for expense in expenses:
        if expense['amount'] >= min_amount:
            result.append(expense)

    return result

def remove_expense(expenses: list, description: str) -> bool:
    if not expenses:
        return False

    normalized_description = description.strip().lower()

    for expense in expenses:
        if expense['description'].lower() == normalized_description:
            expenses.remove(expense)
            return True

    return False


def find_expenses_by_description(expenses: list, description: str) -> list:
    if not expenses:
        return []

    result = []
    normalized_description = description.strip().lower()

    for expense in expenses:
        if expense['description'].lower() == normalized_description:
            result.append(expense)

    return result

    

def get_total(expenses: list) -> int:
    if not expenses:
        return 0

    total = 0

    for expense in expenses:
        total += expense['amount']

    return total

def add_expense(expenses: list, description: str, amount: float) -> None:
    if not description.strip():
        raise ValueError

    if amount <= 0:
        raise ValueError
    
    expense = {
        'description': description,
        'amount': amount
    }

    expenses.append(expense)
    return None


expenses = []

add_expense(expenses, "Lunch", 25.50)
add_expense(expenses, "Bus", 5.00)


print(expenses)

print(get_total(expenses))


print(find_expenses_by_description(expenses, 'lunch'))

print(remove_expense(expenses, 'lunch'))

print(expenses)
