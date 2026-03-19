email = 'rodrigo@gmail.com'
email = email.strip()

if email == '':
    print('Email cannot be empty')

if not('.' in email and '@' in email):
    print('Email must contain . and @.')

if email.count('@') != 1:
    print('You must use only one @.')

if not(email.endswith(('.com','.org','.net'))):
    print('your email must end with .com .org or .net')

if len(email) > 254:
    print('your email must be lower than 254 characters')

if not(email[0].isalnum() and email[-1].isalnum()):
    print('your email must start and end with only letters or numbers')

#password challenge
password = 'aaaA1261213'

if password == '':
    print('Passoword cannot be empty')

if len(password) < 8:
    print('Your password must be at least 8 characters')

if not(any(char.isupper() for char in password)):
    print('must contain at least one uppercase letter')

if not(any(char.islower() for char in password)):
    print('must contain at least one lowercase letter')

if password == email:
    print('The passworld cannot be identical to Email')

if password.count(' ') != 0:
    print('password cannot have spaces')

if not(password[0].isalnum() and password[-1].isalnum()):
    print('your password must start and end with a letter or digit')

