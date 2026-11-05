def total(a=0, b=0, c=0, d=0):
    print(a + b + c + d)


def total_modern(*args):
    print(sum(args))


def create_user(**kwargs):
    print(kwargs)


total(5, 2)
total(5, 2, 4)
total(5, 2, 4, 9)

total_modern(5, 2)
total_modern(5, 2, 4)
total_modern(5, 2, 4, 9)

create_user(first_name='michael', last_name='test', age=33, country='egypt')
create_user(first_name='rodrigo', country='usa')

