# Number Guessing Game
# User chooses the number-range
# Computer picks a random number between 0 and the number chosen by user
# User guesses until correct
# hints: too high / too low
# Made by Rodrigo SG, January, 27th 2026
import random

def only_numbers():
    print('Enter only integer numbers!')
    return 0

while True:
    try:
        number_range = int(input('Type the range you want the numbers to be generated (at least 10): '))
    except ValueError:
        only_numbers()
    else:
        if number_range < 10:
            print('use only integer numbers higher than 10')
        else:
            break

computer_number = int(random.random() * number_range)
user_number = None
attempts = 0
print(f'Number guessing game, range: 0 - {number_range-1}')
print('=' * 40)

while user_number != computer_number:
    try:
        user_number = int(input('Enter a number: '))
    except ValueError:
        only_numbers()
    else: 
        if user_number >= 0 and user_number < number_range:
            attempts += 1
            if user_number == computer_number:
                print('You found the number! congratulations')
                print(f'Number of attempts: {attempts}')
                break
            elif user_number < computer_number:
                print('Too low, try again')
            else:
                print('Too high, try again')
        else:

            print(f'Do not enter a number outsite the range! (0 - {number_range-1})')
