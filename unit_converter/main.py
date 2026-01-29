# 3. Unit Converter
# Examples:
# Celsius ↔ Fahrenheit
# Km ↔ Miles
# Kg ↔ Pounds
# Made by Rodrigo SG, January 28th 2026

import console_treat as console
import fah_celsius as temperature

print('=' * 50)
print('Unit Converter')
print('\nChoose what do you want to convert: ')
print('1- Celsius|Fahrenheit')
print('=' * 50)


while True:
    try:
        option = str(input())
    except:
        print('An error has occourred')
    else:
        match option:
            case '1':
                temperature.celsius_to_fah()
            case _:
                print('Wrong option, try again: ')

     