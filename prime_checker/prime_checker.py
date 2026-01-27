from math import sqrt
#check if a number is prime

def is_prime(number):
    number_sqrt = int(sqrt(number))

    counter = 2

    while counter <= number_sqrt:
        if not (number % counter):
            return False

        counter += 1
    else:
        return True


while True:
    try:
        number = int(input('enter an integer number: '))
        if number < 0:
            print('number must be higher or equal to 0')
            continue

    except ValueError:
        print('Enter only numbers!')
        
    else:
        if number in (0,1):
            print(f'{number} is not a prime')
            break
        else:
            if is_prime(number):
                print('this is a prime number')
            else:
                print('this is not a prime number')
            break


