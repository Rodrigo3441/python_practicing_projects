def clean_active_users(users):
    return [
        {
            'id': user['id'],
            'name': user['name'].strip(),
            'email': user['email'].lower()
        }
        for user in users
        if user['active']
    ]


users = [
    {"id": 1, "name": "  Alice  ", "email": "ALICE@EXAMPLE.COM", "active": True},
    {"id": 2, "name": "Bob", "email": "BOB@EXAMPLE.COM", "active": False},
    {"id": 3, "name": "  Charlie", "email": "CHARLIE@EXAMPLE.COM", "active": True},
    {"id": 4, "name": "Diana  ", "email": "DIANA@EXAMPLE.COM", "active": True},
    {"id": 5, "name": " Eve ", "email": "EVE@EXAMPLE.COM", "active": False},
]

result = clean_active_users(users)

for i in result:
    print(i)