# Transformations
first_name = 'Rodrigo'
last_name = 'Galvão'

full_name = first_name + ' ' +  last_name
print(full_name)

list_of_names = [first_name, ' ', last_name]

ss_full_name = ''.join(list_of_names)
print(ss_full_name)

folder = 'C:/Users/Rodrigo'
file = 'report.csv'
full_path = folder + '/' + file
print(full_path)

name = 'Rodrigo'
age = 19
is_student = False
print(f'My name is {name} and i\'m {age}. {'i am a student' if is_student else 'i am doing nothing'}')
print(f'2 + 3 = {{This is me}}')