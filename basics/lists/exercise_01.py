#students db
students = [
    ["Alice", 8.5, 7.0, 9.0],
    ["Bob", 6.0, 5.5, 6.5],
    ["Carol", 9.5, 9.0, 10.0]
]
#averages stored
averages = []

#treating the information
name, s1, s2, s3 = students[0]
print(name, s1, s2, s3)

#calculing and printing the alice avg
avg = (s1+s2+s3)/3
print('Alice average:', avg)

#calculing individual avg
for name, s1, s2, s3 in students:
    avg = (s1+s2+s3)/3
    print(name, '->',avg)
    averages.append([name,avg])

#printing the averages list
print(averages)
first_student, second_student, third_student = averages


print(first_student)
print(second_student)
print(third_student)