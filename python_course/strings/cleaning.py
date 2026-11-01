# cleaning
text = '#####Engineering####'
text = text.strip('#')
print(len(text))
print(text)

print('='*50)
new_text = '31 3123 13 31    '
print(len(new_text))
new_text = new_text.strip()
print(len(new_text))

# cases

text = 'python PROGRAMMING'
print(text.lower())
print(text.upper())

search = 'Email'.lower().strip()
data = 'emAil'.lower().strip()

print(search == data)

# challenge
messy = '968-Maria, ( d@t@ Engineer );; 27y  '
messy = messy.lower().strip()
messy = messy.replace('@','a').replace('(','').replace(')','')
messy = messy.split(',')

phone, name = messy[0].split('-')
role, age = messy[1].split(';;')

role = role.strip()
age = age.strip().replace('y','')

print(messy)

print(f'number: {phone} | name: {name} | role: {role} | age: {age}')