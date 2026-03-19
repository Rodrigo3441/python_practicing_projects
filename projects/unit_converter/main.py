# 3. Unit Converter
# goal: convert one unit into another one
# Celsius to Fahrenheit
# Km to Miles
# Kg to Pounds
# Creation day: January 28th 2026
# Last Modification: January 29th 2026


import console_treat as console
import fah_celsius as temperature

print('=' * 50)
print('Unit Converter | By Rodrigo')
print('\nChoose what do you want to convert: ')
print('1- Celsius|Fahrenheit')
print('=' * 50)


while True:
    option = input().strip()

    match option:
        case '1':
            console.clear()
            temperature.run_temp_converter()
        case _:
            print('Wrong option, try again: ')

     