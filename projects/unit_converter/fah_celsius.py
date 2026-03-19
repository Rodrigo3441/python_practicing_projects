def run_calculator(option):
    temperatures = ('Celsius','Fahrenheit')
    try:
        user_temperature = float(input(f'Enter your {temperatures[option]} temperature: '))
    except Exception as e:
        print(f'An error has occurred: {e}')
    else:
        match option:
            #Celsius to Fahrenheit
            case 0:
                fah_temperature = (1.8 * user_temperature) + 32
                print(f'{user_temperature}°C is equal to {fah_temperature}°F')

            #Fahrenheit To Celsius
            case 1:
                celsius_temperature = (5/9) * (user_temperature - 32)
                print(f'{user_temperature}°F is equal to {celsius_temperature}°C')


def run_temp_converter():
    print('=' * 50)
    print('Temperature Converter')
    print('{CF} if you want to convert Celsius to Fahrenheit,')
    print('{FC} if you want to convert Fahrenheit to Celsius')
    print('=' * 50)

    while True:
            option = input().strip().lower()

            if option not in ('cf','fc'):
                print('invalid option, enter CF or FC')
                continue

            #0 -> C to F mode and 1 -> F to C mode
            operation = 0 if option == 'cf' else 1

            match option:
                case 'cf':
                    run_calculator(operation)
                    break
                case 'fc':
                    run_calculator(operation)
                    break


