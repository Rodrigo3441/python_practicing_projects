#list
colors = ['red','yellow','blue','green','purple']

print(colors[2])
print(colors)
colors.reverse()
colors.append('potato')
colors.insert(2,'pineapple')
print(colors)
colors.sort()
print(colors)


#tuple
country = (1,2,3,4,5,6,'potato',3,4)
print(country)

country_list = list(country)

print(country_list)

country_list.append('fuc')
print(country_list)

#dictionary

user = {
    "name": "rodrigo",
    "height": 1.87,
    "age": 19,
    "is_working": True
    }

print(user)



