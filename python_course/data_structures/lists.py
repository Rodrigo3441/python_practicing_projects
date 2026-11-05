
def list_unpacking():
    person = ['rodrigo', 19, 'male', 'usa']
    name, age, gender, country = person

    print(name, age, gender, country)

    car = ['fiat', '2018', 'gray']
    year, *details = car
    print(year, details)

    computer = ['dell', '8gb', 1200]
    brand, *_ = computer

    print(brand)


def analyze_and_explore():
    numbers = [1,5,4,3,2,6,4,3,2]
    print('max: ', max(numbers))
    print('min: ', min(numbers))
    print('sum: ', sum(numbers))
    print('len: ', len(numbers))

    print('all: ', all(numbers))
    print('all: ', all([1,2,5,5, None]))

    print('any: ', any(numbers))
    print('any: ', any([0,0,0,None]))

    print('count: ', numbers.count(2))
    print('index: ', numbers.index(2))

    print(4 in numbers)
    print(99 in numbers)

def combine_lists():
    letters = ['a', 'b','c']
    numbers = [1, 2, 3]
    print(letters + numbers)

    comb = [letters, numbers]
    print(comb)

    letters.extend(numbers)
    print(letters)

    # combine with zip
    zipped_list = list(zip(letters, numbers))
    print(zipped_list)

    ids = [101, 102, 103]
    names = ['ori', 'blind', 'forest']
    print(list(zip(ids, names)))


def iterator_iterable():
    # map, filter, enumerate
    list1 = [1,4,3,2,5,6,7,8,3,12,145]
    en_list1 = enumerate(list1)
    # print(list(en_list1))

    for index, value in en_list1:
        print(index, value)

    print(list(reversed(list1)))

    low_letters = ['a','b','k','dk']
    upper_letters = list(map(str.upper, low_letters))

    upper_letters = [letter.upper() for letter in low_letters]
    print(upper_letters)

    messy_data = ['sql','3','66','abc','dfg']
    print(list(filter(str.isalpha, messy_data)))

def lambda_function():
    multiple = lambda x: x**2
    print(multiple(10))

    clark = lambda x, y: x + y
    print(clark(10,2))

    is_in = lambda s: s in 'apple'
    print(is_in('ap'))

    # lambda + map
    prices = ['$20.13', '$12.50', '$33.90']
    
    convert_price = lambda p: float(p.replace('$',''))
    print(list(map(convert_price, prices)))

    # lambda + filter
    prices = [120, 34123, 32, 543]
    print(list(filter(lambda p: p >= 100, prices)))

    students = [['maria', 85],['kumar',90],['max',60]]
    print(list(filter(lambda p: p[1] > 70 and p[0].startswith('m'), students)))


def list_comprehension():
    domains = ['www.google.com', 'openai.com', 'localhost', 'WWW.DATAWITHBARAA.COM']
    domains = [domain.lower().replace('www.','') for domain in domains if domain.lower().endswith('.com')]
    print(domains)


# list_unpacking(
# analyze_and_explore()
# combine_lists()
# iterator_iterable()
# lambda_function()
list_comprehension()