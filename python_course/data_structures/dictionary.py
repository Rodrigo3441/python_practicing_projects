#ordered
#key are unique
# values can be duplicated
# not indexed
# mutable
def first_test():
    customer01 = {
        'a': 10,
        'b': 20,
        'c': 30
    }

    print(customer01)
    print(customer01['a'])
    customer01['c'] = 40
    print(customer01)

def methods():
    user = {
        'id': 1,
        'age': 30,
        'city': 'clay'
    }
    
    #access
    print(user['id']) # exception
    print(user.get('name', 'n/a')) # no exception

    #checks
    print('age' in user)
    print('name' in user)

    #view objects
    print(user.keys())
    print(user.values())
    print(user.items())

    for key, value in user.items():
        print(key, value)

    # add remove update
    user['name'] = 'rod'
    user['age'] = 55
    print(user)

    user.update({'age': 19, 'city': 'paris'})
    print(user)

    print(f'removing: {user.pop('age', 'not found')}') # raises exception
    print(user)

    user.popitem()
    print(user)

    # creation
    user = dict.fromkeys(['id','name','age','city'], None)
    print(user)

    # challenge
    user = {
        'id': 1,
        'name': 'John',
        'age': 30,
        'city': 'Berlin'
    }

    # new_user = {}

    # for key, value in user.items():
    #     if isinstance(value, str):
    #         new_user[key] = value.upper()

    # print(new_user)

    new_user = {
        key: value.upper()
        for key, value in user.items()
        if isinstance(value, str)
    }
     
    print(new_user)

methods()