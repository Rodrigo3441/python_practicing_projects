# Transforming strings
date = '2026/10/31'
print(date.replace('/', '-'))

price = '1234,56'
print(price.replace(',','.'))

price = '$1,299.99'
price = price.replace('$','').replace(',','')
print(float(price))

phone = '176-1234-534'
print(phone.replace('-','/'))
print(phone.replace('-',''))

# Challenge
number_messy = '+49 (176) 123-4567'
symbols = [
    '+',
    '(',
    ')',
    '-',
    ' '
]

for symbol in symbols:
    number_messy = number_messy.replace(symbol, '')

print(number_messy)