person = 'Rodrigo,24,USA,12062006'
person_list = person.split(',')
print(person_list)

date = "2024-03-15T20:00:00Z"
date = date.replace('Z','')
date = date.split('T')
date = date[0]

print(date.split('-'))

# minute 29:00
csv_file = '1234,rodrigo,USA,m'
print(csv_file.split(','))

print('='*99)