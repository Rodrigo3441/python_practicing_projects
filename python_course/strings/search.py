# search
print(f'{'feb' in '2026-feb-10'}')

phone1 = '+49-176-123123'
phone2 = '48-654-16123'

print(phone1.startswith('+49'))

print(phone1[phone1.find('-')+1:])
print(phone2[phone2.find('-')+1:])


print(phone1.find('-'))


email = 'rodrigo@gmail.com'
print(email.endswith('gmail.com'))
print('@' in email)

file = 'data_backup.csv'
print(file.endswith('.csv'))

url = 'https://api.company.com/v1/data'
print('/api' in url)

# validations
country = 'USA'
print(country.isalpha())

phone = '123123123-113'
print(phone.isnumeric())
print(phone.replace('-','').isnumeric())