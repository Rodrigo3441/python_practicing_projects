def save_in_history(filename, number1, operator, number2, result):
    with open(filename, 'a') as f:
        f.write(f'{number1},{operator},{number2},{result}\n')