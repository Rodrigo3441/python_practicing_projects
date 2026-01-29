def fah_to_celsius():
    pass

def celsius_to_fah():
    try:
        celsius_temperature = float(input('Enter the celsius temperature you want to convert: '))
    except ValueError:
        print('Wrong value, try again')
    else:
        fah_temperature = (1.8 * celsius_temperature) + 32
        print(f'The {celsius_temperature}°C in Fahrenheit is {fah_temperature}')