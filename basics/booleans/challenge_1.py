#1- check if a user's name is not empty and the age is greater than or equal to 18
name = ''
age = 19
print(name != '' and age >= 18)

#2- check if the password is at least 8 characters long and does not contain spaces
password = '2sfrff 4da'

print(len(password)>=8 and len(password) == len(password.replace(' ','')))


#3- check if a user's email is not empty, contains '@', and ends with '.com'
email = 'test@gmail.com'

print(email != '' and email.find('@') != -1 and email.endswith('.com'))


#4- check if a username is a string, is not None, and is longer than 5 characters
username = 'rodrigo'

print(isinstance(username,str) and username != None and len(username) > 5)


#5- check if the user is either an admin or a moderator, and either they're not banned or they've verified their email
user = 'admin'
is_banned = True
verified_email = True

print((user == 'admin' or user == 'moderator') and (not is_banned or verified_email))