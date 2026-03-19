# dictionary-problem-set
# author: Rodrigo SG
# started date: March 13th 2026
# Currently on: Problem 8

# p1 - basic dictionary creation
def create_student(name: str, age: int, grade: float) -> dict:
   return  {
        'name': name,
        'age': age,
        'grade': grade 
        }

# p2 - Accessing Values
def get_grade(student: dict) -> float:
    return student['grade']


# p3 - updating dictionary grade
def update_grade(student: dict, new_grade: float) -> dict:
    student['grade'] = new_grade
    return student


# p4 - counting words
def count_words(text: str) -> dict:
    """
        return how many times a word has appeared inside a string

    """
    string_text = text.replace(',','').replace('.','').split()
    words = {}


    for word in string_text:
        words[word] = string_text.count(word)
    
    return words


# p5 - most freqeunt word
def most_frequent_word(text: str) -> str:
    string_text_counted = count_words(text)

    sorted_dict = list({
    key: value for key,
    value in sorted(string_text_counted.items(),
    key=lambda item: item[1])
    })

    return sorted_dict[-1]



# p6 - class average
def class_average(grades: dict) -> float:
    return sum(grades)/len(grades)

# p7 - invert a dictionary
def invert_dicionary(d: dict) -> dict:

    inverted_d = {
        key: value for key,
        value in sorted(d.items(), reverse=True)
    }
    
    return inverted_d

# p8 - inventory system
def add_item(inventory: dict, item: str) -> dict:
    #i stopped here
    pass




dict_words = count_words('apple banana apple orange banana apple banana banana banana')


# p3 - test cases
print('Problem 3 - test case')
rodrigo = create_student('Rodrigo', 19, 10)
print(rodrigo)
print(update_grade(rodrigo, 8))

# p4 - test cases
print('Problem 4 - test case')
print(count_words('My mom got three kid, my dad got three kids, so i got two brothers'))

# p5 - test cases
print('Problem 5 - test case')
print(most_frequent_word('apple banana apple orange banana apple banana banana banana'))

# p6 - test cases
print('Problem 6 - test case')
grades = []
grades.append(get_grade(create_student('Rodrigo', 19, 8.5)))
grades.append(get_grade(create_student('Baraa', 40, 9.8)))
grades.append(get_grade(create_student('Maria', 34, 7.6)))
print(class_average(grades))

# p7 - invert a dictionary
print(invert_dicionary({"a": 1, "b": 2, "c": 3}))