def write_log_out(message):
    with open(r'data\log.txt', 'a') as f:
        f.write(message + '\n')


def clean_and_split_email(email):
    if '@' not in email:
        print('The provided email has no \'@\'.')
        return None
    
    email = email.strip().lower()
    e_address, e_domain = email.split('@')

    return {
        'username': e_address,
        'domain': e_domain
    }

def is_valid_password(password):
    return len(password) >= 8

def is_valid_email(email):
    if not email or '@' not in email or '.' not in email:
        print('error: the email has no proper format')
        return False

    username, domain = email.split('@')
    if not username or not email:
        print('error: the email has no username or domain')
        return False

    return True
    


# external
write_log_out('Your file has been deleted') 
write_log_out('API connection error 404')

# cleaning
print(clean_and_split_email('rodrigoUsa@gmail.com'))
print(clean_and_split_email('rodrigohackergmail.com'))

# validation
print(is_valid_password('asbcsdfgfasdasd'))
print(is_valid_password('a123'))

print(is_valid_email('teste@gmail.com'))
print(is_valid_email('@gmail.com'))
print(is_valid_email('@'))
print(is_valid_email('@gmail.com'))
print(is_valid_email('testegmail.com'))

# orchestrator
def process_user_email(email):
    write_log_out('Application started')
    

    if not is_valid_email(email):
        write_log_out(f'The email \'{email}\' has been denied while registration.')
    else: 
        user_info = clean_and_split_email(email)
        write_log_out(f'Processed email: {user_info['username'], user_info['domain']}')

    write_log_out('Application stopped')


email = input('enter an email')
process_user_email(email)