# Simple Calculator
# Ask for two numbers and an operation (+ - * /)
# Handle invalid input with try/except

# You prctice: functions, input validation, branching
# Made by Rodrigo SG January 27th 2026

# +, -, /, *
import console_treat as console
import save_in_history as sav

def ask_number(n):
    messages = ('Enter the first number: ','Enter the second number: ')
    while True:
        try:
            temp = float(input(messages[n]))
        except ValueError:
            print('Use only numbers!')
        else:
            return temp
        
# unique function
def general_function(operator):
    number1 = ask_number(0)
    number2 = ask_number(1)

    match operator:
        case '+':
            result = round(number1 + number2, 3)
            sav.save_in_history('sum_history.csv', number1, operator, number2, result)
            return result
        case '-':
            result = round(number1 - number2, 3)
            sav.save_in_history('subtraction_history.csv', number1, operator, number2, result)
            return result
        case '*':
            result = round(number1 * number2, 3)
            sav.save_in_history('multiply_history.csv', number1, operator, number2, result)
            return result
        case '/':
            if number2 == 0:
                print('Division by zero not allowed')
                return None
            result = round(number1 / number2, 3)
            sav.save_in_history('division_history.csv', number1, operator, number2, result)
            return result
        case _:
            pass

            
while True:
    
    console.clear()

    print('Rodrigo\'s Calc')
    print('='*30)
    operation = str(input('Choose the operation\n' \
                        '+ for sum\n' \
                        '- for subtraction\n' \
                        '* for multiplication\n' \
                        '/ for division\n' \
                        '0 to exit: ')).strip()


    if operation in ('+','-','*','/'):
        result = general_function(operation)
        if result is not None:
            print(result)
        console.pause()

    elif operation == '0':
        print('Thanks for using Rodrigo\'s calculator')
        break

    else:
        print('Wrong operator, try again')


